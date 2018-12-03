from variables import *
from classes import *


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
