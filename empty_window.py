import sys
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAME_RATE = 120

#  Game init
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Create the Game area (surface)
pygame.display.set_caption(title="Pysteroids ☄")  # Set the window title
clock = pygame.time.Clock()

# Setting mouse to Invisible
pygame.mouse.set_visible(False)

# Ship Import
ship_surf = pygame.image.load('./graphics/ship.png').convert_alpha()
ship_rec = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# Background
background_surf = pygame.image.load('./graphics/background.png').convert_alpha()

# Laser import
laser_surf = pygame.image.load('./graphics/laser.png').convert_alpha()
laser_rec = laser_surf.get_rect(midbottom=ship_rec.midtop)

background_surf.fill((255, 255, 255, 180), None, pygame.BLEND_RGBA_MULT)

#  Import Text
font = pygame.font.Font('./graphics/subatomic.ttf', size=50)
text_surf = font.render('Space', True, (255, 255, 255))
text_rec = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         laser_rec.midbottom = ship_rec.midtop
        #         print('pew pew!')

    # Framerate Limit
    dt = (clock.tick(FRAME_RATE) / 1000)  # Set FrameRate

    # Mouse Input
    ship_rec.center = pygame.mouse.get_pos()

    # Update
    laser_rec.y -= 100 * dt
    print('delta time', dt)
    print(laser_rec.y)

    # Prevent ship from going out of bounds
    # if ship_rec.top < 0:
    #     ship_rec.top = 0
    # elif ship_rec.bottom > WINDOW_HEIGHT:
    #     ship_rec.bottom = WINDOW_HEIGHT
    # if ship_rec.left < 0:
    #     ship_rec.left = 0
    # elif ship_rec.right > WINDOW_WIDTH:
    #     ship_rec.right = WINDOW_WIDTH

    # Drawing
    display_surface.fill((12, 2, 26))  # Fill the background color
    display_surface.blit(background_surf, (0, 0))  # Apply the Background Image

    display_surface.blit(text_surf, text_rec)  # Set Text Position.
    pygame.draw.rect(display_surface, "white", text_rec.inflate((30, 30)), width=8, border_radius=5)

    display_surface.blit(laser_surf, laser_rec)
    display_surface.blit(ship_surf, ship_rec)

    # Draw the final Frame
    pygame.display.update()
