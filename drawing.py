import pygame
from globals import *
import myObjects
import libSpriteSheet
import maps

#container tiles which are surfaces
tileset = []
dicScale = {'sprite': (32, 32), 'tile': (64, 64)}
dictSprites = {'fArcher': 'res/fftClassSprites/fftArcherFemale.png', 'mArcher': 'res/fftClassSprites/fftArcherMale.png',
               'Bard': 'res/fftClassSprites/fftBard.png',
               'fBlackMage': 'res/fftClassSprites/fftBlackMageFemale.png', 'mBlackMage': 'res/fftClassSprites/fftBlackMageMale.png',
               'fCalculator': 'res/fftClassSprites/fftCalculatorFemale.png', 'mCalculator': 'res/fftClassSprites/fftCalculatorMale.png',
               'fChemist': 'res/fftClassSprites/fftChemistFemale.png', 'mChemist': 'res/fftClassSprites/fftChemistMale.png',
               'fWhiteMage': 'res/fftClassSprites/fftWhiteMageFemale.png', 'mWhiteMage': 'res/fftClassSprites/fftWhiteMageMale.png',




            'Cloud': 'res/fftNamedSprites/fftCloud.png'}

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
#this is one place holder for the player.
fftSpirteSheet = libSpriteSheet.spritesheet(dictSprites['fWhiteMage']) #ColorKey: Black
fftSpirteSheet.ColorKey = (255, 255, 255)
iCords = (0, 0)
myObjects.Player(fftSpirteSheet.images_at(fftWalkingLoop, dicScale['sprite'],  colorkey=fftSpirteSheet.ColorKey), iCords, "p1")

fftSpirteSheet = libSpriteSheet.spritesheet(dictSprites['Bard']) #ColorKey: Black
fftSpirteSheet.ColorKey = (255, 255, 255)
iCords = (4, 4)
myObjects.Player(fftSpirteSheet.images_at(fftWalkingLoop, dicScale['sprite'],  colorkey=fftSpirteSheet.ColorKey), iCords, "p1")

#todo Dear Jesus, please give cloud some arms
fftSpirteSheet = libSpriteSheet.spritesheet(dictSprites['Cloud']) #ColorKey: Black
fftSpirteSheet.ColorKey = (255, 255, 255)
iCords = (7,7)
myObjects.Player(fftSpirteSheet.images_at(fftWalkingLoop, dicScale['sprite'],  colorkey=fftSpirteSheet.ColorKey), iCords, "p2")

fftCursors = libSpriteSheet.spritesheet("res/fftCursor0(Green).png")
fftCursors.ColorKey = fftCursors.sheet.get_at((16,0))
myObjects.BattleCursor = fftCursors.image_at(pygame.Rect(0, 0, 64, 64), dicScale['sprite'], colorkey=fftCursors.ColorKey)

