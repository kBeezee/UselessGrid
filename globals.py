import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each cell
HEIGHT = 32
WIDTH = 32
# this sets how tall and long the visible screen is.
g_HEIGHT = 15
g_WIDTH = 25
# This sets how tall and long the 'map' is, including things that are not visible.
MAX_HEIGHT = 15
MAX_WIDTH = 25
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
Grid = []
big_Grid = []

# make a larger grid that represents the whole world - Has to be reversed upon creation, but accessing
# it should be done normally.
for row in range(MAX_WIDTH):
    big_Grid.append([])
    for column in range(MAX_HEIGHT):
        big_Grid[row].append(0)

WINDOW_SIZE = (500, 500) #[(WIDTH * g_WIDTH) + g_WIDTH, (HEIGHT * g_HEIGHT) + g_HEIGHT]

#Sprite Groups
AllSprites = pygame.sprite.Group()
CursorTiles = pygame.sprite.Group()
AllTiles = pygame.sprite.OrderedUpdates()

def write(msg="pygame is cool"):
    myfont = pygame.font.SysFont("None", 34, 128)
    mytext = myfont.render(msg, True, (0, 0, 0))
    mytext = mytext.convert_alpha()
    return mytext

#SpriteSheet Cords:
#OLD
#Link "res/zeldaLink.png"
#NoWeaponWalkingCordsList = [pygame.Rect(101, 127, 16, 24), pygame.Rect(124, 127, 16, 24), pygame.Rect(148, 127, 16, 24),
#                            pygame.Rect(171, 127, 16, 24), pygame.Rect(194, 128, 16, 24), pygame.Rect(218, 127, 16, 24),
#                            pygame.Rect(241, 127, 16, 24)]

#CURRENT
#Agrias
    #Body: "res/fftAgrias.png"  Ill also want to add the arms to make it more like the actual game, but this is good
    #for now.
fftWalkingLoop = [pygame.Rect(167, 3, 20, 34), pygame.Rect(199, 3, 20, 34), pygame.Rect(7, 44, 20, 34),
               pygame.Rect(39, 44, 20, 34), pygame.Rect(71, 44, 20, 34)]