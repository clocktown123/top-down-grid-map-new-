import pygame
from player import player
from limitless import fireball
from sukuna import Sukuna
from cleave import Cleave
from enemy import Enemy
pygame.init()
pygame.display.set_caption("top down grid map game")
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
#gameover = False




A = 0
D = 1
W = 2
S = 3
SPACE = 4
F = 5
keys2 = [False, False, False, False, False, False]

p1 = player()
p2 = Sukuna()
ball = fireball()
cleave = Cleave()
e1 = Enemy()

counter = 0

#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False
button2 = False
button3 = False

mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

ticker = 0

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,2,0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,2],
       [2,0,2,0,0,0,2,2,0,0,0,0,2,0,0,0,0,0,0,2],
       [2,0,2,0,0,0,2,2,0,0,0,0,2,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,1,1,1,1,1,1,1,3,3,3,3,3,1,1,1,1,1,1,2]]

brick = pygame.image.load('brick.png')
dirt = pygame.image.load('dirt.png')
lava = pygame.image.load('lava.png')

text_font = pygame.font.SysFont("Sans", 30, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

while 1: #GAME LOOP######################################################
    clock.tick(60) # fps
    ticker+=1
    #input section--------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                keys2[SPACE] = True
                counter += 1
            if event.key == pygame.K_f:
                keys2[F] = True
             
            
            if event.key == pygame.K_a:
                keys2[A] = True
                #RowNum = 0
            if event.key == pygame.K_d:
                keys2[D] = True
                #RowNum = 3
            if event.key == pygame.K_w:
                keys2[W] = True
                #RowNum = 1
            if event.key == pygame.K_s:
                keys2[S] = True
                #RowNum = 2
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                keys2[SPACE] = False
            if event.key == pygame.K_f:
                keys2[F] = False

            if event.key == pygame.K_a:
                keys2[A] = False
                #RowNum = 0
            if event.key == pygame.K_d:
                keys2[D] = False
                #RowNum = 3
            if event.key == pygame.K_w:
                keys2[W] = False
                #RowNum = 1
            if event.key == pygame.K_s:
                keys2[S] = False
                #RowNum = 2
            
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input (more needed for actual game)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                quitGame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                quitGame = False
    #physics section-------------------------------------------------------

    if counter > 10:
        counter = 0

    p1.move(keys2 , map)
    p2.move(keys2, map)

    ball.move(p1.direction)
    cleave.move(p2.direction2)


    if state == 2:
        e1.move(map, ticker, p1.xpos, p1.ypos)
    if state == 3:
        e1.move(map, ticker, p2.xpos2, p2.ypos2)
           
    if keys2[SPACE] == True:
        ball.shoot(p1.xpos, p1.ypos, p1.direction)

    if keys2[SPACE] == True:
        cleave.shoot(p2.xpos2, p2.ypos2, p2.direction2)

     #ANIMATION-------------------------------------------------------------------
    
    if state == 1 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False
    
    if state == 1 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<550:
        button2 = True
    else:
        button2 = False
    
    if state == 1 and mousePos[0]>700 and mousePos[0]<900 and mousePos[1]>400 and mousePos[1]<550:
        button3 = True
    else:
        button3 = False

    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    if state == 1 and button2 == True and mouseDown == True:
        state = 3
    if state == 1 and button3 == True and mouseDown == True:
        state = 4
   
    #render section-----------------------------------------------------------

    if state == 1:
        screen.fill((230,100,100))# Clear the screen pink

        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (100, 400, 200, 150))
        if button2 == False:
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (400, 400, 200, 150))
        if button3 == False:
            pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (700, 400, 200, 150))

        draw_text("The Honored", text_font, (0,0,0), 110, 440)
        draw_text("One", text_font, (0,0,0), 170, 500)
    
        draw_text("The Fallen", text_font, (0,0,0), 430, 440)
        draw_text("One", text_font, (0,0,0), 470, 500)

    if state == 2 or state == 3 or state == 4:
        screen.fill((128,128,128))

        e1.draw(screen)

        #draw map
        for i in range(20):
            for j in range(20):
                if map[i][j] == 1:
                    screen.blit(dirt, (j*50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 2:
                    screen.blit(brick, (j *50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 3:
                    screen.blit(lava, (j *50, i * 50), (0, 0, 50, 50))
        if state == 2:
            if keys2[F] == True:
                p1.domain(screen)

            if ball.isAlive == True and counter < 10:
                ball.draw(screen)
            else:
                ball.B_draw(screen)
        
        elif state == 3:
            if cleave.isAlive == True:
                cleave.draw(screen)

        pygame.draw.rect(screen, (0, 0, 0), (790, 50, 160, 100), 5)  # width = 3
        if counter == 1:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 16, 90))
        elif counter == 2:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 32, 90))
        elif counter == 3:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 48, 90))
        elif counter == 4:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 64, 90))
        elif counter == 5:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 80, 90))
        elif counter == 6:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 96, 90))
        elif counter == 7:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 112, 90))
        elif counter == 8:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 128, 90))
        elif counter == 9:
            pygame.draw.rect(screen, (58, 156, 156), (795, 55, 150, 90))


        if state == 2:
            p1.draw(screen)
        if state == 3:
            p2.draw(screen)
        #elif state == 3:
            
    
    pygame.display.flip()#this actually puts the pixel on the screen


#end game loop#############################################################################
pygame.quit()
