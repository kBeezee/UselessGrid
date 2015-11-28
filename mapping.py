#Handle Mapping
from globals import *
def Gen_SmallGrid(fbig_Grid, fTOP_LEFT):
    # GLOBALS
    # Do Not use globals in seperate module, just update 1 variable at a time via return
    # GLOBALS

    # init 10x10, empty grid.
    Grid = []
    for row in range(g_HEIGHT):
        Grid.append([])
        for column in range(g_WIDTH):
            pass

    # fill that empty grid with what is in the big grid, based on the offset.
    for row in range(g_HEIGHT):
        for column in range(g_WIDTH):
            Grid[row].append(fbig_Grid[fTOP_LEFT[0]+row][fTOP_LEFT[1]+column])
    # return the new grid to the calling function.
    return Grid


def GridOutOfBounds(fTOP_LEFT, dir):
    # Move the grid up and down
    if dir == "up":
        if fTOP_LEFT[0] >= 0 and fTOP_LEFT[0] <= MAX_HEIGHT - g_HEIGHT:
            return True
        else:
            print "Cant Move, u/d"
            return False

    # Move the grid left and right
    if dir == "left":
        if fTOP_LEFT[1] >= 0 and fTOP_LEFT[1] <= MAX_WIDTH - g_WIDTH:
            return True
        else:
            print "Cant Move, l/r"
            return False



