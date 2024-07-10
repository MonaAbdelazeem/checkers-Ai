from .constants import PURPLE, WHITE2, SQUARE_SIZE, WHITE, CROWN
import pygame

class Piece:
    PADDING = 15          #size of circle piece
    OUTLINE = 2           #outline of circle 

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0         
        self.y = 0         
        self.calc_pos()    # of piece in its sqr

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):                 # to drow the circle of piece
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, WHITE2, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:                    # put the crown on piece
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)