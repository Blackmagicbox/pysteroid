import sys
import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAMERATE = 120


def laser_update(ll: list, dt: float, speed=300):
    for laser in ll:
        laser.y -= round(speed * dt)
        if laser.bottom < 0:
            ll.remove(laser)


def display_score(ft: pygame.font.Font):
    text_surf = ft.render(f'Space: {pygame.time.get_ticks() // 1000}', True, (255, 255, 255))
    text_rec = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rec)
    pygame.draw.rect(display_surface, "white", text_rec.inflate((30, 30)), width=8, border_radius=5)


def laser_cooldown(cs: bool, st: int, duration=500) -> bool:
    if not cs:
        ct = pygame.time.get_ticks()
        if ct - st >= duration:
            cs = True

    return cs


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
laser_list = []

# Laser cooldown timer
can_shoot = True
shoot_time = None

background_surf.fill((255, 255, 255, 180), None, pygame.BLEND_RGBA_MULT)

#  Import Text
font = pygame.font.Font('./graphics/subatomic.ttf', size=50)

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_rec = laser_surf.get_rect(midbottom=ship_rec.midtop)
            laser_list.append(laser_rec)
            # print('pew pew!')
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

    # Framerate Limit
    delta_time = (clock.tick(FRAMERATE) / 1000)  # Set FrameRate

    # Mouse Input
    ship_rec.center = pygame.mouse.get_pos()

    # Update
    # for laser_rec in laser_list:
    laser_update(laser_list, delta_time)
    can_shoot = laser_cooldown(can_shoot, shoot_time)

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

    display_score(font)

    for rect in laser_list:
        display_surface.blit(laser_surf, rect)

    display_surface.blit(ship_surf, ship_rec)

    # Draw the final Frame
    pygame.display.update()
