import myObjects

#Note the tiles are being added to the group as they are being created. remember they are drawn in the order they are
#added b/c of OrderedUpdates(), fill it as things should be displayed.W

#todo procedurally generate landscape with algoritham hidden below. --This is done, but can be better
#it must add them as they should, and be all lined up neatly.
# the last two args will only change anything if their change is >= +/- 16.
def MakeMap0(tileset):
    for x in range(0, 160, 16):
        gridX = x / 16
        gridY = 0
        #these are our isometric "rows", going from the *top left* to the *right side* of the screen, our x.
        #as it repreats it creates the isometric "columns", going from the *top right* to the *left side* of the screen our y

        myObjects.Tiles(tileset, 96+x, 304-(x*2), gridX, gridY) #x y
        gridY += 1

        myObjects.Tiles(tileset, 112+x, 336-(x*2), gridX, gridY) #x y

        gridY += 1
        myObjects.Tiles(tileset, 128+x, 368-(x*2), gridX, gridY) #x y

        gridY += 1
        myObjects.Tiles(tileset, 144+x, 400-(x*2), gridX, gridY) #x y

        gridY += 1
        myObjects.Tiles(tileset,  160+x, 432-(x*2), gridX, gridY) #x y

        gridY += 1
        myObjects.Tiles(tileset,  176+x, 464-(x*2), gridX, gridY) #x y

        gridY += 1
        myObjects.Tiles(tileset,  192+x, 496-(x*2), gridX, gridY) #x y