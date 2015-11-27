#Handle Mapping
def Gen_SmallGrid(fbig_Grid, fTOP_LEFT):
    # GLOBALS
    # Do Not use globals in seperate module, just update 1 variable at a time via return
    # GLOBALS

    # init 10x10, empty grid.
    Grid = []
    for row in range(20):
        Grid.append([])
        for column in range(20):
            pass

    # fill that empty grid with what is in the big grid, based on the offset.
    for row in range(20):
        for column in range(20):
            Grid[row].append(fbig_Grid[fTOP_LEFT[0]+row][fTOP_LEFT[1]+column])
    # return the new grid to the calling function.
    return Grid
