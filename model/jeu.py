import pygame
from pygame.locals import *

from GenMap import *

pygame.init()
perso = pygame.image.load('Sprite/mechant.png')
perso = pygame.transform.scale(perso,(256,256))

src = pygame.display.set_mode((1024,576))

#--------------------------------------------------------------------------------------------------

class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

#--------------------------------------------------------------------------------------------------

class CaseInv(object):
    def __init__(self, image, coo):
        self.image = image
        self.coo = coo

    def getImage(self):
        return self.image

    def getCoo(self):
        return self.coo

#--------------------------------------------------------------------------------------------------

class Inventaire(object):
    def __init__(self, x, y):
        self.items = {}
        self.x = x
        self.y = y
        self.img_back = "Sprite/bgInv.png"
        self.img_box = "Sprite/inv.png"
        self.img_boxMain = "Sprite/inv2.png"
        self.cases = []
        self.load()

    def load(self):
        self.img_back = pygame.image.load(self.img_back)
        self.img_box = pygame.image.load(self.img_box)
        self.img_boxMain = pygame.image.load(self.img_boxMain)

    def draw(self, screen, main):
        screen.blit(pygame.transform.scale(self.img_back, (1024, 300)), [0, 476])

        del self.cases[:]

        for i in range(1,10):
            if i == main:
                self.cases.append(CaseInv(pygame.transform.scale(self.img_boxMain, (72, 72)), [i*64+i*40-44, 496]))
            else:
                self.cases.append(CaseInv(pygame.transform.scale(self.img_box, (64, 64)), [i*64+i*40-40, 500]))
        for i in range(0,9):
            screen.blit(self.cases[i].getImage(),self.cases[i].getCoo())

#--------------------------------------------------------------------------------------------------

class Coordonee(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

#--------------------------------------------------------------------------------------------------

class Perso(object):
    def __init__(self, image, coo, direction, inventaire, main):
        self.image = image
        self.coo = coo
        self.direction = direction
        self.inventaire = inventaire
        self.main = main

    def getImage(self):
        return self.image

    def getCoo(self):
        return self.coo

    def getDirection(self):
        return self.direction

    def setDirection(self, direction):
        self.direction = direction

    def getInventaire(self):
        return self.inventaire

    def getMain(self):
        return self.main

    def setMain(self, main):
        self.main = main

    def obtain_item(item_get):
        self.inventaire.append(get_item)

#--------------------------------------------------------------------------------------------------

niveau = Niveau('Niveau/niveau1.txt')
niveau.generer()
niveau.afficher(src)

direction = K_DOWN
index_img = 0

inventaire = Inventaire(0, 0)
main = 0

Joueur = Perso(dict([(direction,[perso.subsurface(x,y,64,64)for x in range(0,256,64)]) for direction,y in zip((K_DOWN,K_LEFT,K_RIGHT,K_UP),range(0,256,64))]), Coordonee(512,128), direction, inventaire, main)

src.blit(Joueur.getImage()[Joueur.getDirection()][index_img],(128,128))
pygame.display.flip()

InvUp = False
myfont = pygame.font.SysFont('Comic Sans MS', 40)
text = myfont.render('Inventaire', False, (0, 0, 0))
invMain = 1

#BOUCLE PRINCIPALE
#Limitation de vitesse de la boucle
while True:
    ev = pygame.event.poll()
    if ev.type == QUIT: break
    k = pygame.key.get_pressed()
    if k[K_i]:
        InvUp = not InvUp
        if InvUp:
            Joueur.getInventaire().draw(src, invMain)
            pygame.display.flip()
        pygame.time.wait(200)
    for i in (K_DOWN,K_UP,K_LEFT,K_RIGHT):
        if k[i]:
            Joueur.setDirection(i) if Joueur.getDirection() != i else Joueur.getDirection()
            xvar = (-k[K_LEFT]+k[K_RIGHT])*16
            yvar = (-k[K_UP]+k[K_DOWN])*16
            for it in range(0,4):
                    index_img = (index_img+1)%4
                    Joueur.getCoo().setX(Joueur.getCoo().getX() + xvar)
                    Joueur.getCoo().setY(Joueur.getCoo().getY() + yvar)
                    niveau.afficher(src)
                    src.blit(Joueur.getImage()[Joueur.getDirection()][index_img],(Joueur.getCoo().getX(),Joueur.getCoo().getY()))
                    if InvUp:
                        Joueur.getInventaire().draw(src,invMain)
                    pygame.display.flip()
                    pygame.time.wait(110)

            break
        if InvUp:
            for i in (K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9):
                if k[i]:
                    if i == K_0:
                        invMain = 10
                    elif i == K_1:
                        invMain = 1
                    elif i == K_2:
                        invMain = 2
                    elif i == K_3:
                        invMain = 3
                    elif i == K_4:
                        invMain = 4
                    elif i == K_5:
                        invMain = 5
                    elif i == K_6:
                        invMain = 6
                    elif i == K_7:
                        invMain = 7
                    elif i == K_8:
                        invMain = 8
                    elif i == K_9:
                        invMain = 9
                    Joueur.getInventaire().draw(src,invMain)
                    pygame.display.flip()
    else: index_img = 0
    niveau.afficher(src)
    src.blit(Joueur.getImage()[Joueur.getDirection()][index_img],(Joueur.getCoo().getX(),Joueur.getCoo().getY()))
    if InvUp==True:
        Joueur.getInventaire().draw(src, invMain)
    pygame.display.flip()
