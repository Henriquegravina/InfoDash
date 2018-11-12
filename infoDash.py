## Painel de instrumentos em Phyton e pygame
## henrique @ gravina com br
## Licença GPL3



import random, sys, time, pygame, math
from pygame.locals import *

WINDOWWIDTH = 320
WINDOWHEIGHT = 240

#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = (  0, 155,   0)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (155, 155,   0)
DARKGRAY     = ( 40,  40,  40)
bgColor = BLACK
FPS = 1000

DadoA = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
DadoB = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
DadoC = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
DadoD = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    #DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),pygame.FULLSCREEN)
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('deep')
    pygame.mouse.set_visible(False)
    
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    #infoSurf = BASICFONT.render('Basic DEEP data loger', 1, WHITE)
    #infoRect = infoSurf.get_rect()
    #infoRect.topleft = (10, WINDOWHEIGHT - 25)

    
#    BGIMAGE = pygame.image.load('escala3.png')
#    BGIMAGE = pygame.transform.smoothscale(BGIMAGE, (106,106))
    
    DISPLAYSURF.fill(bgColor)
    waitingForInput = False
    cc = 0
    a = 0
    b = 50
    c = 100
    d = 150
    while True: # main game loop
        
        a = a + 1
        if a >= 256:
           a=0
       
        b = b + 1
        if b >= 256:
           b=0
       
        c = c + 1
        if c >= 256:
           c=0
       
        d = d + 1
        if d >= 256:
           d = 0
       
       
        cc = cc + 1
        if a >= 2:
            DadoA.pop(0)
            DadoA.append(a)
    
            DadoB.pop(0)
            DadoB.append(b)
        
            DadoC.pop(0)
            DadoC.append(c)
    
            DadoD.pop(0)  
            DadoD.append(d)
            
            cc = 0
    
    
    
        clickedButton = None # button that was clicked (set to YELLOW, RED, GREEN, or BLUE)
        DISPLAYSURF.fill(bgColor)
        #DISPLAYSURF.blit(BGIMAGE, (0,23))
        #DISPLAYSURF.blit(BGIMAGE, (106,23))

        grau1 =  DadoA[200]
        x_gauge1 = 53
        y_gauge1 = 75
        comp1 = 40
        #DISPLAYSURF.blit(BGIMAGE, (0,23)) # ESCALA
        radiano1 = ( 3.1415 * (225 - grau1) ) / 180;
        pygame.draw.line(DISPLAYSURF, BRIGHTBLUE, (x_gauge1,y_gauge1), (x_gauge1+comp1*math.cos(radiano1), y_gauge1+comp1*-(math.sin(radiano1))), 2)        
        pygame.draw.line(DISPLAYSURF, BRIGHTBLUE, (x_gauge1-1,y_gauge1-1), (x_gauge1+comp1*math.cos(radiano1), y_gauge1+comp1*-(math.sin(radiano1))), 1)
        pygame.draw.line(DISPLAYSURF, BRIGHTBLUE, (x_gauge1-2,y_gauge1-2), (x_gauge1+comp1*math.cos(radiano1), y_gauge1+comp1*-(math.sin(radiano1))), 1)
        
        LabelDadoA = BASICFONT.render(str(DadoA[200]), 1, WHITE)
        LabelDadoARect = LabelDadoA.get_rect()
        LabelDadoARect.topleft = (x_gauge1, y_gauge1+15)
        DISPLAYSURF.blit(LabelDadoA, LabelDadoARect)


        grau2 = DadoB[200]
        x_gauge2 = 53*3
        y_gauge2 = 75
        comp2 = 40
        #DISPLAYSURF.blit(BGIMAGE, (53*2,23)) # ESCALA
        radiano2 = ( 3.1415 * (225 - grau2) ) / 180;
        pygame.draw.line(DISPLAYSURF, BRIGHTRED, (x_gauge2,y_gauge2), (x_gauge2+comp2*math.cos(radiano2), y_gauge2+comp2*-(math.sin(radiano2))), 2)
        pygame.draw.line(DISPLAYSURF, BRIGHTRED, (x_gauge2-1,y_gauge2-1), (x_gauge2+comp2*math.cos(radiano2), y_gauge2+comp2*-(math.sin(radiano2))), 1)
        pygame.draw.line(DISPLAYSURF, BRIGHTRED, (x_gauge2-2,y_gauge2-2), (x_gauge2+comp2*math.cos(radiano2), y_gauge2+comp2*-(math.sin(radiano2))), 1)
        
        LabelDadoB = BASICFONT.render(str(DadoB[200]), 1, WHITE)
        LabelDadoBRect = LabelDadoB.get_rect()
        LabelDadoBRect.topleft = (x_gauge2, y_gauge2+15)
        DISPLAYSURF.blit(LabelDadoB, LabelDadoBRect)
        
        grau3 = DadoC[200]
        x_gauge3 = 53*5
        y_gauge3 = 75
        comp3 = 40
        #DISPLAYSURF.blit(BGIMAGE, (53*4,23)) # ESCALA
        radiano3 = ( 3.1415 * (225 - grau3) ) / 180;
        pygame.draw.line(DISPLAYSURF, BRIGHTYELLOW, (x_gauge3,y_gauge3), (x_gauge3+comp3*math.cos(radiano3), y_gauge3+comp3*-(math.sin(radiano3))), 2)
        pygame.draw.line(DISPLAYSURF, BRIGHTYELLOW, (x_gauge3-1,y_gauge3-1), (x_gauge3+comp3*math.cos(radiano3), y_gauge3+comp3*-(math.sin(radiano3))), 1)
        pygame.draw.line(DISPLAYSURF, BRIGHTYELLOW, (x_gauge3-2,y_gauge3-2), (x_gauge3+comp3*math.cos(radiano3), y_gauge3+comp3*-(math.sin(radiano3))), 1)
        
        LabelDadoC = BASICFONT.render(str(DadoC[200]), 1, WHITE)
        LabelDadoCRect = LabelDadoC.get_rect()
        LabelDadoCRect.topleft = (x_gauge3, y_gauge3+15)
        DISPLAYSURF.blit(LabelDadoC, LabelDadoCRect)
        
        grau4 = DadoD[200]
        x_gauge4 = 53
        y_gauge4 = 185
        comp4 = 40
        #DISPLAYSURF.blit(BGIMAGE, (0,23+110)) # ESCALA
        radiano4 = ( 3.1415 * (225 - grau4) ) / 180;
        pygame.draw.line(DISPLAYSURF, WHITE, (x_gauge4,y_gauge4), (x_gauge4+comp4*math.cos(radiano4), y_gauge4+comp4*-(math.sin(radiano4))), 2)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_gauge4-1,y_gauge4-1), (x_gauge4+comp4*math.cos(radiano4), y_gauge4+comp4*-(math.sin(radiano4))), 2)
        pygame.draw.line(DISPLAYSURF, WHITE, (x_gauge4-2,y_gauge4-2), (x_gauge4+comp4*math.cos(radiano4), y_gauge4+comp4*-(math.sin(radiano4))), 2)
        
        LabelDadoD = BASICFONT.render(str(DadoD[200]), 1, WHITE)
        LabelDadoDRect = LabelDadoD.get_rect()
        LabelDadoDRect.topleft = (x_gauge4, y_gauge4+15)
        DISPLAYSURF.blit(LabelDadoD, LabelDadoDRect)
        
        

        #DISPLAYSURF.blit(infoSurf, infoRect)
        
        
        POSGRAPHX=110
        POSGRAPHY=120
        GRAPHSIZEX=200
        GRAPHSIZEY=110
        
        
        LINEAI = regulariza(DadoA[0],0,255,0,GRAPHSIZEY-1)
        for indice in range(0,200): 
            LINEAF = regulariza(DadoA[indice],0,255,0,GRAPHSIZEY-1)
            pygame.draw.line(DISPLAYSURF, BRIGHTBLUE, (POSGRAPHX+1+indice-1,POSGRAPHY-1+GRAPHSIZEY-LINEAI), (POSGRAPHX+1+indice,POSGRAPHY-1+GRAPHSIZEY-LINEAF) , 2)
            LINEAI = regulariza(DadoA[indice],0,255,0,GRAPHSIZEY-1)

        LINEAI = regulariza(DadoB[0],0,255,0,GRAPHSIZEY-1)
        for indice in range(0,200): 
            LINEAF = regulariza(DadoB[indice],0,255,0,GRAPHSIZEY-1)
            pygame.draw.line(DISPLAYSURF, BRIGHTRED, (POSGRAPHX+1+indice-1,POSGRAPHY-1+GRAPHSIZEY-LINEAI), (POSGRAPHX+1+indice,POSGRAPHY-1+GRAPHSIZEY-LINEAF) , 2)
            LINEAI = regulariza(DadoB[indice],0,255,0,GRAPHSIZEY-1)
            
        LINEAI = regulariza(DadoC[0],0,255,0,GRAPHSIZEY-1)
        for indice in range(0,200): 
            LINEAF = regulariza(DadoC[indice],0,255,0,GRAPHSIZEY-1)
            pygame.draw.line(DISPLAYSURF, BRIGHTYELLOW, (POSGRAPHX+1+indice-1,POSGRAPHY-1+GRAPHSIZEY-LINEAI), (POSGRAPHX+1+indice,POSGRAPHY-1+GRAPHSIZEY-LINEAF) , 2)
            LINEAI = regulariza(DadoC[indice],0,255,0,GRAPHSIZEY-1)
            
        LINEAI = regulariza(DadoD[0],0,255,0,GRAPHSIZEY-1)
        for indice in range(0,200): 
            LINEAF = regulariza(DadoD[indice],0,255,0,GRAPHSIZEY-1)
            pygame.draw.line(DISPLAYSURF, WHITE, (POSGRAPHX+1+indice-1,POSGRAPHY-1+GRAPHSIZEY-LINEAI), (POSGRAPHX+1+indice,POSGRAPHY-1+GRAPHSIZEY-LINEAF) , 2)
            LINEAI = regulariza(DadoD[indice],0,255,0,GRAPHSIZEY-1)

        
        pygame.draw.rect(DISPLAYSURF, WHITE, (POSGRAPHX,POSGRAPHY,GRAPHSIZEX,GRAPHSIZEY), 2)

        
        
        
        checkForQuit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()
    
def regulariza(x,in_min,in_max,out_min,out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
