import sys
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAME_RATE = 60

# Initializing Game, dependencies and Setting Window Size
pygame.init()
pygame.display.set_caption(title="Pysteroids ☄")  # Set the window title
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Create the Game area (surface)

# Setting mouse to Invisible
pygame.mouse.set_visible(False)

# Background
background_surf = pygame.image.load('./graphics/background.png').convert_alpha()
background_surf.fill((255, 255, 255, 180), None, pygame.BLEND_RGBA_MULT)

# Player sprites
# Ship Sprite
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rec = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# Laser beam Sprite
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_rec = laser_surf.get_rect()

# Text
font = pygame.font.Font('./graphics/subatomic.ttf', size=50)
text_surf = font.render('Space', True, (255, 255, 255))
text_rec = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

while True:
    # 1.Handle Input
    for event in pygame.event.get():
        # Handle Quiting the game.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                laser_rec.midbottom = ship_rec.midtop
                print('pew pew!')

    # Update the screen
    clock.tick(FRAME_RATE)  # Set FrameRate

    # Mouse Input
    ship_rec.center = pygame.mouse.get_pos()

    # Position Background sprites
    display_surface.fill((12, 2, 26))  # Fill the background color
    display_surface.blit(background_surf, (0, 0))  # Apply the Background Image

    # Position Text Sprite
    display_surface.blit(text_surf, text_rec)  # Set Text Position.

    # Position Laser sprites
    display_surface.blit(laser_surf, laser_rec)

    #  2.Update Ship Position
    # Prevent ship from going out of bounds
    if ship_rec.top < 0:
        ship_rec.top = 0
    elif ship_rec.bottom > WINDOW_HEIGHT:
        ship_rec.bottom = WINDOW_HEIGHT
    if ship_rec.left < 0:
        ship_rec.left = 0
    elif ship_rec.right > WINDOW_WIDTH:
        ship_rec.right = WINDOW_WIDTH

    display_surface.blit(ship_surf, ship_rec)

    laser_rec.bottom -= 10

    # Apply the changes (end of rendering)
    pygame.display.update()
