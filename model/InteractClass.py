import pygame
import sys
sys.path.append('..')
from model.EventClass import Event
from model.boutonClass import Button

def getNbEvt(events):
    nb =0
    for en in events:
        nb += 1 if not en.checked() else 0

class Interact:
    def __init__(self,nom,imgPath,events,x,y):
        self.nom=nom
        self.img = pygame.image.load(imgPath)
        self.img = pygame.transform.scale(self.img,(64,64))
        self.backImg = pygame.image.load('data/Sprites/bgInt.png')
        self.events = events
        self.x = x*64
        self.y = y*64
        self.font =pygame.font.Font(None, 50);
        self.font2 =pygame.font.Font(None, 25);
        self.buttons = []
        nbEv = getNbEvt(self.events)
        nbcour = 0
        for ev in events:
            self.buttons.append(Button(ev.text,52+328*nbcour,380,278,60,None,35))
            nbcour += 1
     
    def draw(self,fenetre,x,y):
        fenetre.blit(self.img,(x,y))
    
    def interactAct(self,x,y):
        return True if ((x-64 == self.x or x+64==self.x)and y == self.y) or ((y-64 == self.y or y+64==self.y)and x== self.x) else False

    def drawInteract(self,fenetre):
        fenetre.blit(pygame.transform.scale(self.backImg, (1024, 175)), [0, 310])
        text = self.font.render(self.nom+":", 1, (255,255,255))
        fenetre.blit(text,(20,320))
        nbcour = 0
        for ev in self.events:
            if not ev.checked():
                if ev.item:
                    text = self.font2.render("requiert "+ev.item, 1, (255,0,0))
                    fenetre.blit(text,(120+328*nbcour,450))
                self.buttons[nbcour].draw(fenetre)
                
            nbcour +=1
    def update(self,score,inv,events):
        it = 0
        for b in self.buttons:
            if b.click():
                if not self.events[it].item:
                    self.events[it].setCheck(True)
                    if self.events[it] in events:
                        score.addScore(self.events[it].score*3)
                    else:
                        score.addScore(self.events[it].score)
                    if self.events[it].img:
                        self.img = self.events[it].img
                    if self.events[it].son:
                        self.events[it].son.play(0)
                else:
                    nbit = 0
                    for item in inv.items:
                        if item.name == self.events[it].item:
                            self.events[it].setCheck(True)
                            if self.events[it] in events:
                                score.addScore(self.events[it].score*5)
                            else:
                                score.addScore(self.events[it].score)
                            if self.events[it].img:
                                self.img = self.events[it].img
                            if self.events[it].son:
                                self.events[it].son.play(0)
                            del inv.items[nbit]
                            break
                        nbit += 1
                    
                    
            it += 1
                
