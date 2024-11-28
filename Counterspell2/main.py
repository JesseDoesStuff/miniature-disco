import pygame
import sys
from pygame.locals import *

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960

# Setup for pygame + making screen for 960 width and 960 height
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Roadblocks")
running = True


bg_img = pygame.transform.scale(pygame.image.load('img/base.png'), (960, 960))
g_img = pygame.image.load('img/ground.png')
c_img = pygame.image.load('img/cone.png')

conesX = [1, 1, 2, 4, 5, 6, 6, 7, 7, 8, 9, 10, 10, 12, 14, 15, 17, 18, 20, 21, 21, 22, 24, 24, 25, 26, 28, 30, 31, 31, 32]
conesY = [5, 6, 2, 3, 28, 12, 13, 13, 14, 21, 21, 16, 28, 30, 31, 23, 12, 6, 2, 9, 19, 25, 20, 27, 14, 15, 12, 5, 6, 8, 12]

def drawMap():
    row = 0
    while row < 32:
        col = 0
        while col < 32:
            screen.blit(g_img, (col * 30, row * 30))
            col += 1
        row += 1

    i = 0  
    while i < len(conesY):
        screen.blit(c_img, (conesX[i] * 30, conesY[i] * 30))
        i += 1
    



while running: 

    # DON'T TAKE THIS OUT THEN WE CANT EXIT GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    drawMap()

    

    # Keep the screen updating so that it's not just one picture the whole time
    pygame.display.update()

pygame.quit()
