import pygame, sys
import os, time
pygame.init()

pygame.display.set_caption("Alfabet")

fps = 60

width = 640
height = 480

screen = pygame.display.set_mode((width, height))

background = pygame.image.load('bg.png')

#grafiki liter
Litera_A = pygame.image.load('Letter_A.png')
Litera_B = pygame.image.load('Letter_B.png')
Litera_C = pygame.image.load('Letter_C.png')
Litera_D = pygame.image.load('Letter_D.png')
Litera_E = pygame.image.load('Letter_E.png')
Litera_F = pygame.image.load('Letter_F.png')
Litera_G = pygame.image.load('Letter_G.png')
Litera_H = pygame.image.load('Letter_H.png')
Litera_I = pygame.image.load('Letter_I.png')
Litera_J = pygame.image.load('Letter_J.png')
Litera_K = pygame.image.load('Letter_K.png')
Litera_L = pygame.image.load('Letter_L.png')
Litera_M = pygame.image.load('Letter_M.png')
Litera_N = pygame.image.load('Letter_N.png')
Litera_O = pygame.image.load('Letter_O.png')
Litera_P = pygame.image.load('Letter_P.png')
Litera_Q = pygame.image.load('Letter_Q.png')
Litera_R = pygame.image.load('Letter_R.png')
Litera_S = pygame.image.load('Letter_S.png')
Litera_T = pygame.image.load('Letter_T.png')
Litera_U = pygame.image.load('Letter_U.png')
Litera_W = pygame.image.load('Letter_W.png')
Litera_X = pygame.image.load('Letter_X.png')
Litera_Y = pygame.image.load('Letter_Y.png')
Litera_Z = pygame.image.load('Letter_Z.png')
litery=[Litera_A,Litera_B,Litera_C]
# litery w liście
litery = []
litery.append(Litera_A)
litery.append(Litera_B)
litery.append(Litera_C)
litery.append(Litera_D)
litery.append(Litera_E)
litery.append(Litera_F)
litery.append(Litera_G)
litery.append(Litera_H)
litery.append(Litera_I)
litery.append(Litera_J)
litery.append(Litera_K)
litery.append(Litera_L)
litery.append(Litera_M)
litery.append(Litera_N)
litery.append(Litera_O)
litery.append(Litera_P)
litery.append(Litera_R)
litery.append(Litera_S)
litery.append(Litera_T)
litery.append(Litera_U)
litery.append(Litera_W)
litery.append(Litera_X)
litery.append(Litera_Y)
litery.append(Litera_Z)
#ilosc liter
liczba_liter = len(litery)
# wyswietlana litera
wyswietlana_litera = 0
#  mainloop
while True:
    with open("moje_dane.txt", "a") as myfile:

        myfile.write("start\n")

    czas=pygame.time.get_ticks()/1000
    print(czas)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if czas>1:
        wyswietlana_litera = (wyswietlana_litera + 1) % liczba_liter
        time.sleep(1)
    # wyswietlanie
    screen.fill((255,255,255)) 
    screen.blit(litery[wyswietlana_litera], (width/2 - Litera_A.get_width()/2, 100))
    pygame.display.flip()

