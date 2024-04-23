import pygame
import random
import math

A = 0
D = 1
W = 2
S = 3

class Enemy:
    def __init__ (self):
        self.xpos = 400
        self.ypos = 200
        self.direction = D
        self.isAlive = True
    
    def die(self, ballx, bally):
        if math.sqrt((self.xpos-ballx)**2 + (self.ypos-bally)**2) <= 20:
            self.isAlive = False
    
    def draw(self, screen):
        if self.isAlive == True:
            pygame.draw.rect(screen, (20, 20, 40), ( self.xpos, self.ypos, 20, 20))

    def move(self, map, ticker, px, py):
        if ticker % 40 == 0: #change this number to make him change direction less or more often
            num = random.randrange(0, 4)
            if num == 0:
                self.direction = D
            elif num == 1:
                self.direction = A
            elif num == 2:
                self.direction = W
            elif num == 3:
                self.direction = S
        #check if the player is in the line of sight
        if abs(int(py/50) - int(self.ypos/50))<2: #check that player and enemy are in the same row
            if px < self.xpos: #check that player is to the left of the enemy
                self.xpos -=1
                self.direction = A
            else:
                self.xpos+=1
                self.direction = D
        if abs(int(px/50) - int(self.xpos/50))<2:
            if py < self.ypos: #check that player is to the left of the enemy
                self.ypos -=1
                self.direction = W
            else:
                self.ypos+=1
                self.direction = S
        
        if self.direction == D and map[int((self.ypos) / 50)][int((self.xpos + 20) / 50)] == 2:
            self.direction = W
            self.xpos -= 6
        if self.direction == A and map[int((self.ypos) / 50)][int((self.xpos - 20) / 50)] == 2:
            self.direction = S
            self.xpos += 6
        if self.direction == S and map[int((self.ypos + 20) / 50)][int((self.xpos) / 50)] == 2:
            self.direction = A
            self.ypos -= 6
        if self.direction == W and map[int((self.ypos - 20) / 50)][int((self.xpos) / 50)] == 2:
            self.direction = D
            self.ypos += 6

        if self.direction == D:
            self.xpos += 3
        elif self.direction == A:
            self.xpos -= 3
        elif self.direction == W:
            self.ypos -=3
        elif self.direction == S:
            self.ypos +=3
