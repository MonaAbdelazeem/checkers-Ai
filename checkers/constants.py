import pygame

WIDTH, HEIGHT = 630, 630
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb

WHITE = (255, 255, 255)
WHITE2 = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
GREY2 = (109,109,109)
PURPLE =(117,51,145)

CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (44, 25))