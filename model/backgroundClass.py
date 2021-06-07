""" Arriere plan du jeu => herbes, roches, maisons, barrieres """

import pygame
from pygame.locals import *
import sys
sys.path.append('..')
from data.constantes import *
from model.InteractClass import *
from model.EventClass import Event
from model.InventaireClass import Item
import random

clock = pygame.time.Clock()

def getType(niveau,lig,col,symb):
    if niveau[lig][col-1] not in symb and niveau[lig-1][col] not in symb:
        return 0
    elif niveau[lig][col+1] not in symb and niveau[lig-1][col] not in symb:
        return 2
    elif niveau[lig][col-1] not in symb and niveau[lig+1][col] not in symb:
        return 6
    elif niveau[lig][col+1] not in symb and niveau[lig+1][col] not in symb:
        return 8
    elif niveau[lig][col+1] not in symb and niveau[lig][col-1] in symb:
        return 5
    elif niveau[lig][col-1] not in symb and niveau[lig][col+1] in symb:
        return 3
    elif niveau[lig+1][col] not in symb and niveau[lig-1][col] in symb:
        return 7
    elif niveau[lig-1][col] not in symb and niveau[lig+1][col] in symb:
        return 1
    else:
        return 4
def getTypeBar(niveau,lig,col,symb):
    if niveau[lig+1][col] == symb and niveau[lig-1][col] == symb:
        return 5
    elif niveau[lig][col+1] == symb and niveau[lig][col-1] == symb:
        return 7
    elif niveau[lig][col-1] == symb and niveau[lig-1][col] == symb:
        return 8
    elif niveau[lig][col+1] == symb and niveau[lig-1][col] == symb:
        return 6
    elif niveau[lig][col-1] == symb and niveau[lig+1][col] == symb:
        return 2
    elif niveau[lig][col+1] == symb and niveau[lig+1][col] == symb:
        return 0
    elif niveau[lig+1][col] != symb and niveau[lig-1][col] != symb:
        if niveau[lig][col+1] == symb:
            return 6
        else:
            return 8
    elif niveau[lig][col+1] != symb and niveau[lig][col-1] != symb and niveau[lig+1][col] == symb:
        return 5
    else:
        return 4
class Paysage:
    def __init__(self, fenetre,fichier):
        self.structure = []

        items_list = []
        items_list.append(['carte','data/images/items/carte.png',False])
        items_list.append(['rose','data/images/items/rose.png',False])
        items_list.append(['cle','data/images/items/cle.png',False])
        items_list.append(['emeraude','data/images/items/emeraude.png',True])
        items_list.append(['hanoi','data/images/items/hanoi.png',False])
        items_list.append(['saphir','data/images/items/saphir.png',True])
        items_list.append(['baton','data/images/items/baton.png',False])
        items_list.append(['pizza','data/images/items/pizza.png',False])
        items_list.append(['lunette','data/images/items/lunettes.png',False])
        items_list.append(['diamant','data/images/items/diamant.png',True])
        items_list.append(['sabreLaser','data/images/items/sabreLaser.png',False])

        random.shuffle(items_list)

        self.herbe = pygame.image.load("data/images/Herbe2.png").convert()
        self.fleur = pygame.image.load("data/images/Herbe1.png").convert()
        self.caillou = pygame.image.load("data/images/roche.png").convert()
        self.vert = pygame.image.load("data/images/Plante.png").convert_alpha()
        self.maison1 = pygame.image.load("data/images/Maison5.png").convert_alpha()
        self.maison2 = pygame.image.load("data/images/Maison6.png").convert_alpha()
        self.maison3 = pygame.image.load("data/images/Maison7.png").convert_alpha()
        self.arbretronc = pygame.image.load("data/images/tr.png").convert_alpha()
        self.arbrefeuillage = pygame.image.load("data/images/haut_arbre.png").convert_alpha()
        self.hauteherbe = pygame.image.load("data/images/HauteHerbe.png").convert_alpha()

        self.barriere_hori = pygame.image.load("data/images/Barriere1.png").convert_alpha()
        self.barriere_vert = pygame.image.load("data/images/Barriere2.png").convert_alpha()
        self.rocher1 = pygame.image.load("data/images/rock1.png").convert_alpha()
        self.rocher2 = pygame.image.load("data/images/rock2.png").convert_alpha()
        self.lampadaire = pygame.image.load("data/images/lampadaire.png").convert_alpha()
        self.iut2 = pygame.image.load("data/images/iut2.png").convert_alpha()

        self.pontavant = pygame.image.load("data/images/pont_avant.png").convert_alpha()
        self.ressort = pygame.image.load("data/images/ressort.png").convert_alpha()

        self.herbe = pygame.transform.scale(self.herbe,(64,64))
        self.fleur = pygame.transform.scale(self.fleur,(64,64))
        self.caillou = pygame.transform.scale(self.caillou,(64,64))
        self.vert = pygame.transform.scale(self.vert,(64,64))
        self.maison1 = pygame.transform.scale(self.maison1,(128,128))
        self.maison2 = pygame.transform.scale(self.maison2,(128,128))
        self.maison3 = pygame.transform.scale(self.maison3,(128,128))
        self.arbretronc = pygame.transform.scale(self.arbretronc,(64,64))
        self.arbrefeuillage = pygame.transform.scale(self.arbrefeuillage,(194,128))
        self.hauteherbe = pygame.transform.scale(self.hauteherbe,(64,64))
        self.lampadaire = pygame.transform.scale(self.lampadaire,(64,128))
        self.iut2 = pygame.transform.scale(self.iut2,(384,192))

        self.pontavant = pygame.transform.scale(self.pontavant,(256,64))

        self.barriere_hori = pygame.transform.scale(self.barriere_hori,(64,64))
        self.barriere_vert = pygame.transform.scale(self.barriere_vert,(64,64))
        self.rocher1 = pygame.transform.scale(self.rocher1,(64,64))
        self.rocher2 = pygame.transform.scale(self.rocher2,(64,64))
        self.ressort = pygame.transform.scale(self.ressort,(64,64))

        eau_img = pygame.image.load("data/images/eau_Tile.png").convert_alpha()
        eau_img = pygame.transform.scale(eau_img,(192,192))

        bar_img = pygame.image.load("data/images/barriere_Tile.png").convert_alpha()
        bar_img = pygame.transform.scale(bar_img,(192,192))

        path_img = pygame.image.load("data/images/path_Tile.png").convert_alpha()
        path_img = pygame.transform.scale(path_img,(192,192))

        img = pygame.image.load('data/images/fontaine.png').convert_alpha()
        img = pygame.transform.scale(img,(96,224))
        self.path = []
        for y in range(0,3):
            for x in range(0,3):
                self.path.append(path_img.subsurface(x*64,y*64,64,64))

        self.eau = []
        for y in range(0,3):
            for x in range(0,3):
                self.eau.append(eau_img.subsurface(x*64,y*64,64,64))
        self.bar = []
        for y in range(0,3):
            for x in range(0,3):
                self.bar.append(bar_img.subsurface(x*64,y*64,64,64))
        self.fontaine = []
        for y in range(0,4):
            for x in range(0,3):
                self.fontaine.append(img.subsurface(x*32,y*32,32,32))
        self.fenetre = fenetre
        self.offsetX = 0
        self.offsetY = 0
        self.index_fontaine = 0

        self.events = []
        blanchon1 = Event("Null Pointer","Null Pointer Exception",20,None,None,True,"data/musics/blanchon1.wav")
        blanchon2 = Event("Tour Hanoî","Trouve tours Hanoï",50,"hanoi")
        blanchon3 = Event("Lunette","Trouve mes lunette",50,"lunette","data/Sprites/blanchon.png",True)
        blanchon = [blanchon1,blanchon2,blanchon3]
        coffre = Event("Trouver tresor","Ouvrir",50,"cle","data/images/items/coffreopen.png",True)
        emile = Event("RIP Emile","Deposer fleur",50,"rose","data/images/RIPem2.png",True)
        cotcot = Event("Cot cot","Cot cot cot coooot Cot",10,None,None,True,"data/musics/chicken.wav")
        gandoulf = Event("gandoulf","Trouve mon baton",50,"baton","data/Sprites/gandalf.png", True)
        scoobadoo = Event("scoobadoo","Trouve mes Snacks",50,"snacks","data/Sprites/scooby.png", True)
        danotello = Event("danotello","Trouve ma pizza",50,"pizza","data/Sprites/tortue.png", True)
        darkVadou = Event("darkvadou","Trouve mon sabre",50,"sabreLaser","data/Sprites/darkVador.png", True)
        flint = Event("flint","Trouve ma carte",50,"carte","data/Sprites/pirate.png", True)

        interactions_list = [[[cotcot],"Cot cot","data/images/poule.png"],[blanchon,"M. Blanchon","data/Sprites/blanchonsslun.png"],[[coffre],"Coffre",'data/images/items/coffre.png'],[[emile],"Pierre tombale",'data/images/RIPem1.png'],[[gandoulf],"Gandoulf",'data/Sprites/gandalfSansBaton.png'],[[scoobadoo],"Scooba-Doo",'data/Sprites/scooby.png'],[[danotello],"Danotello",'data/Sprites/tortue.png'],[[darkVadou],"DarkVadou",'data/Sprites/darkVadorSansSabre.png'],[[flint],"Flint",'data/Sprites/pirateSansCarte.png']]
        random.shuffle(interactions_list)

        self.events.append(blanchon1)
        self.events.append(blanchon2)
        self.events.append(blanchon3)
        self.events.append(coffre)
        self.events.append(emile)
        self.events.append(cotcot)
        self.events.append(gandoulf)
        self.events.append(scoobadoo)
        self.events.append(danotello)
        random.shuffle(self.events)

        self.interactionsName = []
        self.interactions = []

        self.items = []
        self.items_Nom = []

        """Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste par ligne à afficher"""
        with open(fichier, "r") as fichier: #On ouvre le fichier
            structure_niveau = []
            #On parcourt les lignes du fichier
            y = 0
            for ligne in fichier:
                ligne_niveau = []
                #On parcourt les sprites (lettres) contenus dans le fichier
                x = 0
                for sprite in ligne:
                    #On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        #On ajoute le sprite à la liste de la ligne
                        if sprite == '0':
                            nb_aleatoire = random.choice(['0','0', 'F'])
                            ligne_niveau.append(nb_aleatoire)
                        elif sprite == 'M':
                            nb_aleatoire2 = random.choice(['A','B', 'C'])
                            ligne_niveau.append(nb_aleatoire2)
                        elif sprite == '#':
                            Interact1 = Interact(interactions_list[0][1],interactions_list[0][2],interactions_list[0][0],x,y)
                            ligne_niveau.append(Interact1.nom)
                            self.interactionsName.append(Interact1.nom)
                            self.interactions.append(Interact1)
                            del interactions_list[0]
                        elif sprite == 'I':
                            item = Item(items_list[0][0],x*64,y*64,items_list[0][1],items_list[0][2])
                            ligne_niveau.append(item.getName())
                            self.items.append(item)
                            self.items_Nom.append(item.getName())
                            del items_list[0]
                        else:
                            ligne_niveau.append(sprite)
                        x += 1
                #On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
                y += 1
            #On sauvegarde cette structure
            self.structure = structure_niveau

    def move(self, x, y):
        self.offsetX -= x/4
        self.offsetY -= y/4

    def afficher(self):
        y = 0
        it=0
        for ligne in self.structure:
            x = 0
            for case in ligne:
                self.fenetre.blit(self.herbe, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                x += 1
            y += 1
        y = 0
        for ligne in self.structure:
            x = 0
            for case in ligne:
                if case == '1':	   #1 = Mur
                    self.fenetre.blit(self.caillou, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'F':	   #F = Fleur
                    self.fenetre.blit(self.fleur, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'A':	   #A = Maison
                    self.fenetre.blit(self.maison1, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'B':	   #B = Maison
                    self.fenetre.blit(self.maison2, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'C':	   #C = Maison
                    self.fenetre.blit(self.maison3, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'v':	   #C = Maison
                    self.fenetre.blit(self.vert, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'o' or case == 'j':	   #o = eau
                    self.fenetre.blit(self.eau[getType(self.structure,y,x,['o','j'])], ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'b':	   #b = barriere
                    self.fenetre.blit(self.bar[getTypeBar(self.structure,y,x,'b')], ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'p':	   #C = Maison
                    self.fenetre.blit(self.rocher1, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'd':	   #C = Maison
                    self.fenetre.blit(self.rocher2, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'U':
                    self.fenetre.blit(self.iut2, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite-128))
                elif case == 'Q':	   #C = Maison
                    self.fenetre.blit(self.ressort, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'c':
                    self.fenetre.blit(self.path[getTypeBar(self.structure,y,x,'c')], ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case in self.interactionsName:
                    self.interactions[it].draw(self.fenetre,((x+self.offsetX)*taille_sprite),((y+self.offsetY)*taille_sprite))
                    it+=1
                x += 1
            y += 1

        for it in self.items:
            it.draw(self.fenetre,self.offsetX,self.offsetY)

    def dropItem(self, item, perso):
        item.setX(perso.x)
        item.setY(perso.y)
        self.fenetre.blit(item.image, (item.x,item.y))

    def afficherApres(self):
        y = 0
        for ligne in self.structure:
            x = 0
            for case in ligne:
                if case == 'r':	   #r = arbre haut
                    self.fenetre.blit(self.arbrefeuillage, ( (x+self.offsetX-1)*taille_sprite,(y+self.offsetY-1)*taille_sprite))
                elif case == 'R':	   #R = arbre bas
                    self.fenetre.blit(self.arbretronc, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'h':	   #R = arbre bas
                    self.fenetre.blit(self.hauteherbe, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'l':
                    self.fenetre.blit(self.lampadaire, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                elif case == 'P':	   #C = Maison
                    self.fenetre.blit(self.pontavant, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                #if case != 'M' and case !='m':
                #	self.fenetre.blit(self.herbe, ( (x+self.offsetX)*taille_sprite,(y+self.offsetY)*taille_sprite))
                x += 1
            y += 1

    def animerBouger(self):
        return True;

    def animerAfficher(self):
        self.fenetre.blit(self.fontaine[self.index_fontaine],((3+self.offsetX)*taille_sprite,(5+self.offsetY)*taille_sprite))
        self.index_fontaine = (self.index_fontaine+1)%12

    def dropItem(self, item, perso):
        item.setX(perso.x)
        item.setY(perso.y)
        self.fenetre.blit(item.image, (item.x,item.y))

    def afficherBulle(self):
        return

    def interactUpdate(self,x,y,score,inv,events):
        for interact in self.interactions:
            if interact.interactAct(x,y):
                interact.drawInteract(self.fenetre)
                interact.update(score,inv,events)
