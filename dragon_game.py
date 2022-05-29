import random

import pygame  # to install use ---> pip install pygame

# initialize pygame
pygame.init()

# Assets Folder
Game_folder = 'd:/Code/PycharmProjects/feed_the_dragon/'
# Creating Game Window
window_Width = 1200
window_Height = 600
display_surface = pygame.display.set_mode((window_Width, window_Height))

# giving name to Game Window
pygame.display.set_caption('Feed the Dragon')

# Icon
game_icon = pygame.image.load(Game_folder + 'dragon_icon.png')
pygame.display.set_icon(game_icon)
# Loading up Background Image
background_image = pygame.transform.scale(pygame.image.load(Game_folder + 'dragon_night.jpg'),
                                          (window_Width, window_Height))

# Game Actors
dragon = pygame.image.load(Game_folder + 'dragon.png')
dragon_rect = dragon.get_rect()
dragon_rect.right = window_Width - 10
dragon_rect.centery = window_Height // 2
dragon_velocity = 6

# Loading all coin images in a List...
coins = []
for i in range(6):
    coins.append(pygame.transform.scale(pygame.image.load(Game_folder + 'coin/' + str(i) + '.png'), (32, 32)))
coin_index = 0
coin_rect = coins[coin_index].get_rect()
coin_rect.left = 0
coin_rect.top = 400
coin_velocity = 5

# Game Sounds
loss = pygame.mixer.Sound(Game_folder + 'loss.wav')
loss.set_volume(0.5)
pick = pygame.mixer.Sound(Game_folder + 'pickup.wav')
pick.set_volume(0.5)
background_music = pygame.mixer.music.load(Game_folder + 'background_music.mp3', )
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Game HUD
# Load the font and colors
big_game_font = pygame.font.Font(Game_folder + 'AttackGraffiti.ttf', 60)
small_game_font = pygame.font.Font(Game_folder + 'AttackGraffiti.ttf', 40)
GREEN = pygame.Color(0, 200, 0)
RED = pygame.Color(255, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# Render text using the font and color
title = big_game_font.render('Feed the Dragon', True, GREEN)
title_rect = title.get_rect()
title_rect.centerx = window_Width // 2
title_rect.top = 10

player_score = 0
player_lives = 3

# Score
score = small_game_font.render('Score: ' + str(player_score), True, WHITE)
score_rect = score.get_rect()
score_rect.left = 50
score_rect.top = 10

# Lives
lives = small_game_font.render('Lives : ' + str(player_lives), True, WHITE)
lives_rect = lives.get_rect()
lives_rect.right = window_Width - 50
lives_rect.top = 10

# Game Over
game_over_text = big_game_font.render('GAME OVER !', True, RED)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (window_Width // 2, window_Height // 2)

# Restart
game_restart_text = small_game_font.render('r : Restart', True, GREEN)
game_restart_text_rect = game_restart_text.get_rect()
game_restart_text_rect.center = (window_Width // 2, window_Height // 2 + 50)

# Quit
game_quit_text = small_game_font.render('q : Quit', True, GREEN)
game_quit_text_rect = game_quit_text.get_rect()
game_quit_text_rect.center = (window_Width // 2, window_Height // 2 + 100)

# main game LOOP (Life of Game)
game_status = 1
FPS = 60
clock = pygame.time.Clock()
running = True
# Loop
while running:
    # Listens to Events
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if game_status == 2:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_q:
                    running = False
                elif ev.key == pygame.K_r:
                    player_score = 0
                    player_lives = 3
                    pygame.mixer.music.play(-1)
                    coin_index = 0
                    coin_rect.left = 0
                    coin_rect.top = 400
                    coin_velocity = 5
                    dragon_rect.centery = window_Height // 2
                    score = small_game_font.render('Score : ' + str(player_score), True, WHITE)
                    lives = small_game_font.render('Lives : ' + str(player_lives), True, WHITE)
                    game_status = 1

    # apply background
    display_surface.blit(background_image, (0, 0))

    if game_status == 1:
        # Know which key is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dragon_rect.top > 100:
            dragon_rect.top -= dragon_velocity
        elif keys[pygame.K_DOWN] and dragon_rect.bottom < window_Height:
            dragon_rect.bottom += dragon_velocity
        elif keys[pygame.K_LEFT] and dragon_rect.left > 1000:
            dragon_rect.left -= 5
        elif keys[pygame.K_RIGHT] and dragon_rect.right <= 1200:
            dragon_rect.right += 5

        # update the coin Position
        coin_rect.right += coin_velocity

        # check for gain( dragon ate it )
        if coin_rect.colliderect(dragon_rect):
            pick.play()
            coin_velocity += 0.5
            coin_rect.left = -150
            coin_rect.top = random.randint(100, window_Height - coin_rect.height)
            player_score += 1
            score = small_game_font.render('Score : ' + str(player_score), True, WHITE)

        # check for loss
        if coin_rect.right > window_Width:
            loss.play()
            coin_rect.left = -150
            coin_rect.top = random.randint(100, window_Height - coin_rect.height)
            coin_velocity -= 0.5
            player_lives -= 1
            if player_lives > 1:
                lives = small_game_font.render('Lives :' + str(player_lives), True, WHITE)
            elif player_lives == 1:
                lives = small_game_font.render('Lives: ' + str(player_lives), True, RED)
            elif player_lives == 0:
                game_status = 2
                lives = small_game_font.render('Lives: ' + str(player_lives), True, RED)
                pygame.mixer.music.stop()
        # Draw the actors
        display_surface.blit(dragon, dragon_rect)
        display_surface.blit(coins[int(coin_index)], coin_rect)
        coin_index = (coin_index + 0.2) % 6

    elif game_status == 2:
        display_surface.blit(game_over_text, game_over_text_rect)
        display_surface.blit(game_restart_text, game_restart_text_rect)
        display_surface.blit(game_quit_text, game_quit_text_rect)

    # Draw the HUD
    display_surface.blit(title, title_rect)
    display_surface.blit(score, score_rect)
    display_surface.blit(lives, lives_rect)

    # Refresh the window
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
