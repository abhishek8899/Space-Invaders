import pygame
import time


bul = pygame.image.load("bul.jpg")
mis = pygame.image.load("bomb.jpg")
alien = pygame.image.load("alien.jpg")
freezed = pygame.image.load("freeze.jpg")
player = pygame.image.load("a.jpg")
global imagerect
imagerect = player.get_rect()
imagerect.center = (400, 700)
width = 800
height = 1000
screen = pygame.display.set_mode((width, height))

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
score = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MOVESPEED = 10
SHOOT = 1.2

tim = time.time()
tim1 = tim

invaders = [[]]
bullets = []
missiles = []
walls = []
frz = []
sc = []
