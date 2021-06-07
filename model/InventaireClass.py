import pygame
import sys
sys.path.append('..')

class Item(object):
    def __init__(self, name, x, y, image, isGem):
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image,(64,64))
        self.inInv = False
        self.inMain = False
        self.isGem = isGem

    def getName(self):
        return self.name

    def getImage(self):
        return self.image

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def draw(self, fenetre, offX, offY):
        fenetre.blit(self.getImage(),[self.x+offX*64,self.y+offY*64])

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
        self.items = []
        self.x = x
        self.y = y
        self.img_back = "data/Sprites/bgInv.png"
        self.img_box = "data/Sprites/inv.png"
        self.img_boxMain = "data/Sprites/inv2.png"
        self.cases = []
        self.load()

    def load(self):
        self.img_back = pygame.image.load(self.img_back).convert_alpha()
        self.img_box = pygame.image.load(self.img_box).convert_alpha()
        self.img_boxMain = pygame.image.load(self.img_boxMain).convert_alpha()

    def draw(self, screen, main, invUp):
        del self.cases[:]

        for i in range(0,len(self.items)):
            if i+1 == main:
                self.cases.append(CaseInv(pygame.transform.scale(self.items[i].getImage(), (72, 72)), [50+i*960/9-4, 496]))
            else:
                self.cases.append(CaseInv(pygame.transform.scale(self.items[i].getImage(), (64, 64)), [50+i*960/9, 500]))

        for i in range(len(self.items),9):
                if i+1 == main:
                    self.cases.append(CaseInv(pygame.transform.scale(self.img_boxMain, (72, 72)), [50+i*960/9-4, 496]))
                else:
                    self.cases.append(CaseInv(pygame.transform.scale(self.img_box, (64, 64)), [50+i*960/9, 500]))
        for i in range(0,9):
            screen.blit(self.cases[i].getImage(),self.cases[i].getCoo())

    def drawBoxInv(self, screen, boxInvUp):
            screen.blit(pygame.transform.scale(self.img_back, (1024, 300)), [0, 476])

    def getItem(self, items, item, fenetre, invMain, invUp):
        if len(self.items) < 9:
            items.remove(item)
            self.items.append(item)
            self.draw(fenetre, invMain, invUp)
        else:
            print("inventaire plein")

    def getGem(self, score, items, item, fenetre, invMain, invUp):
        items.remove(item)
        score.addScore(10)
        self.draw(fenetre, invMain, invUp)

    def getItemMain(self, items, main):
        print(items[main-1].getName())
        return items[main-1]

    def removeItem(self, items, item, fenetre, perso, papa, invMain, invUp):
        if len(self.items) > 0:
            papa.dropItem(item, perso)
            items.append(item)
            del self.items[invMain-1:invMain]
            self.draw(fenetre, invMain, invUp)
        else:
            print("inventaire vide")
