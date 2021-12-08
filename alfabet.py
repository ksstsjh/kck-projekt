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

def main():
    run = True
    while run:

        screen.blit(Litera_A,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        pygame.display.update()



def menu():
    title_font = pygame.font.SysFont("calibri", 25, bold=True, italic=False)
    run = True
    while run:
        screen.blit(background, (0,0))
        title_label = title_font.render("Wcisnij lewy przycisk myszki aby rozpoczac", 1, (0,0,0))
        screen.blit(title_label, (width/2 - title_label.get_width()/2,350))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()


menu()

pygame.quit()




