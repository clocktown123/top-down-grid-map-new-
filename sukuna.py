import pygame

A = 0
D = 1
W = 2
S = 3
SPACE = 4
F = 5



Guy = pygame.image.load('GuySS2.png') #load your spritesheet
Guy.set_colorkey((255, 90, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)




#expansion = pygame.image.load('domain.png')


class Sukuna:
    def __init__ (self):

        #player variables
        self.xpos2 = 200
        self.ypos2 = 615
        self.vx2 = 0
        self.vy2 = 0
        self.frameWidth2 = 95
        self.frameHeight2 = 95
        self.RowNum2 = 0 #for left animation, this will need to change for other animations
        self.frameNum2 = 1
        self.ticker2 = 0
        self.direction2 = D

    def draw(self, screen):
        #pygame.draw.rect(screen, (255,0,255), (self.xpos, self.ypos, 30, 30))
        screen.blit(Guy, (self.xpos2-40, self.ypos2 -40), (self.frameWidth2*self.frameNum2, self.RowNum2*self.frameHeight2, self.frameWidth2, self.frameHeight2))

    #def domain(self, screen):
        #screen.blit(expansion, (0,0), (0,0, 10000, 10000))

    def move(self, keys2, map):
        #LEFT MOVEMENT
        if keys2[A] == True:
            self.vx2 = -3
            self.RowNum2 = 0
            self.direction2 = A
        #RIGHT MOVEMENT
        elif keys2[D] == True:
            self.vx2 = 3
            self.RowNum2 = 3
            self.direction2 = D
        #TURN OFF X VELOCITY
        else:
            self.vx2 = 0
        
        if keys2[W] == True:
            self.vy2 = -3
            self.RowNum2 = 1
            self.direction2 = W
        elif keys2[S] == True:
            self.vy2 = 3
            self.RowNum2 = 2
            self.direction2 = S
        else:
            self.vy2 = 0
        
        if self.vx2<0 or self.vx2>0 or self.vy2 <0 or self.vy2>0: #left animation
        # Ticker is a spedometer. We don't want Chicken animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
            self.ticker2+=1
        
        if self.ticker2%10==0: #only change frames every 10 ticks
          self.frameNum2+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 8 frames (0 through 7)
        if self.frameNum2>7: 
           self.frameNum2 = 0
        
        

        #COLLISION
        #LEFT
        if map [int((self.ypos2-10) / 50)][int((self.xpos2 - 10) / 50)] == 2:
            self.xpos2+=3
        #RIGHT
        if map [int((self.ypos2) / 50)][int((self.xpos2 +30 + 5) / 50)] == 2:
            self.xpos2-=3
        #DOWN
        if map [int((self.ypos2 + 30 + 5) / 50)][int((self.xpos2 ) / 50)] == 2:
            self.ypos2-=3
        #UP
        if map [int((self.ypos2 - 20) / 50)][int((self.xpos2) / 50)] == 2:
            self.ypos2+=3

        self.ypos2+=self.vy2
        self.xpos2+=self.vx2
