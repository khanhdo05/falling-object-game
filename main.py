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
object_size = WIDTH // 15
object_x = random.randint(0, WIDTH - object_size)
object_y = 0 # top of the screen
object_speed = 10

# Player's properties
player_size = WIDTH // 15
player_x = WIDTH // 2           # middle
player_y = HEIGHT - player_size # ground

# Other
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

# Main Game Loop
running = True
is_paused = False # Pause Flag

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_paused:
                    is_paused = False
                else:
                    is_paused = True
            elif event.key == pygame.K_LEFT:
                player_x -= player_size
            elif event.key == pygame.K_RIGHT:
                player_x += player_size
    
    # Update object's position
    if is_paused == False:
        object_y += object_speed
        if object_y >= HEIGHT:
            running = False
    
    # Collision Check
    if player_y < object_y + object_size and object_x < player_x + player_size and player_x < object_x + object_size:
        score += 1
        object_y = 0
        object_x = random.randint(0, WIDTH - object_size)      

    # Boundaries Check
    if player_x < 0:
        player_x = 0
    elif player_x + player_size > WIDTH - player_size:
        player_x = WIDTH - player_size

    
    # Drawing
    screen.fill(background_color)
    pygame.draw.rect(screen, object_color, (object_x, object_y, object_size, object_size))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Renew screen
    pygame.display.flip()

    # Frames per sec
    clock.tick(30)

# Exit game
pygame.quit()