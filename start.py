"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import mapping
from globals import *


# starting point for the smaller grid, which is generated in the globals module.
big_Grid[9][9] = 1
TOP_LEFT = [0, 0]

# make a smaller grid that is the visible area
Grid = mapping.Gen_SmallGrid(big_Grid, TOP_LEFT)

# Initialize pygame
pygame.init()
pygame.key.set_repeat(100, 100)

# Set the HEIGHT and WIDTH of the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
Running = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Handle Events
def Events_UpdateGrid(fGrid):  # Note, this is big_Grid
    #GLOBALS
    global Running
    global TOP_LEFT
    #GLOBALS
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            Running = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Running = False
            # Move the grid up and down
            if event.key == pygame.K_DOWN:
                if mapping.GridOutOfBounds([TOP_LEFT[0]-1, TOP_LEFT[1]], "up"):
                    TOP_LEFT[0] -= 1
            elif event.key == pygame.K_UP:
                if mapping.GridOutOfBounds([TOP_LEFT[0]+1, TOP_LEFT[1]], "up"):
                    TOP_LEFT[0] += 1
            # move the grid left and right
            elif event.key == pygame.K_LEFT:
                if mapping.GridOutOfBounds([TOP_LEFT[0], TOP_LEFT[1]+1], "left"):
                    TOP_LEFT[1] += 1
            elif event.key == pygame.K_RIGHT:
                if mapping.GridOutOfBounds([TOP_LEFT[0], TOP_LEFT[1]-1], "left"):
                    TOP_LEFT[1] -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            fCol = pos[0] // (WIDTH + MARGIN)+TOP_LEFT[1]
            fRow = pos[1] // (HEIGHT + MARGIN)+TOP_LEFT[0]
            # Set that location to zero
            if fGrid[fRow][fCol] == 1:
                fGrid[fRow][fCol] = 0
                print("Turned Off", pos, "Grid coordinates: ", fRow, fCol)
            else:
                fGrid[fRow][fCol] = 1
                print("Turned On", pos, "Grid coordinates: ", fRow, fCol)
    return fGrid

# -------- Main Program Loop -----------
while Running:
    # Effect changes on big_Grid
    big_Grid = Events_UpdateGrid(big_Grid)
    # Reflect those changes on the small grid.
    Grid = mapping.Gen_SmallGrid(big_Grid, TOP_LEFT)

    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(g_HEIGHT):
        for column in range(g_WIDTH):
            color = WHITE
            if Grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
