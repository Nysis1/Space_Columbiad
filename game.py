import pygame
from pygame.locals import *
from model.backgroundClass import Paysage
from model.personnageClass import Perso
from model.InventaireClass import Item
from model.BucketListClass import BucketList
from model.timerClass import Timer
from model.PNJClass import Pnj
from model.scenarioClass import Scenario
from data.constantes import *

class Game:
        def __init__(self,fenetre,sound):
                #--------------------------------------------------------------------------------------------------
                # Construction objets
                self.fenetre = fenetre

                # Arriere plan
                self.papa = Paysage(fenetre,niveau1)

                self.direction = K_DOWN

                self.perso = Perso(self.fenetre,self.papa)

                self.clock = pygame.time.Clock()

                self.tdList = BucketList(self.papa.events)
                #--------------------------------------------------------------------------------------------------
                # Variables inventaire

                self.invUp = False
                self.boxInvUp = False
                self.invMain = 1
                self.clic_i = False
                self.clic_e = False
                self.clic_a = False
                #--------------------------------------------------------------------------------------------------

                self.touch_espace = False;
                self.timer = Timer()
                self.animation = []

                #animation.append(Pnj(fenetre,papa))
                self.animation.append(self.papa)
                # Pnj : fenetre, papapa (le background), perso principal (pour réagir à son approche)
                # son image (sprite de 64x64), dialogue (1er element : ce qu'il demande, 2e element : ce qu'il repond quand on lui donne le bon truc)
                self.animation.append(Pnj(self.fenetre,self.papa,self.perso, 'data/images/vieille.png', ['Bonjour ! Je suis une vieille Grandma', 'Merci bcp !!'], 700, 140, 0, 1000))
                self.animation.append(Pnj(self.fenetre,self.papa,self.perso, 'data/images/garcon.png', ['Hello I\'m a lonely boy'], 400, 1700, 1, 1300))
                self.animation.append(Pnj(self.fenetre,self.papa,self.perso, 'data/images/garcon.png', ['J\'aime beaucoup regarder les fleurs...'], 980, 1100, 0, 1600))
                self.animation.append(self.perso)
                self.scenar = Scenario(self.fenetre)

                self.file = open("menu/score.txt","a")

        def draw(self):
                music  = pygame.mixer.music.load("data/musics/scenar.wav")
                pygame.mixer.music.play(-1)
                self.scenar.draw()
                music  = pygame.mixer.music.load("data/musics/game.wav")
                pygame.mixer.music.play(-1)
                while not self.timer.finTemps():
                        ev = pygame.event.poll()
                        if ev.type == QUIT: break
                        k = pygame.key.get_pressed()
                        self.touch_espace = True if k[K_SPACE] else False
                        if self.touch_espace: self.perso.miseAJourVie(True)
                        else: self.perso.dvol = False
                        if k[K_ESCAPE]:
                                break
                        elif k[K_e]:
                                if self.clic_e == False:
                                        for item in self.papa.items:
                                                if self.perso.x == item.x and self.perso.y == item.y  and self.touch_espace == False:
                                                        if item.isGem:
                                                                self.perso.getInventaire().getGem(self.perso.score, self.papa.items, item, self.fenetre, self.invMain, self.invUp)
                                                        else:
                                                                self.perso.getInventaire().getItem(self.papa.items, item, self.fenetre, self.invMain, self.invUp)
                                self. clic_e = True

                        elif not k[K_e]:
                                self.clic_e = False
                        if k[K_i]:
                                self.boxInvUp = not self.boxInvUp if not self.clic_i else self.boxInvUp
                                if self.boxInvUp:
                                        self.perso.getInventaire().drawBoxInv(self.fenetre, True)
                                        self.perso.getInventaire().draw(self.fenetre, self.invMain, True)
                                        self.clic_i = True
                        elif not k[K_i]:
                                self.clic_i = False
                        if k[K_a]:
                                if self.clic_a == False:
                                        if self.invMain <= len(self.perso.getInventaire().items):
                                                self.perso.getInventaire().removeItem(self.papa.items, self.perso.getInventaire().getItemMain(self.perso.getInventaire().items, self.invMain), self.fenetre, self.perso, self.papa, self.invMain, self.invUp)
                                                self.clic_a = True
                        elif not k[K_a]:
                                self.clic_a = False


                        for animatedItem in self.animation:
                                result = animatedItem.animerBouger()
                        self.papa.afficher()

                        if self.touch_espace:self.papa.afficherApres()
                        for animatedItem in self.animation:
                                result = animatedItem.animerAfficher()
                                #if result != True: animation.remove(animatedItem)
                        if not self.touch_espace : self.papa.afficherApres()
                        for animatedItem in self.animation:
                    		      result = animatedItem.afficherBulle()


                        if k[K_n]: self.perso.action()

                        for i in (K_DOWN,K_UP,K_LEFT,K_RIGHT):
                                if k[i]:
                                        self.direction = i if self.direction != i else self.direction
                                        xvar = (-k[K_LEFT]+k[K_RIGHT])
                                        yvar = (-k[K_UP]+k[K_DOWN])

                                        self.perso.deplacerdd(xvar,yvar,self.touch_espace,self.direction)
                                        break
                                if self.boxInvUp:
                                        for i in (K_0,K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9):
                                                if k[i]:
                                                        if i == K_0:
                                                                self.invMain = 10
                                                        elif i == K_1:
                                                                self.invMain = 1
                                                        elif i == K_2:
                                                                self.invMain = 2
                                                        elif i == K_3:
                                                                self.invMain = 3
                                                        elif i == K_4:
                                                                self.invMain = 4
                                                        elif i == K_5:
                                                                self.invMain = 5
                                                        elif i == K_6:
                                                                self.invMain = 6
                                                        elif i == K_7:
                                                                self.invMain = 7
                                                        elif i == K_8:
                                                                self.invMain = 8
                                                        elif i == K_9:
                                                                self.invMain = 9
                                                        self.perso.getInventaire().draw(self.fenetre,self.invMain, True)
                        self.perso.score.draw(self.fenetre) #FLORIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIAN
                        self.timer.update(); #FLORIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIAN
                        self.timer.draw(self.fenetre) #FLORIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIAN7
                        self.papa.interactUpdate(self.perso.x,self.perso.y,self.perso.score,self.perso.getInventaire(),self.tdList.events)
                        if self.boxInvUp==True:
                                self.perso.getInventaire().drawBoxInv(self.fenetre, self.boxInvUp)
                                self.perso.getInventaire().draw(self.fenetre, self.invMain, self.invUp)
                        self.perso.afficherBarreVie()
                        self.tdList.draw(self.fenetre)
                        pygame.display.flip()
                        self.clock.tick(16)
                self.file.write("You_"+str(self.perso.score.score)+" ")
                self.file.close()
