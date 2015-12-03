from globals import *
from numpy import *
from mapping import *
import mapping
import pygame
import random
from random import *

class Player(pygame.sprite.Sprite):
    #todo, so now the problem is that this sprite is on a grid, it needs to use the iso() function to get where it belongs.
    def __init__(self, surface, y, x, name=""):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.SpriteRect = self.surface[0].get_rect()
        self.rect = pygame.Rect(x,y,self.SpriteRect[2],self.SpriteRect[3])
        self.add(AllSprites)
        self.name = name
        self.x = x
        self.y = y
        self.rect2 = pygame.Rect((mapping.iso(self.x+8, self.y+16, 16, 16)), (32, 32))
        #todo attach this to the grid block this sprite is standing on.
        self.gridX = None
        self.gridY = None

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

        #Actual writing to screen.
        fScreen.blit(self.surface[self.cImage], mapping.iso(self.x+8, self.y+16, 16, 16))
        #fScreen.blit(pygame.transform.flip(self.surface[self.cImage], True, False), [self.BigCords[0]*self.rect[2], self.BigCords[1]*self.rect[3]])

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
        if mapping.PlayerOutOfBounds([r+fdir[0], c+fdir[1]], fdir):
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


class Tiles(pygame.sprite.Sprite):
    def __init__(self, tileset, x, y, gridX, gridY):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        #decide what tile to use.
        i = randrange(0, len(tileset))
        if i not in [0, 1, 2]:
            i = 8

        self.add(AllTiles)
        self.TileNumber = len(AllTiles)
        self.surface = tileset[i]
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        self.gridX = gridX
        self.gridY = gridY
        self.rect2 = pygame.Rect((mapping.iso(self.x, self.y, 8, 8)), (64, 64))

    def update(self, fScreen):
        fScreen.blit(self.surface, mapping.iso(self.x, self.y, 8, 8))
        #fScreen.blit(write(str(self.TileNumber)), mapping.iso(fScreen, self.x, self.y, 16, 16))


class Cursor(pygame.sprite.Sprite):
    def __init__(self, tileset, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.add(CursorTiles)
        self.TileNumber = len(CursorTiles)
        i = randrange(0, len(tileset))
        self.surface = tileset[0].copy()
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        self.rect2 = pygame.Rect((mapping.iso(self.x, self.y, 16, 16)), (64, 64))
        self.surface.set_alpha(125)

    def update(self, fScreen):
        fScreen.blit(self.surface, mapping.iso(self.x, self.y, 16, 16))