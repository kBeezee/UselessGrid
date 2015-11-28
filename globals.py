# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each cell
WIDTH = 20
HEIGHT = 20
# this sets how tall and long the visible screen is.
g_HEIGHT = 20
g_WIDTH = 40

MAX_HEIGHT = 50
MAX_WIDTH = 50
# This sets the margin between each cell
MARGIN = 1
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
Grid = []
big_Grid = []

# make a larger grid that represents the whole world
for row in range(MAX_HEIGHT):
    big_Grid.append([])
    for column in range(MAX_WIDTH):
        big_Grid[row].append(0)

WINDOW_SIZE = [(WIDTH * g_WIDTH) + (MARGIN * g_WIDTH) + MARGIN, (HEIGHT * g_HEIGHT) + (MARGIN * g_HEIGHT) + MARGIN]

