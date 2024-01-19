# main.py

# Libraries Initialization
import pygame
import random
from sys import exit
pygame.init()

# Game Window
WIDTH = 800 * 2
HEIGHT = 600 * 2
TITLE = "Catch Me If You Can"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Color palette
background_color = (252, 227, 252) # Light Pink
object_color = (69, 143, 247)      # Blue
player_color = (209, 27, 115)      # Hot Pink

background_image = pygame.image.load('graphics/background.png')

# Falling object's properties
object_size = WIDTH // 15
object_x = random.randint(0, WIDTH - object_size)
object_y = 0 # top of the screen
object_speed = 20

# Player's properties
player_size = WIDTH // 15
player_x = WIDTH // 2           # middle
player_y = HEIGHT - player_size - 166 # ground

# Other
clock = pygame.time.Clock()
score = 0
pixel_font = pygame.font.Font('font/VT323/VT323-Regular.ttf', 200)
regular_font = pygame.font.Font('font/Roboto/Roboto-Medium.ttf', 100)

# Main Game Loop

running = True
is_paused = False # Pause Flag

while running:

    for event in pygame.event.get():
        # Quit action
        if event.type == pygame.QUIT:
            running = False
        # Game logic when pressed keys
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
            elif event.key == pygame.K_ESCAPE:
                running = False
    
    # Draws a new screen
    screen.blit(background_image, (0, 0))

    # Update object's position
    if is_paused == False:
        object_y += object_speed
        if object_y >= HEIGHT - player_size - 166:
            running = False
    
    # Collision Check
    if player_y + 166 < object_y + object_size and object_x < player_x + player_size and player_x < object_x + object_size:
        score += 1
        object_y = 0
        object_x = random.randint(0, WIDTH - object_size)      

    # Boundaries Check
    if player_x < 0:
        player_x = 0
    elif player_x + player_size > WIDTH - player_size:
        player_x = WIDTH - player_size

    # Text
    if is_paused == False:
        text = regular_font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(text, (70, 70))
    else:
        text_paused = regular_font.render("Paused. Press Space to Resume!", True, (0, 0, 0))
        screen.blit(text_paused, (WIDTH // 2 - (WIDTH // 3), HEIGHT // 2))

    # Drawing
    pygame.draw.rect(screen, object_color, (object_x, object_y, object_size, object_size))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Renew screen
    pygame.display.flip()

    # Frames per sec
    clock.tick(30)

# Game Over Screen
game_over_color = (15, 20, 31) # Dark Blue
screen.fill(game_over_color)
game_over_text = pixel_font.render("XXXXXXXXXXXXX", True, (252, 43, 113))
press_to_quit = pixel_font.render("XXXXXXXXXX", True, (252, 43, 113))
screen.blit(game_over_text, (WIDTH // 2 - 550, HEIGHT // 2 - 200))
screen.blit(press_to_quit, (WIDTH // 2 - 400, HEIGHT // 2))
pygame.display.flip()

# Wait a minute!
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            waiting = False

# Quit game
pygame.quit()
exit()