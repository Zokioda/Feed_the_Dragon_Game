import pygame  # to install use ---> pip install pygame

pygame.init()

Game_folder = 'd:/Code/PycharmProjects/feed_the_dragon/'
window_Width = 1000
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

# Game Characters
dragon = pygame.image.load(Game_folder + 'dragon.png')
dragon_x = window_Width - 80
dragon_y = 64
dragon_velocity = 10
# FPS = 60
# clock = pygame.time.Clock()
running = True
# Main Game Loop
while running:
    # Listens to Events
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    # Know which key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dragon_y > 64:
        dragon_y -= dragon_velocity
    elif keys[pygame.K_DOWN] and dragon_y < window_Height - 128:
        dragon_y += dragon_velocity
    elif keys[pygame.K_LEFT] and dragon_x > 800:
        dragon_x -= 5
    elif keys[pygame.K_RIGHT] and dragon_x < 900:
        dragon_x += 5

    # apply background
    display_surface.blit(background_image, (0, 0))
    display_surface.blit(dragon, (dragon_x, dragon_y))
    pygame.display.update()
    # clock.tick(FPS)

pygame.quit()
