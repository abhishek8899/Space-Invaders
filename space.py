import pygame
import sys
import time
from pygame.locals import *
from invaders import *
from chkovrlp import *
from hit import *
from construct import *
from variables import *


pygame.init()
pygame.font.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('SPACESHIP')
myfont = pygame.font.SysFont("monospace", 100)
invaders = makeinvaders(invaders)


def movepaddle(player):
    global imagerect
    if moveLeft and imagerect.center[0] > 50:
        lst = list(imagerect.center)
        lst[0] -= MOVESPEED
        imagerect.center = tuple(lst)
    # print imagerect.center,width
    if moveRight and imagerect.center[0] < width - 50:
        lst = list(imagerect.center)
        lst[0] += MOVESPEED
        imagerect.center = tuple(lst)
    return player


def movebullets(bullets, missiles):
    for bullet in bullets:
        bullet.y -= SHOOT
        if bullet.y < -100:
            bullets.remove(bullet)
    for missile in missiles:
        missile.y -= 2 * SHOOT
        if missile.y < -100:
            missiles.remove(missile)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_SPACE:
                bullet = fire1(
                    imagerect.center[0] - 10, imagerect.center[1] - 132)
                bullets.append(bullet)
            if event.key == ord('s'):
                missile = fire2(
                    imagerect.center[0] - 4, imagerect.center[1] - 132)
                missiles.append(missile)
        if event.type == KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False

    if time.time() - tim1 > 8:
        for row in invaders:
            for invader in row:
                row.remove(invader)
        tim1 = time.time()

    if time.time() - tim > 10:
        makeinvaders(invaders)
        tim = time.time()
        tim1 = tim

    screen.fill(BLACK)
    drawplayerinvaderbullet(player, invaders, frz, bullets, missiles)
    movebullets(bullets, missiles)
    invaders = invaderdead(bullets, invaders, frz)
    invaderfreeze(missiles, invaders)
    player = movepaddle(player)
    if(sc == []):
        scoretext = myfont.render("Score 0", False, (255, 25, 25))
    else:
        scoretext = myfont.render(
            "Score {0}".format(sc[-1]), False, (255, 25, 25))

    screen.blit(scoretext, (200, 850))
    pygame.display.update()

    mainClock.tick(60)
