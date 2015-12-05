from globals import *
from numpy import *
from mapping import *
from mapping import PlayerOutOfBounds
import pygame
from random import *

class Player(pygame.sprite.Sprite):
    #todo, so now the problem is that this sprite is on a grid, it needs to use the iso() function to get where it belongs.
    def __init__(self, surface, (x, y), name=""):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        #although the spirte is scaled to 32x32 when importing the spritesheet we blit that 32x32 sprite to the
        # center of a transparent 64x64 surface.  This is to help with the isometric calculations
        for i in range(len(self.surface)):
            #note the (16,0) this is to position the sprite on the tile so it is "standing" on something.
            self.surface[i] = self.get64x64Surface(self.surface[i], (16, 0))
        self.rect = surface[0].get_rect()
        self.add(AllSprites)
        self.name = name
        self.cart = (x, y)
        x *= self.rect.height/2
        y *= self.rect.width/2
        self.selected = False

        #self.iso = [(x-y)+3*64, ((x+y)/2)+1*64] #the +3*64 and +1*64 are for a 'border'
        self.iso = [((x - y)+3*64), (((x+y)/2)+1*64)-8]
        #Animation
        self.imageCount = len(self.surface) - 1 #this is the image count.
        self.cImage = randrange(0, self.imageCount) #This is the image counter.
        self.AnimateSlower = 0
        self.AnimateDirection = 1 # this revereses the order of the pictures for a smoother animation.

    def update(self, fScreen):
        #Animation
        if self.cImage >= self.imageCount:
            self.AnimateDirection = -1
        elif self.cImage <= 0:
            self.AnimateDirection = 1

        if self.AnimateSlower > 6:
            self.cImage += self.AnimateDirection
            self.AnimateSlower = 0
        else:
            self.AnimateSlower += 1


        #look at the INIT of this object to find that although the spirte is scaled to 32x32 when importing the spritesheet
        #we blit that 32x32 sprite to the center of a transparent 64x64 surface.  This is to help with the isometric
        #calculations
        self.surface[self.cImage].set_colorkey((0,0,0))
        if self.selected:
            cSelected = pygame.Surface((64, 64))
            cSelected.fill((255,0,0))
            cSelected.set_alpha(125)
            cSelected.blit(self.surface[self.cImage], (0,32))
            #cSelected.blit(self.surface[self.cImage], self.iso)
            #self.surface[self.cImage].blit(cSelected, (16,0))
            #self.rect = fScreen.blit(cSelected, self.iso)
            fScreen.blit(cSelected, (self.iso[0],self.iso[1]-32))
        else:
            self.rect = fScreen.blit(self.surface[self.cImage], self.iso)
            self.rect = pygame.Rect(self.rect[0]+16, self.rect[1], self.rect[2]-32, self.rect[3]-32)

    def get64x64Surface(self, surface, loc=(16, 16)):
        tsur = pygame.Surface((64, 64))
        tsur.set_colorkey((0,0,0))
        tsur.fill((0,0,0))

        #This will be important because of the tuple on the end, because it decides where on the transparent surface
        #the sprite goes. (16, 16) = center
        tsur.blit(surface, loc)
        #
        return tsur


    def move(self, fBigGrid, fdir):
        # get the direction, ie +/- to x/y
        if fdir == "n":
            fdir = (0, -1)
        elif fdir == "s":
            fdir = (0, 1)
        elif fdir == "e":
            fdir = (1, 0)
        elif fdir == "w":
            fdir = (-1, 0)

        #The player object should always keep track of where it is so we dont have to hunt for it.
        r = self.BigCords[0]
        c = self.BigCords[1]
        if PlayerOutOfBounds([r+fdir[0], c+fdir[1]], fdir):
            fBigGrid[r+fdir[0]][c+fdir[1]] = self
            self.BigCords = [r+fdir[0], c+fdir[1]]
            fBigGrid[r][c] = 0 #todo this wont work, its got to remember what it was before player was there.
        return fBigGrid

    def centeronplayer(self, fTOP_LEFT):
        #We should be centering the small grid on the red blip, unless it is to close to the edge.
        #But we should allow the arrow keys to move around independent of the red blip.

        nTOP = self.BigCords[0] - 5
        nLEFT = self.BigCords[1] - 5
        if nTOP < 0:
            nTOP = 0
        elif nTOP >= MAX_HEIGHT - g_HEIGHT:
            nTOP = MAX_HEIGHT - g_HEIGHT

        if nLEFT < 0:
            nLEFT = 0
        elif nLEFT >= MAX_WIDTH - g_WIDTH:
            nLEFT = MAX_WIDTH - g_WIDTH

        return [nTOP, nLEFT]

    def select(self):
        print "You clicked a sprite located at %s" % str(self.cart)
        self.selected = True


class Tiles(pygame.sprite.Sprite):
    def __init__(self, tileset, y, x, tIndex=""):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.add(AllTiles)
        self.TileNumber = len(AllTiles) #count of all tiles

        if tIndex != "":
            self.surface = tileset[tIndex]
        else:
            self.surface = tileset[randrange(0, 1)] # decide what tile to use.

        self.rect = self.surface.get_rect()
        self.cart = [x, y]
        x *= self.rect.height/2
        y *= self.rect.width/2
        #so much props to
        #http://gamedevelopment.tutsplus.com/tutorials/creating-isometric-worlds-a-primer-for-game-developers--gamedev-6511
        self.iso = [(x-y)+3*64, ((x+y)/2)+1*64] #the +3*64 and +1*64 are for a 'border'
        #print self.cart, self.iso

    def update(self, fScreen):
        fScreen.blit(self.surface, self.iso)


class Cursor(pygame.sprite.Sprite):
    def __init__(self, fSurface=None, cart=None):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.add(CursorTiles)
        self.surface = pygame.Surface((0, 0))
        self.surface.fill((0,0,0)) #this can come out eventually
        self.surface.set_alpha(127)
        self.mPos = pygame.mouse.get_pos()
        self.mPos = (self.mPos[0], self.mPos[1])
        #self.iso = ((2*self.mPos[1] + self.mPos[0]) / 2, (2 * self.mPos[1] - self.mPos[0]) / 2)

        #afdsafd
        self.cart = (math.floor(self.mPos[0] / 64), math.floor(self.mPos[1] / 64))
        #what if i got the cartesian cords for this 10x10 rect, and then see if it is the same as any of the sprites


    def selected(self):
        for t in AllTiles:
            if (self.rect2[0] == t.rect2[0] and self.rect2[1]-31 <= t.rect2[1]):
                print "Tile Grid: %s " % [t.gridX, t.gridY]
                print "Tile: %s " % t.rect2
                print "--"
                print "Cursor Tile: %s" % self.rect2
                print self.rect2.center

    def update(self, fScreen):
        #print "mPos: %s /t cart: %s" % (self.mPos, self.cart)
        self.rect = fScreen.blit(self.surface, self.mPos)

