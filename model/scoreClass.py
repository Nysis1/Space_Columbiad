import pygame
import sys
sys.path.append('..')

class score:
    """Classe permettant la gestion du score"""
    def __init__(self):
        self.score = 0
        self.backImg = pygame.image.load('data/Sprites/score_bg.png')
        self.font =pygame.font.Font(None, 50);
    def addScore(self,nb):
        self.score += nb

    def draw(self,fenetre):
        fenetre.blit(pygame.transform.scale(self.backImg, (280, 60)), [2, 2])
        esp = "     "
        if self.score<10:
            esp="            "
        elif self.score<100:
            esp="          "
        elif self.score<1000:
            esp="        "
        elif self.score<10000:
            esp="      "
        text = self.font.render("Score : "+esp+str(self.score), 1, (255,255,255))
        fenetre.blit(text,(10,15))
        
