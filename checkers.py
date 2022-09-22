from turtle import back
import numpy as np
import pygame, sys
import itertools

pygame.init()

WIDTH = 1000
HEIGHT = 1000
BOARD_ROWS = 8
BOARD_COLS = 8
SQUARE_SIZE = WIDTH//BOARD_ROWS

RED = pygame.Color('red')
GRAY = pygame.Color('gray')
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
BOARD_COLORS = itertools.cycle((WHITE, BLACK))

board = np.zeros((BOARD_ROWS, BOARD_COLS))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

gameOver = False
player = 1
def draw_board():

    for x in range(0, WIDTH, SQUARE_SIZE):
        for y in range(0, HEIGHT, SQUARE_SIZE):
            rect = (x, y, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(background, next(BOARD_COLORS), rect)
        next(BOARD_COLORS)

while True:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    pygame.display.flip()