# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

#ive added some code to change how its return and this is where scaling takes place as well.

import pygame
from globals import *
dicScale = {'sprite': (32, 32), 'tile': (64, 64)}

class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, scale=None, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        if scale is None:
            scale = (scale[0], scale[1])

        return pygame.transform.scale(image, scale)

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, scale=None, colorkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, scale, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, scale=None, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
