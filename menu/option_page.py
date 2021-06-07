import pygame
import sys
sys.path.append('..')
from menu.boutton import *
class Option :
    
    def __init__(self, fenetre):

        self.niveauSons = 10

        
        self.bmoins = Button(text="-", left=310, top=100, width=50, height=50, picture=None, size = 0)
        self.bmoins.setBorderSize(8)
        self.moins = False
        self.bplus = Button(text="+", left=600, top=100, width=50, height=50, picture=None, size = 0)
        self.bplus.setBorderSize(8)
        self.plus = False


        self.image01 = pygame.image.load("menu/mountain.jpg").convert()
        self.image01 = pygame.transform.scale(self.image01, (1024,576))

        self.image02 = pygame.image.load("menu/scrollcartoon02.png")
        self.image02 = pygame.transform.scale(self.image02, (400,800))
        self.image02 = pygame.transform.rotate(self.image02,90)
        
        self.myfont01 = pygame.font.SysFont("Comic Sans MS", 60)
        self.label01 = self.myfont01.render("Options", 1, (0,0,0))

        self.myfont02 = pygame.font.SysFont("Comic Sans MS", 40)
        self.label02 = self.myfont02.render("Volume", 1, (0,0,0))

        self.myfont09 = pygame.font.SysFont("Arial", 20)
        self.label05 = self.myfont09.render("Utilisations du languages Python et de la bibliothèque Pygame.", 1, (0,0,0))

        self.label20 = self.myfont09.render("Giacinti Florian : Gestion du personnage et évènements du Jeu.", 1, (0,0,0))
        self.label21 = self.myfont09.render("Sauvat Valentin : Création des différents design de texture personnage et", 1, (0,0,0))
        self.label22 = self.myfont09.render("jaquette.", 1, (0,0,0))
        self.label23 = self.myfont09.render("Davidovski Léon : Création de niveau, des collisions animations de texture.", 1, (0,0,0))
        self.label24 = self.myfont09.render("Bessard Lucas : Création et dévelloppement de l'IHM du jeu.", 1, (0,0,0))
        self.label25 = self.myfont09.render("Pandraud Nicolas : Création de l'inventaire, gestion des items et création de", 1, (0,0,0))
        self.label26 = self.myfont09.render("la <<To do list>>.", 1, (0,0,0))
        self.label03 = self.myfont02.render("Credit !", 1, (0,0,0))
        

        #bouton pour le retour en arrière
        self.bmenu = Button(text="Retour", left=25, top=500, width=100, height=50, picture=None, size = 20)
        self.bmenu.setBorderSize(10)
        self.menu = False
        
    def changerSons(self, niveau):
        self.niveauSons = niveau
        
        
    def getSons(self):
        return self.niveauSons
    
    def update(self, fenetre):
        self.bmenu.update()
        self.bplus.update()
        self.bmoins.update()
        self.menu = self.bmenu.click()
        self.plus = self.bplus.click()
        self.moins = self.bmoins.click()
        

    def draw(self, fenetre):
        fenetre.blit(self.image01, (0,0))
        fenetre.blit(self.image02, (150,150))
        pygame.draw.rect(fenetre, (255,255,255), (155,100,525,50), 0)
        pygame.draw.rect(fenetre, (0,0,0), (365,100,9*self.niveauSons,50), 0)
        fenetre.blit(self.label01, (400, 0))
        fenetre.blit(self.label02, (175, 100))
        fenetre.blit(self.label03, (250, 160))
        self.bmenu.draw(fenetre)
        self.bplus.draw(fenetre)
        self.bmoins.draw(fenetre)
        fenetre.blit(self.label05, (225,250))
        fenetre.blit(self.label20, (225,300))
        fenetre.blit(self.label21, (225,325))
        fenetre.blit(self.label22, (375,350))
        fenetre.blit(self.label23, (225,375))
        fenetre.blit(self.label24, (225,400))
        fenetre.blit(self.label25, (225,425))
        fenetre.blit(self.label26, (397,450))
        
        
        
