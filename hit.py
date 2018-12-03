from variables import *
from chkovrlp import *
from classes import *


def invaderdead(bullets, invaders, frz):
    for bullet in bullets:
        for row in invaders:
            for invader in row:
                if doRectsOverlap(bullet, invader):
                    row.remove(invader)
                    bullets.remove(bullet)
                    global score
                    score += 1
                    sc.append(score)
    for bullet in bullets:
        for f in frz:
            if doRectsOverlap(bullet, f):
                frz.remove(f)
                bullets.remove(bullet)
                score += 1
                sc.append(score)
    return invaders


def invaderfreeze(missiles, invaders):
    for missile in missiles:
        for row in invaders:
            for invader in row:
                if doRectsOverlap(missile, invader):
                    f = freeze(invader.x, invader.y, time.time())
                    frz.append(f)
                    # print "f",frz
                    row.remove(invader)
                    missiles.remove(missile)
    return invaders
