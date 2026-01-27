import pygame

s_width = 1024
s_height = 768
screen = pygame.display.set_mode((s_width, s_height))

class Grid:
    def __init__(self, tile_x, tile_y, n_rows, n_tiles, padding, color):
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.n_rows = n_rows
        self.n_tiles = n_tiles
        self.color = color
        self.padding = padding
        self.antgrid = []

    def return_grid_info(self):
        return "# Rows: {}, # Tiles: {}, Grid Color: {}".format(self.n_rows, self.n_tiles, self.color)

    def make_grid(self):
        # Assemble the grid with the given properties       
        for i in range(self.n_tiles):
            tile_row = []

            for j in range(self.n_rows):
                gridtile = 0 
                tile_row.append(gridtile)
            self.antgrid.append(tile_row)
        
        
    def draw_grid(self):
        #Draw grid (number of tiles across and rows down (+x, +y).
        for i in range(self.n_tiles):
            for j in range(self.n_rows):
                
                tile_rect = pygame.Rect(i * (self.tile_x + self.padding), j * (self.tile_y + self.padding),self.tile_x,self.tile_y)
                        
                if self.antgrid[i][j] == 1:
                    pygame.draw.rect(screen, (0,0,0), tile_rect)
                elif self.antgrid[i][j] == 0:
                    pygame.draw.rect(screen, (255,255,255), tile_rect)
          

    
                
