import sys
from random import randint, uniform

import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FRAMERATE = 120

score = 0


def laser_update(_laser_list: list, dt: float, speed=300):
    for _laser in _laser_list:
        _laser.y -= round(speed * dt)
        if _laser.bottom < 0:
            _laser_list.remove(_laser)


def meteor_update(_meteor_list, dt: float, speed=300):
    for _meteor, _direction in _meteor_list:
        _meteor.center += _direction * speed * dt
        if _meteor.top > WINDOW_WIDTH:
            meteor_list.remove((_meteor, _direction))


def display_score(ft: pygame.font.Font, kills: int):
    text_surf = ft.render(f'Score: {(pygame.time.get_ticks() // 1000) + kills}', True, (255, 255, 255))
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

#  Meteor
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)
meteor_surf = pygame.image.load('./graphics/meteor.png').convert_alpha()
meteor_list = []

# Import Sound
laser_sound = pygame.mixer.Sound('./sounds/laser.ogg')
explosion_sound = pygame.mixer.Sound('./sounds/explosion.wav')
background_music = pygame.mixer.Sound('./sounds/music.wav')
background_music.play(loops=-1)

while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_rec = laser_surf.get_rect(midbottom=ship_rec.midtop)
            laser_list.append(laser_rec)
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
            # Play Laser Sound
            laser_sound.play()
        if event.type == meteor_timer:
            x_pos = randint(-100, WINDOW_WIDTH + 100)
            y_pos = randint(-100, -50)
            meteor_rec = meteor_surf.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            meteor_list.append((meteor_rec, direction))

    # Framerate Limit
    delta_time = (clock.tick(FRAMERATE) / 1000)  # Set FrameRate

    # Mouse Input
    ship_rec.center = pygame.mouse.get_pos()

    # Update
    # for laser_rec in laser_list:
    laser_update(laser_list, delta_time)
    meteor_update(meteor_list, delta_time)
    can_shoot = laser_cooldown(can_shoot, shoot_time)

    #  Ship collision detection
    for meteor, _ in meteor_list:
        if ship_rec.colliderect(meteor):
            pygame.quit()
            sys.exit()

    for laser in laser_list:
        for meteor, _ in meteor_list:
            if laser.colliderect(meteor):
                laser_list.remove(laser)
                meteor_list.remove((meteor, _))
                explosion_sound.play()
                score += 10

    # Drawing
    display_surface.fill((12, 2, 26))  # Fill the background color
    display_surface.blit(background_surf, (0, 0))  # Apply the Background Image

    display_score(font, score)

    for rect in laser_list:
        display_surface.blit(laser_surf, rect)

    display_surface.blit(ship_surf, ship_rec)

    for rect, _ in meteor_list:
        display_surface.blit(meteor_surf, rect)

    # Draw the final Frame
    pygame.display.update()
