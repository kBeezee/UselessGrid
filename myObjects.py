from globals import *
from numpy import *
from mapping import *
from mapping import PlayerOutOfBounds
#import drawing
import pygame
from random import *

BattleCursor = None
def getTileCoordinates(point, tileHeight):
    tempPt = [math.floor(point[1] / tileHeight), math.floor(point[0] / tileHeight)]
    return tempPt

def isoTo2D(Point):
    tempPt = [(2 * Point[1] + Point[0]) / 2, (2 * Point[1] - Point[0]) / 2]
    return tempPt
    #}
    #function isoTo2D(pt:Point):Point{
    #var tempPt:Point = new Point(0, 0);
    #tempPt.x = (2 * pt.y + pt.x) / 2;
    #tempPt.y = (2 * pt.y - pt.x) / 2;
    #return(tempPt);
    #}

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

        #self.iso = [(x-y)+3*64, ((x+y)/2)+1*64] #the +3*64 and +1*64 are for a 'border' and the -4 and -12 are for centering on top of tile
        self.iso = [((x - y)+3*64)-4, (((x+y)/2)+1*64)-12]
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
            #Here, we are blitting the cursor to the sprite, but we have to make it a 64x64 surface, then put the smaller
            #battle cursor on that surface, and adjust it to the top middle. then cursor to sprite, then sprite to screen.
            cSelected1 = self.get64x64Surface(BattleCursor, (16,self.cImage+4))
            cSelected1.set_colorkey((0,0,0))
            cSelected1.blit(self.surface[self.cImage], (0,32))
            self.rect = fScreen.blit(cSelected1, (self.iso[0],self.iso[1]-32))
            cSelected1 = None
        else:
            self.rect = fScreen.blit(self.surface[self.cImage], self.iso)
            self.rect = pygame.Rect(self.rect[0]+16, self.rect[1], self.rect[2]-32, self.rect[3]-32)

    def get64x64Surface(self, surface, loc=(16, 16)):
        tempSurface = pygame.Surface((64, 64))
        tempSurface.set_colorkey((0,0,0))

        #This will be important because of the tuple on the end, it decides where on the transparent surface
        #the sprite goes. (16, 16) = center, (16,0) = topcenter
        tempSurface.blit(surface, loc)
        return tempSurface

    def select(self):
        print "You clicked a sprite located at %s" % str(self.cart)
        self.selected = True


class Tiles(pygame.sprite.Sprite):
    def __init__(self, tileset, y, x):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.add(AllTiles)
        self.TileNumber = len(AllTiles) #count of all tiles
        self.surface = tileset[randrange(0, 4)] # decide what tile to use.
        self.rect = self.surface.get_rect()
        self.cart = [x, y]
        x *= self.rect.height/2
        y *= self.rect.width/2
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
        self.rect = pygame.Rect(0,0,0,0)
        self.mPos = pygame.mouse.get_pos()
        self.mPos = (self.mPos[0], self.mPos[1])
        self.cart = [0, 0]


        #ScreenCords to Map Cords
        print self.mPos #x= [0]
        xCursor = self.mPos[0]
        yCursor = self.mPos[1]
        TILE_HEIGHT = 64 / 2
        TILE_WIDTH = 64
        xMouseTile = (xCursor / TILE_WIDTH / 2 + yCursor / TILE_HEIGHT / 2) / 2;
        yMouseTile = (yCursor / TILE_HEIGHT / 2 - xCursor / TILE_WIDTH  / 2) / 2;
        print (xMouseTile, yMouseTile)
        #public PointF AbsoluteToMap(PointF screenPoint)
        #{
        #PointF mapPoint = new PointF();
        #screenPoint.X /= (Scale / 2);
        #screenPoint.Y /= (Scale / 4);
        #
        #mapPoint.X = (screenPoint.X + screenPoint.Y) / 2;
        #mapPoint.Y = (screenPoint.X - screenPoint.Y) / 2;
        #return mapPoint;
        #}
    def update(self, fScreen):
        #print "mPos: %s /t cart: %s" % (self.mPos, self.cart)
        self.rect = fScreen.blit(self.surface, self.mPos)



        self.cart = getTileCoordinates((isoTo2D((self.mPos))), 64)
        #getTileCoordinates(isoTo2D(screen point), tile height);
        #function getTileCoordinates(pt:Point, tileHeight:Number):Point{
        #var tempPt:Point = new Point(0, 0);
        #tempPt.x = Math.floor(pt.x / tileHeight);
        #tempPt.y = Math.floor(pt.y / tileHeight);
        #return(tempPt);

        #}
        #function isoTo2D(pt:Point):Point{
        #var tempPt:Point = new Point(0, 0);
        #tempPt.x = (2 * pt.y + pt.x) / 2;
        #tempPt.y = (2 * pt.y - pt.x) / 2;
        #return(tempPt);
        #}
