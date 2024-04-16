import pygame
import math


A = 0
D = 1
W = 2
S = 3
SPACE = 4
F = 5

slash = pygame.image.load('cleave.png')

class Cleave:
    def __init__(self):
        self.xpos = -10 # draw off scren when not in use
        self.ypos = -10
        self.isAlive = False
        self.direction = D

    def shoot(self, x, y, dir):
        self.xpos = x + 20 # start fireball at center of player
        self.ypos = y +20
        self.isAlive = True
        self.direction = dir

       

    def move(self, dir):
        if self.direction == D:
            self.xpos+=20
        elif self.direction == A:
            self.xpos-=20
        if self.direction == S:
            self.ypos+=20
        elif self.direction == W:
            self.ypos-=20
        
    def draw(self,screen):
        screen.blit(slash, (self.xpos, self.ypos) )
    
    def B_draw(self, screen):
        pygame.draw.circle(screen, (138,43,226), (self.xpos, self.ypos), 30)
        pygame.draw.circle(screen, (147,112,219), (self.xpos, self.ypos), 15)

    def collide(self, x, y):
        if math.sqrt((self.xpos - x) **2 + (self.ypos - y) **2) < 25:
            print("collision")
            return True
        else:
            return False
        
