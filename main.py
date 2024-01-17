# main.py

# Libraries Initialization
import pygame
import random
pygame.init()

# Game Window
WIDTH = 800
HEIGHT = 600
TITLE = "Falling Object Game"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Clock
clock = pygame.time.Clock()

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Drawing
    
    # Renew screen
    pygame.display.flip()

    # Frames per sec
    clock.tick(30)

# Exit game
pygame.quit()