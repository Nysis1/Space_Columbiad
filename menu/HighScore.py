import pygame
import sys
sys.path.append('..')
from menu.boutton import *

class HighScore :

    def score(self, fenetre):
        with open("menu/score.txt", "r") as f:
            tabint = []

            txt = f.read()
            txt = txt.split(' ')
            txt = txt[:-1]
            i = 0
            while i < len(txt):
                txt[i] = txt[i].split('_')
                i += 1

            # Sort players by score
            tabint = sorted(txt, key=lambda x: int(x[1]), reverse=True)

            i = 0
            for it in tabint:
                    if (i == 0):
                        label = self.myfont2.render("1er    : " + it[0], 1, (0,0,0))
                    else:
                        label = self.myfont2.render(str(i+1) + "ème : " + it[0], 1, (0,0,0))
                    fenetre.blit(label, (300, (180 + i*25)))

                    label = self.myfont2.render("score : " + it[1], 1, (0,0,0))
                    fenetre.blit(label, (530, (180 + i*25)))
                    i = i + 1

            f.close()

    def __init__(self, fenetre):

        # Color background
        self.menu =False

        # Back button
        self.b = Button(text="Retour", left=25, top=500, width=100, height=50, picture=None, size = 20)
        self.b.setBorderSize(10)

        self.image = pygame.image.load("menu/mountain.jpg").convert()
        self.image = pygame.transform.scale(self.image, (1024,576))

        # Hightscore
        self.image2 = pygame.image.load("menu/parchemin.png")
        self.image2 = pygame.transform.scale(self.image2, (700,450))
        self.myfont = pygame.font.SysFont("Arial", 60)
        self.label = self.myfont.render(" HighScore", 1, (255,255,255), 6)

        self.myfont2 = pygame.font.SysFont("Comic Sans MS", 20)


    def update(self):
        self.b.update()
        self.menu = self.b.click()

    def draw(self, fenetre): 
        fenetre.blit(self.image, (0,0))
        fenetre.blit(self.image2, (170,100))
        fenetre.blit(self.label, (400, 50))
        self.score(fenetre)
        self.b.draw(fenetre)
