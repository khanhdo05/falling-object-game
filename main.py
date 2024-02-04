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

# Background Image
welcome_image = pygame.image.load('graphics/welcome.png')
background_image = pygame.image.load('graphics/background.png')
game_over_background = pygame.image.load('graphics/game_over_background.png')
game_over_screen = pygame.image.load('graphics/game_over_screen.png')

# Heart Image
heart_img = pygame.image.load('graphics/heart.png')
heart_img = pygame.transform.scale(heart_img, (80, 80))
heart_big_img = pygame.transform.scale(heart_img, (130, 130))

# Falling object's properties
object_img = pygame.image.load('graphics/object.png')
object_size = WIDTH // 10
object_img = pygame.transform.scale(object_img, (object_size, object_size))
object_x = random.randint(0, WIDTH - object_size)
object_y = 0 # top of the screen
object_speed = 15

# Player's properties
player_img = pygame.image.load('graphics/player.png')
player_size = WIDTH // 10
player_img = pygame.transform.scale(player_img, (player_size, player_size))
player_x = WIDTH // 2           # middle
player_y = HEIGHT - player_size - 166 # ground

# Music
pygame.mixer.music.load('audio/background_music.mp3')
lose_sound = pygame.mixer.Sound('audio/lose.mp3')
# Other
clock = pygame.time.Clock()
score = 0
heart = 3

# Font
game_over_font = pygame.font.Font('font/Pixelify_Sans/static/PixelifySans-Bold.ttf', 200)
pixel_font = pygame.font.Font('font/VT323/VT323-Regular.ttf', 220)
pixel_small_font = pygame.font.Font('font/VT323/VT323-Regular.ttf', 170)
pixel_smaller_font = pygame.font.Font('font/VT323/VT323-Regular.ttf', 90)
regular_font = pygame.font.Font('font/Roboto/Roboto-Medium.ttf', 100)

# Welcome Screen
welcome = True
while welcome:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            welcome = False
    screen.blit(welcome_image, (0, 0))
   
    pygame.display.flip()
    clock.tick(30)

# Instruction Screen
instruction = True
while instruction:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            instruction = False
    screen.fill((0, 0, 0))
    ins_text = regular_font.render("Got the rules?", True, (255, 255, 255))
    screen.blit(ins_text, (WIDTH // 2, HEIGHT // 2))
   
    pygame.display.flip()
    clock.tick(30)
            
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
        if object_y >= HEIGHT - player_size:
            heart -= 1
            object_y = 0
            object_x = random.randint(0, WIDTH - object_size)  
            object_speed += 3
    
    # Collision Check
    if player_y + 166 < object_y + object_size and object_x < player_x + player_size and player_x < object_x + object_size:
        score += 1
        object_y = 0
        object_x = random.randint(0, WIDTH - object_size)  
        object_speed += 1

    # Boundaries Check
    if player_x < 0:
        player_x = 0
    elif player_x + player_size > WIDTH - player_size:
        player_x = WIDTH - player_size

    # Text
    if is_paused == False:
        screen.blit(heart_img, (WIDTH - 200, 55))
        text = regular_font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(text, (70, 30))
        heart_count = regular_font.render(":"+ str(heart), True, (0, 0, 0))
        screen.blit(heart_count, (WIDTH - 115, 38))
    else:
        text_paused = regular_font.render("Paused. Press Space to Resume!", True, (0, 0, 0))
        screen.blit(text_paused, (WIDTH // 2 - (WIDTH // 3), HEIGHT // 2))

    # Lose!
    if heart == 0:
        running = False

    # Drawing
    screen.blit(object_img, (object_x, object_y))
    screen.blit(player_img, (player_x, player_y))

    # Renew screen
    pygame.display.flip()

    # Frames per sec
    clock.tick(30)

# Game Over Screen
game_over = True
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            game_over = False
    screen.blit(game_over_screen, (0, 0))
    over_text = game_over_font.render("GAME OVER", True, (251, 194, 7))
    screen.blit(over_text, (WIDTH // 2 - 500, HEIGHT // 2 - 200))
   
    pygame.display.flip()
    clock.tick(30)

# Hehe Screen
game_over_text = pixel_font.render("______________", True, (252, 43, 113))
press_to_quit = pixel_font.render("_________?", True, (252, 43, 113))
dear = pixel_small_font.render("TO:____", True, (251, 194, 7))
happy = pixel_smaller_font.render("I KNOW, THIS IS PRETTY LIT, RIGHT?", True, (251, 194, 7))
score_final = pixel_smaller_font.render("X" + str(score), True, (252, 43, 113))
screen.blit(game_over_background, (0, 0))
screen.blit(game_over_text, (WIDTH // 2 - 600, HEIGHT // 2 - 200))
screen.blit(press_to_quit, (WIDTH // 2 - 420, HEIGHT // 2))
screen.blit(dear, (WIDTH // 2 - 240, 130))
screen.blit(happy, (WIDTH // 2 - 600, HEIGHT - 220))
screen.blit(score_final, (350, 180))
screen.blit(heart_big_img, (200, 160))
screen.blit(player_img, (1200, 145))
pygame.display.flip()

# Wait a minute!
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False

# Quit game
pygame.quit()
exit()
