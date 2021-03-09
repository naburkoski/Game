import os
import pygame
from Player import *
#from EnSemy import *

global currentDirection, dif
SCREENHEIGHT = 406
SCREENWIDTH = 500
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

pygame.init()

clock = pygame.time.Clock()
screencolor = (0, 0, 0)
screen = pygame.display.set_mode(SCREENSIZE)

startScrollPosX = (SCREENWIDTH / 2) - (84 / 2)

dif = 0


def redrawBackground():
    global dif

    backgroundWidth, backgroundHeight = background.get_rect().size
    stageWidth = backgroundWidth  
    stageHeight = backgroundHeight

    if player.x < startScrollPosX:
        if keys[pygame.K_LEFT] and dif > 0:
            player.x = startScrollPosX
            dif -= player.vel

        player.x = player.x

    elif player.x > startScrollPosX:
        if keys[pygame.K_RIGHT] and dif < 200:
            player.x = startScrollPosX
            dif += player.vel

    screen.blit(background, (0 - dif, 0))


def redrawWindowStageOne():
    global background
    background = pygame.image.load(f'{os.getcwd()}\\images\\Background.png').convert()

    redrawBackground()
    player.move(keys, SCREENWIDTH)
    player.redraw(screen)

    pygame.draw.rect(screen, (255, 255, 255), player.hitbox, 1)

    for attack in attacks:
        attack.update()

    pygame.display.update()


player = Character(50, 310, 70, 70)
attacks = []
platforms = []


running = True
while running:
    global keys
    keys = pygame.key.get_pressed()

    pygame.display.set_caption("Working title")
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if player.currentDirection == "Left":
        direction = -1
    else:
        direction = 1

    if keys[pygame.K_f]:
        if len(attacks) < 3:
            attacks.append(
                playerAttacks(round(player.x + player.width // 2), round(player.y + player.height // 2), 10, 10, direction, 15, 1))

    pygame.time.delay(50)

    redrawWindowStageOne()

pygame.quit()
