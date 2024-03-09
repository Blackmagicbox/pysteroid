import sys
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

pygame.init()

exit_the_game = False
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(title="Pysteroids ☄")

# Importing images
background_surf = pygame.image.load('./graphics/background.png').convert_alpha()
background_surf.fill((255, 255, 255, 180), None, pygame.BLEND_RGBA_MULT)
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()

# Importing text
font = pygame.font.Font('./graphics/subatomic.ttf', size=50)
text_surf = font.render('Space', True, (255, 255, 255))

while True:
    # Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the screen
    display_surface.fill((12, 2, 26))
    display_surface.blit(background_surf, (0, 0))
    display_surface.blit(text_surf, (500, 200))
    display_surface.blit(ship_surf, (300, 500))

    # Apply the changes (end of rendering)
    pygame.display.update()
