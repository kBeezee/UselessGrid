import pygame
from globals import *
import myObjects
import libSpriteSheet
import maps

#container tiles which are surfaces
tileset = []
dicScale = {'sprite': (32, 32), 'tile': (64, 64)}

""""
Really this isnt drawing anything anymore, its preparing everything to be drawn.
For sprites its getting them from a file and adding them to the sprite group.
For   tiles its getting them from a file, adding the *surfaces* to a regular list, and passing that list a function that
    after creating the sprite, adds it to the tile group.
"""""


########TILES########
#Get A TileSheet
TilesFileOne = libSpriteSheet.spritesheet("res/basic_ground_tiles-black.png")
TilesFileOne.ColorKey = (0, 0, 0)

#Define where the tiles are
blocks=[pygame.Rect(0, 0, 128, 128), pygame.Rect(128, 0, 128, 128), pygame.Rect(256, 0, 128, 128),
        pygame.Rect(384, 0, 128, 128), pygame.Rect(512, 0, 128, 128), pygame.Rect(640, 0, 128, 128),
        pygame.Rect(768, 0, 128, 128), pygame.Rect(896, 0, 128, 128)]

#turn those tiles into a list of surfaces
tileset += TilesFileOne.images_at(blocks, dicScale['tile'], colorkey=TilesFileOne.ColorKey)

#get another image with tiles/sprites
TilesFileTwo = libSpriteSheet.spritesheet("res/basic_water_tiles-black.png")
TilesFileTwo.ColorKey = (0, 0, 0)

#get a list of surfaces
tileset += TilesFileTwo.images_at(blocks, dicScale['tile'], colorkey=(0, 0, 0))

#pass tilesets to be used to make the visible map.
maps.MakeMap0(tileset)


########Sprites
#Todo, get this to snap to be on top of a tile.
""""
Here is how to do the above ^^
Step 1, call get the surface list from libSpriteSheet.py, pass the physical cords. (drawing.py)
Step 2,

when going from the top right to the right side of the screen:
As the grid[1] (y) increases, the pixel location increses by 32
as the grid[0] (y)
"""""

#this is one place holder for the player.
fftSpirteSheet = libSpriteSheet.spritesheet("res/fftFemaleWhiteMage.png") #ColorKey: Black
fftSpirteSheet.ColorKey = (255, 255, 255)
myObjects.Player(fftSpirteSheet.images_at(fftWalkingLoop, dicScale['sprite'],  colorkey=fftSpirteSheet.ColorKey), 5, 0, "p1")

#
#fftSpirteSheet = libSpriteSheet.spritesheet("res/fftFemaleBlackMage.png") #ColorKey: Black
#fftSpirteSheet.ColorKey = (255, 255, 255)
#myObjects.Player(fftSpirteSheet.images_at(fftWalkingLoop,
#                                                scale=(32,32), colorkey=fftSpirteSheet.ColorKey), x, y, "p2")
#