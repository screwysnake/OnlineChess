import pygame

pygame.init()

class Board():
    def __init__(self, width, height):
        self.cell_width = width
        self.cell_height = height
    
    def draw_Board(self, win):
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = (255, 255, 255)
                else:
                    color = (128, 128, 128)
                cell_rect = (45 + col * self.cell_width, 45 + row * self.cell_height, self.cell_width, self.cell_height)
                pygame.draw.rect(win, color, cell_rect)
    