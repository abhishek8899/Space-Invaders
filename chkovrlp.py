def doRectsOverlap(bullet, invader):
    if (bullet.x >= invader.x) and (bullet.x <= invader.x + 100):
        if (bullet.y >= invader.y) and (bullet.y <= invader.y + 100):
            return True
        else:
            return False
    else:
        return False
