# Create the ant logic for the "ant" to walk around
import pygame
from antgrid import Grid

s_width = 1024
s_height = 768
screen = pygame.display.set_mode((s_width, s_height))

class Ant:
    def __init__(self, x, y, ant_w, ant_h, color):
        self.anttile_x = x
        self.anttile_y = y
        self.antwidth = ant_w
        self.antheight = ant_h
        self.color = color

    def make_ant(self):
        gridant = pygame.Rect(self.anttile_x, self.anttile_y, self.antwidth,self.antheight)
        #screen.blit(gridant, (self.anttile_x,self.anttile_y))

        return gridant
        
