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

# Color palette
background_color = (252, 227, 252) # Light Pink
object_color = (69, 143, 247)      # Blue
player_color = (209, 27, 115)      # Hot Pink

# Falling object's properties
object_size = 20
object_x = random.randint(0, WIDTH - object_size)
object_y = 0 # top of the screen
object_speed = 10

# Player's properties
player_size = 20
player_x = WIDTH // 2           # middle
player_y = HEIGHT - player_size # ground

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
    screen.fill(background_color)
    pygame.display.flip()

    # Frames per sec
    clock.tick(30)

# Exit game
pygame.quit()