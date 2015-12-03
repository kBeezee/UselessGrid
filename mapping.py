#Handle Mapping
from globals import *

def Gen_SmallGrid(fbig_Grid, fTOP_LEFT):
    # GLOBALS
    # Do Not use globals in seperate module, just update 1 variable at a time via return
    # GLOBALS

    # init empty small grid.
    fGrid = [[0 for col in range(g_WIDTH)] for row in range(g_HEIGHT)]

    for col in range(len(fGrid)):
        for row in range(len(fGrid[col])):
            #print "[%s][%s]. + %s" % (col, row, fTOP_LEFT)
            fGrid[col][row] = fbig_Grid[fTOP_LEFT[0]+row][fTOP_LEFT[1]+col]
    return fGrid

def GridOutOfBounds(fTOP_LEFT, fdir):
    # Move the grid up and down
    if fdir == "up":
        if fTOP_LEFT[0] >= 0 and fTOP_LEFT[0] <= MAX_HEIGHT - g_HEIGHT:
            return True
        else:
            print "Cant Move Minimap, u/d"
            return False

    # Move the grid left and right
    if fdir == "left":
        if fTOP_LEFT[1] >= 0 and fTOP_LEFT[1] <= MAX_WIDTH - g_WIDTH:
            return True
        else:
            print "Cant Move Minimap, l/r"
            return False


def PlayerOutOfBounds(fTOP_LEFT, fdir):
    # Move the grid up and down
    if fdir[1] != 0:
        if fTOP_LEFT[1] >= 0 and fTOP_LEFT[1] < MAX_HEIGHT:
            return True
        else:
            print "Cant Move Player u/d to: %s - MAX_HEIGHT: %s" % (fTOP_LEFT, MAX_HEIGHT)
            return False

    # Move the grid left and right
    if fdir[0] != 0:
        if fTOP_LEFT[0] >= 0 and fTOP_LEFT[0] < MAX_WIDTH:
            return True
        else:
            print "Cant Move Player l/r to: %s - MAX_WIDTH: %s " % (fTOP_LEFT, MAX_WIDTH)
            return False


def iso(cordPosX, cordPosY, OneOver4OfSpriteH, OneOver4OfSpriteW):
    #TODO use this for my program.
    a = round(cordPosX/OneOver4OfSpriteW - cordPosY/OneOver4OfSpriteH)
    b = round(cordPosX/OneOver4OfSpriteW + cordPosY/OneOver4OfSpriteH)
    x = (b - a)/2*OneOver4OfSpriteH
    y = (b + a)/2*OneOver4OfSpriteW
    return [x, y]


def CenterMiniMap():
    pass
