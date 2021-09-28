import sys
import pygame
import random

from pygame import mixer

pygame.font.init() 

pygame.init()

# Loading the music file
mixer.music.load("media/boom.wav")


def check_events(screen, ship, bitcoin,settings):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                # Move ship right.
                ship.right(settings)

            elif event.key == pygame.K_LEFT:
                # Move ship left.
                ship.left(settings)

            elif event.key == pygame.K_q:
                # Move ship up.
                ship.up(settings)

            elif event.key == pygame.K_a:
                # Move ship down.
                ship.down(settings)

            # ANY OTHER KEY OPTIONS GO HERE
            elif event.key == pygame.K_SPACE and bitcoin.mining == 100:
                # Move ship down.
                bitcoin.mining = 0
                bitcoin.fire = True
                bitcoin.choosen = False

def update_screen(ai_settings, screen, starship, bitcoin, roadster_group ,roadsters):
    """Update sprites & messages on the screen.""" 

    if bitcoin.fire and bitcoin.display:

        # Calling certain function according to bitcoijn type
        if bitcoin.super:
            bitcoin.Super_fire_bitcoin(ai_settings)
        else:
            bitcoin.fire_bitcoin(ai_settings)


    elif bitcoin.fire:

        # This is tell when a certain type of bitcoin will be generated 
        if random.randint(0,2):
            bitcoin.super = True
        else :
            bitcoin.super = False

        # Calling certain function according to bitcoijn type
        if bitcoin.super:
            bitcoin.Super_fire_firsttime(starship.rect.x, starship.rect.y)
        else:
            bitcoin.fire_firsttime(starship.rect.x, starship.rect.y)


    for i in range(0,ai_settings.aliens):
        roadsters[i].rect.x -= roadsters[i].speed
        if roadsters[i].rect.x <= 0:
            roadsters[i].rect.x = ai_settings.screen_width
            roadsters[i].rect.y = random.randint(0,ai_settings.screen_height)


    # setting collide conditions between straship and roadster
    starship_collision = pygame.sprite.spritecollide(starship, roadster_group, True)

    if starship_collision:
        starship.damage += 10
        starship_collision = 0
        mixer.music.play()


    # setting collide conditions between bitcoin and roadster
    bitcoin_collision = pygame.sprite.spritecollide(bitcoin, roadster_group, True)

    if bitcoin_collision:
        ai_settings.score += 10
        mixer.music.play()
        if bitcoin.super :
            bitcoin.Super_on_collision()
        else: 
            bitcoin.on_collision()

    pygame.display.update()


        