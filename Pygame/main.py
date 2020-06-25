import pygame
import random
import math
from pygame import mixer
pygame.init()
img = "vr-gaming.png"
bg = pygame.image.load("background.png")
bullet = pygame.image.load("bullet.png")
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")
icon = pygame.image.load(img)
pygame.display.set_icon(icon)
spaceship = pygame.image.load("spaceship.png")
enemy = pygame.image.load("alien.png")
font = pygame.font.Font('freesansbold.ttf', 32)
enemyx = []
enemyy = []
spacex, spacey = 250, 530
bulletx, bullety = 265, 525
movespace = 0
moveenemy_x = []
moveenemy_y = []
movebullet_y = 5
bullet_state = "ready"
score = 0
num_of_enemies = 4
mixer.music.load('background.wav')
mixer.music.play(-1)
game = True
for i in range(0, num_of_enemies):
    # enemy[i] = pygame.image.load("alien.png")
    enemyx.append(random.randint(0, 536))
    enemyy.append(random.randint(0, 300))
    moveenemy_x.append(3)
    moveenemy_y.append(15)


def displayspaceship(x, y):
    screen.blit(spaceship, (x, y))


def displayenemy(x, y):
    screen.blit(enemy, (x, y))


def bullet_ready(x, y):
    screen.blit(bullet, (x, y))
    global bullet_state
    bullet_state = "fire"


def collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(bulletx-enemyx, 2)) +
                         (math.pow(bullety-enemyy, 2)))
    # print("distance" + str(distance))
    if(distance < 29):
        return True
    else:
        return False


def show_score(value):
    score = font.render("Score :0" + str(value), True, (255, 255, 255))
    screen.blit(score, (10, 1))


def does_gameend():
    f = 0
    for i in range(num_of_enemies):
        if(enemyy[i] >= 450):
            f = 1
            for i in range(num_of_enemies):
                enemyy[i] = enemyy[i]+1000
            font2 = pygame.font.Font('freesansbold.ttf', 64)
            gameover = font2.render("Game Over", True, (255, 255, 255))
            screen.blit(gameover, (155, 150))
            # print("here")
            global game
            game = False
            break


run = True

while run:
    # screen.fill((255, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movespace = -4
            if event.key == pygame.K_RIGHT:
                movespace = +4
            if event.key == pygame.K_SPACE:
                if(bullet_state == "ready"):
                    bulletx = spacex+18
                    bullet_ready(bulletx, bullety)
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movespace = 0

    if(bullety <= 0):
        bullety = 525
        bullet_state = "ready"

    if(bullet_state == "fire"):
        bullety -= movebullet_y
        bullet_ready(bulletx, bullety)

        #
    if(spacex+movespace < 536 and spacex+movespace > 0):
        spacex = spacex+movespace
    displayspaceship(spacex, spacey)
    if(game == True):
        for i in range(0, num_of_enemies):

            if(enemyx[i]+moveenemy_x[i] < 536 and enemyx[i]+moveenemy_x[i] > 0):
                enemyx[i] = enemyx[i]+moveenemy_x[i]
            else:
                moveenemy_x[i] = -(moveenemy_x[i])
                moveenemy_y[i] = +moveenemy_y[i]
                enemyy[i] = enemyy[i]+moveenemy_y[i]
            point = collision(enemyx[i], enemyy[i], bulletx, bullety)
            if point == True:

                enemy_sound = mixer.Sound('explosion.wav')
                enemy_sound.play()
                bullety = 525
                bullet_state = "ready"
                # bullet_ready(bulletx, bullety)
                score += 1
                print(score)
                enemyx[i] = random.randint(0, 536)
                enemyy[i] = random.randint(0, 300)
                #moveenemy_x[i]= +moveenemy_x[i]
            displayenemy(enemyx[i], enemyy[i])
    does_gameend()
    # print(game)
    show_score(score)

    pygame.display.update()
