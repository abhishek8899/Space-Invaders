import random
from classes import *


def makeinvaders(invaders):
    y = random.randint(0, 1)
    for i in invaders:
        x = random.randint(0, 7)
        invader = fire1(100 * x, 100 * y)
        i.append(invader)
    return invaders
