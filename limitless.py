import pygame
import math
import random

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = 4
W = 5

class fireball:
    def __init__(self):
        self.xpos = -10 # draw off scren when not in use
        self.ypos = -10
        self.isAlive = False
        self.direction = RIGHT

    def shoot(self, x, y, dir):
        self.xpos = x + 20 # start fireball at center of player
        self.ypos = y +20
        self.isAlive = True
        self.direction = dir

       

    def move(self, dir):
        if self.direction == RIGHT:
            self.xpos+=20
        elif self.direction == LEFT:
            self.xpos-=20
        if self.direction == DOWN:
            self.ypos+=20
        elif self.direction == UP:
            self.ypos-=20
        
    def draw(self,screen):
        self.rando = random.randrange(0, 2)
        self.redAlive = False
        self.blueAlive = False
        if self.rando == 0:
            self.redAlive = True
        else:
            self.blueAlive = True
        if self.redAlive:
            pygame.draw.circle(screen, (220,20,60), (self.xpos, self.ypos), 10)
            pygame.draw.circle(screen, (250,0,0), (self.xpos, self.ypos), 5)
        if self.blueAlive:
            pygame.draw.circle(screen, (0,0,225), (self.xpos, self.ypos), 10)
            pygame.draw.circle(screen, (65,105,255), (self.xpos, self.ypos), 5)
    
    def B_draw(self, screen):
        pygame.draw.circle(screen, (138,43,226), (self.xpos, self.ypos), 30)
        pygame.draw.circle(screen, (147,112,219), (self.xpos, self.ypos), 15)

    def collide(self, x, y):
        if math.sqrt((self.xpos - x) **2 + (self.ypos - y) **2) < 25:
            print("collision")
            return True
        else:
            return False
        
