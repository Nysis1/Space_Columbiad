import pygame
import boutton
import sys
sys.path.append('..')

class Tuto :

    def __init__(self, fenetre):
        self.image01 = pygame.image.load("menu/mountain.jpg").convert()
        self.image01 = pygame.transform.scale(self.image01, (1024,576))

        #------------------------------------
        self.image02 = pygame.image.load("menu/regle_fond.png")
        #------------------------------------

        self.bmenu = boutton.Button(text="Retour", left=25, top=500, width=100, height=50, picture=None, size = 20)
        self.bmenu.setBorderSize(10)
        self.menu = False

    def update(self):
        # self.bmenu.update()
        self.menu = self.bmenu.click()

    def draw(self, fenetre):
        fenetre.blit(self.image01, (0,0))
        '''fenetre.blit(self.image02, (75,50))
        fenetre.blit(self.label01, (345, 70))'''
        #------------------------------------
        fenetre.blit(self.image02, (0,0))

        #------------------------------------

        self.bmenu.draw(fenetre)
