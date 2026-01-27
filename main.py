# Langton's Ant Test
# Author: Joshua Ottey
# Prototype Date: April 20, 2025 @ 4:08PM EST
# Update: January 27, 2026 @ 12:23AM EST
#################################################

# UPDATE 1/27/2026: Colliderect checks are removed. The direction and color change within the tile map itself for a smoother simulation.
# It feels faster and it no longer stutters. The grid padding has been reconfigured and the Ant class is removed for now.
import pygame
from antgrid import Grid

def main():
    pygame.init()

    #Play with these parameters
    tile_size = 10 #in pixels
    n_rows = 60 #The number of tiled rows down (+y axis)
    n_tiles = 80 #The number of tiles across (+x axis)
    slowness = 1 #How fast it goes. Smaller value is faster while larger value is slower.
    ant_x = 30 #Ant's position X in the tile map array
    ant_y = 30 #Ant's position Y in the tile map array
    clock = pygame.time.Clock()
    run = True
    caption = pygame.display.set_caption("Langton's Ant")
    ant_icon = pygame.image.load("langtonsant_screenshot_for_icon.png")
    pygame.display.set_icon(ant_icon)
    framecount = 0
    fps = 60

    #Defining Langton's Ant Grid and his ant (including tile width/height, rows/columns, ant width/height, ant position, direction, and speed)
    color = (255,255,255) #White grid

    grid_padding = 0 #Set how far apart grid tiles are. Default = 0 (no spacing)

    #A not so great fix for padding issue but it'll do for now
    if grid_padding > 0:
        s_width = (tile_size + 1) * n_tiles
        s_height = (tile_size + 1) * n_rows
        screen = pygame.display.set_mode((s_width, s_height))
    else:
        s_width = (tile_size) * n_tiles
        s_height = (tile_size) * n_rows
        screen = pygame.display.set_mode((s_width, s_height))

    direction = 1 #0: ant's right, 1: ant's up, 2: ant's down, 3: ant's left
    antgrid1 = Grid(tile_size, tile_size, n_rows, n_tiles, grid_padding, color)
    antgrid1.make_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill('black')
        framecount += 1
        ant = antgrid1.antgrid[ant_x][ant_y] #Actually define our ant for the movement check below

        #Add and subtract our direction total based on if the tile index is 0 or 1
        if framecount % slowness == 0:
            if ant == 0:
                antgrid1.antgrid[ant_x][ant_y] = 1
                direction += 1

            if ant == 1:
                antgrid1.antgrid[ant_x][ant_y] = 0
                direction -= 1

            #Move the ant based on its direction
            if direction == 0: #up
                ant_y -= 1
            elif direction == 1: #right
                ant_x += 1
            elif direction == 2: #down
                ant_y += 1
            elif direction == 3: #left
                ant_x -= 1

            #This loops the ant's direction
            if direction > 3:
                direction = 0
                ant_y -= 1
            elif direction < 0:
                direction = 3
                ant_x -= 1

        antgrid1.draw_grid() #Draw the current state of the tilemap
        #print(f"Ant X: {ant_x}, Ant Y: {ant_y}, Direction {direction}") #Uncomment to see debugging

        pygame.display.flip()
        clock.tick(fps) #Frames per second = 60
main()
pygame.quit()
