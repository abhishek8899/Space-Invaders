from variables import *


def drawplayerinvaderbullet(player, invaders, frz, bullets, missiles):
    screen.blit(player, imagerect)
    for i in invaders:
        for invader in i:
            if invader in invaders[0]:
                screen.blit(alien, (invader.x, invader.y))
    for f in frz:
        if time.time() - f.t <= 5:
            screen.blit(freezed, (f.x, f.y))
        else:
            frz.remove(f)
    for b in bullets:
        screen.blit(bul, (b.x, b.y))
    for m in missiles:
        screen.blit(mis, (m.x, m.y))
