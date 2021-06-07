import pygame
import sys
sys.path.append('..')
from model.InventaireClass import Item
class Event:
    def __init__(self,nom,text,score,item=None,img=None,freeze=True,son=None):
        self.nom = nom
        self.font = pygame.font.Font(None,25)
        self.text=text
        self.score = score
        self.check = False
        self.item = item
        if img:
            self.img = pygame.image.load(img)
            self.img = pygame.transform.scale(self.img,(64,64))
        else:
            self.img = None
        if son:
            self.son = pygame.mixer.Sound(son)
        else:
            self.son = None
        self.freeze = freeze
    def checked(self):
        return self.check

    def setCheck(self,etat):
        self.check = etat
    def getItem(self):
        return self.item.getName()
    def strike(self, fenetre, text, pos):
        text_width, text_height = self.font.size(text)
        pygame.draw.lines(fenetre, (0,0,0), False, [(795,pos*35+50), (text_width+795,pos*35+50)], 3)

    def draw(self, fenetre, pos):
        if self.checked():
            self.strike(fenetre, self.nom, pos)
        text = self.font.render(self.nom, 1, (0,0,0))
        fenetre.blit(text,(795,pos*35+41))
