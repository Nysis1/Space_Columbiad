import pygame
import sys
sys.path.append('..')
from menu.boutton import *

class Menu : 

    def __init__(self, fenetre):

        #color background
        self.image = pygame.image.load("menu/ImageMenu.png")
        self.image01 = pygame.image.load("menu/Zorgs_Redemption.png")
        self.image01 = pygame.transform.scale(self.image01, (800, 200))

        #creation d'un bouton pour l'option ou il y aura le credit/niveau de sons
        self.bOption = Button(text="Options", left=20, top=450, width=175, height=75, picture=None, size = 40)
        self.bOption.setBorderSize(10)
        self.options =False
        #creation d'un bouton pour quitter
        self.bquit = Button(text="Quitter", left=825, top=450, width=175, height=75, picture=None, size = 40)
        self.bquit.setBorderSize(10)
        self.quit =False
        #creation du bouton pour jouer
        self.bjouer = Button(text="Jouer", left=370, top=210, width=300, height=150, picture=None, size = 35)
        self.bjouer.setBorderSize(10)
        self.jouer =False
        #bouton pour highscore
        self.bhightscore = Button(text="HighScore", left=550, top=450, width=175, height=75, picture=None, size = 40)
        self.bhightscore.setBorderSize(10)
        self.hightscore =False
        #boutton pour comment jouer
        self.bregle = Button(text="Règles", left=285, top=450, width=175, height=75, picture=None, size = 40)
        self.bregle.setBorderSize(10)
        self.regle =False

        
        
    def update(self):
        self.bOption.update()
        self.bquit.update()
        self.bjouer.update()
        self.bhightscore.update()
        self.bregle.update()
        self.options =self.bOption.click()
        self.quit =self.bquit.click()
        self.jouer =self.bjouer.click()
        self.hightscore =self.bhightscore.click()
        self.regle =self.bregle.click()
        

    def draw(self, fenetre):
        fenetre.blit(self.image, (0,0))
        fenetre.blit(self.image01, (125, -5))
        self.bOption.draw(fenetre)
        self.bquit.draw(fenetre)
        self.bjouer.draw(fenetre)
        self.bhightscore.draw(fenetre)
        self.bregle.draw(fenetre)
        

