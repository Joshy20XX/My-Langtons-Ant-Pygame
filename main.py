# Langton's Ant Test
# Author: Joshua Ottey
# Prototype Date: April 20, 2025 @ 4:08PM EST
# Update Date: August 22, 2025 @ 1:26AM EST
#################################################

# We'd want to use Pygame to demo it
import pygame
from antgrid import Grid
from ant import Ant

def main():
    pygame.init()
    s_width = 1024
    s_height = 768
    screen = pygame.display.set_mode((s_width, s_height))
    clock = pygame.time.Clock()
    run = True
    caption = pygame.display.set_caption("Langton's Ant")
    ant_icon = pygame.image.load("langtonsant_screenshot_for_icon.png")
    pygame.display.set_icon(ant_icon)
    framecount = 0
    fps = 60

    #Defining Langton's Ant Grid and his ant (including tile width/height, rows/columns, ant width/height, ant position, direction, and speed)
    color = (255,255,255) #White grid
    antcolor = (255,0,0)
    tile_w = 7
    tile_h = 7
    n_rows = (s_height // tile_h)
    n_tiles = (s_width // tile_w) + 1
    grid_padding = 0
    ant_w = tile_w
    ant_h = tile_h
    ant_tilex = 80
    ant_tiley = 50
    direction = 0 #0: ant's right, 1: ant's up, 2: ant's down, 3: ant's left
    speed = 1 # speed must be greater than zero
    antgrid1 = Grid(tile_w, tile_h, n_rows, n_tiles, grid_padding, color)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        framecount += 1
        screen.fill('black')

        antx = (antgrid1.tile_x + antgrid1.padding) * ant_tilex
        anty = (antgrid1.tile_y + antgrid1.padding) * ant_tiley
        gridant1 = Ant(antx, anty, ant_w, ant_h, antcolor)
        ant = gridant1.make_ant()
        
        antgrid1.make_grid()
        pygame.draw.rect(screen, antcolor, ant)
    
        # If the ant goes off the grid, end the simulation
        if ant_tilex < 0 or ant_tilex > n_tiles - 1:
            break
        elif ant_tiley < 0 or ant_tiley > n_rows - 1:
            break

        if framecount % speed == 0:
            for i in range(n_tiles):
                for j in range(n_rows):
                    tile_rect = pygame.Rect((tile_w + grid_padding) * i, (tile_h + grid_padding) * j,tile_w,tile_h)
                    
                    if ant.colliderect(tile_rect) and antgrid1.antgrid[i][j] == 0:
                        direction += 1
    
                    if ant.colliderect(tile_rect) and antgrid1.antgrid[i][j] == 1:
                        direction -= 1

                        
            antgrid1.change_grid(ant)
            
            # Control the ant's movement based on its direction
            if direction == 0: #up
                ant_tiley -= 1
                    
            elif direction == 1: #right
                ant_tilex += 1
                    
            elif direction == 2: #down
                ant_tiley += 1
                    
            elif direction == 3: #left
                ant_tilex -= 1

            if direction > 3:
                direction = 0
                ant_tiley -= 1
                
            elif direction < 0:
                direction = 3
                ant_tilex -= 1
                
        
        pygame.display.flip()
        clock.tick(fps) #FPS = 60

main()
pygame.quit()
