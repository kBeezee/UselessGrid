import myObjects

#Note the tiles are being added to the group as they are being created. remember they are drawn in the order they are
#added b/c of OrderedUpdates(), fill it as things should be displayed.W

#todo procedurally generate landscape with algoritham hidden below. --This is done, but can be better
#it must add them as they should, and be all lined up neatly.
# the last two args will only change anything if their change is >= +/- 16.
def MakeMap0(tileset):
    for y in range(0, 10):
        for x in range(0, 10):
            myObjects.Tiles(tileset, y, x)
