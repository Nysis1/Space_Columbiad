import pygame
from pygame.locals import *
import sys
sys.path.append('..')
from model.InventaireClass import Inventaire
from data.constantes import *
from model.scoreClass import score #FLORIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIAN

def array_len(array):
        tot = 0
        for i in array:
                tot +=1
        return tot


class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, fenetre, niveau):
		#Sprites du personnage
                img = pygame.image.load('data/Sprites/mechant.png')
                img = pygame.transform.scale(img,(256,256))
                img2 = pygame.image.load('data/Sprites/mechant_vol.png')
                img2 = pygame.transform.scale(img2,(128,512))
		#Position du personnage en cases et en pixels
                self.x = 512
                self.y = 128
                self.offsetX = 0
                self.offsetY = 0
		#Direction par défaut
                self.image = dict([(direction,[img.subsurface(x,y,64,64)for x in range(0,256,64)]) for direction,y in zip((pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP),range(0,256,64))])
                self.image_vol = dict([(direction,[img2.subsurface(x,y,128,128)for x in range(0,128,128)]) for direction,y in zip((pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP),range(0,512,128))])
		#Niveau dans lequel le personnage se trouves
                self.niveau = niveau
                self.index_img = 0
                self.fenetre = fenetre
                self.inventaire = Inventaire(0, 0)
                self.main = 0
                self.vol = False

                self.dx = 0 # voir Léon
                self.dy = 0 # voir Léon
                self.dvol = False # voir Léon
                self.ddirection = K_DOWN;
                self.dejadeplacement = False
                self.score = score() #FLORIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIAN
                self.tailleVie = 100
                self.bloquerVie = False
                self.i = 0
                self.sauterressort = False
                self.saut = 0
                self.varx = 0
                self.vary = 0

	def getInventaire(self):
		return self.inventaire

	def getMain(self):
		return self.main

	def setMain(self, main):
		self.main = main

	def obtain_item(item_get):
		self.inventaire.append(get_item)

	def deplacerdd(self,x,y,vol, direction):
		if self.dejadeplacement == False:
			self.dejadeplacement = True
			self.dx = x
			self.dy = y
			self.miseAJourVie(self.dvol)
			#self.dvol = vol
			self.ddirection = direction
			#self.afficher(self.ddirection, self.dvol)

	def miseAJourVie(self,vol):
		if not self.bloquerVie:
			self.dvol = vol
            #if not self.dvol and self.index_img == 0 and self.x/64 != 0 and self.y/64 != 0:
				#self.varx += round(self.x/64)-self.x/64
				#self.vary += round(self.x/64)-self.y/64
				#self.x = round(self.x/64)*64
				#self.y = round(self.y/64)*64
				#self.deplacer(1,1,vol)
				#self.x = round(self.x/64)*64
				#self.y = round(self.y/64)*64
			"""
            self.x = round(self.x/64)*64
			self.y = round(self.y/64)*64
			while not self.dvol and self.niveau.structure[self.y//64+self.vary][self.x//64+self.varx] in ('1','A','B','C','m','R','b','p','d','n','g','o'):
				self.x += 16
				self.y += 16
				x2=1;
				y2=1;
				if self.x-1 < 64*8 or self.x-1 > (array_len(self.niveau.structure[0])-8)*64 :
					x2=0
					self.offsetX += 16
				if self.y-1 < 64*3 or self.y-1 > (array_len(self.niveau.structure)-6)*64:
					y2=0
					self.offsetY += 16

				self.niveau.move(x2,y2)
                """

	def deplacer(self,x,y,vol):
			if self.dejadeplacement == True:
				self.index_img = (self.index_img+1)%4
				self.vary = 0 if (self.y/64)-(self.y//64) > 0.2 and y<0 else y
				self.varx = 0 if (self.x/64)-(self.x//64) > 0.2 and x<0 else x
				if self.niveau.structure[self.y//64+self.vary][self.x//64+self.varx] == 'Q' and not self.dvol : self.sauterressort = True
				self.dx = x
				self.dy = y
				self.dvol = vol
				if round(self.x/64)*64 != self.x or round(self.y/64)*64 != self.y or (self.niveau.structure[self.y//64+self.vary][self.x//64+self.varx] not in ('1','A','B','C','m','R','b','p','d','n','g', 'o','2')and self.niveau.structure[self.y//64+self.vary][self.x//64+self.varx] not in self.niveau.interactionsName)or(vol==True and self.niveau.structure[self.y//64+self.vary][self.x//64+self.varx] not in ('1','2')) :
					self.x += x*16
					self.y += y*16
					x2=x;
					y2=y;
					if self.x-x < 64*8 or self.x-x > (array_len(self.niveau.structure[0])-8)*64 :
						x2=0
						self.offsetX += x*16
					if self.y-y < 64*3 or self.y-y > (array_len(self.niveau.structure)-6)*64:
						y2=0
						self.offsetY += y*16
					self.niveau.move(x2,y2)

	def ressort(self):
		if self.sauterressort:
			if self.i < 8:
				x = 1
				y = -1
			else:
				x = 1
				y = 1

			self.x += x*16
			self.y += y*16
			x2=x;
			y2=y;
			if self.x-x < 64*8 or self.x-x > (array_len(self.niveau.structure[0])-8)*64 :
				x2=0
				self.offsetX += x*16
			if self.y-y < 64*3 or self.y-y > (array_len(self.niveau.structure)-6)*64:
				y2=0
				self.offsetY += y*16
			self.niveau.move(x2,y2)
			self.i += 1
		if self.i > 15:
			self.sauterressort = False
			self.i = 0

                #print(str(self.x) + " " + str(self.y))
	def afficher(self, direction,vol):
		#self.ressort()
		if self.dvol==False:
				self.fenetre.blit(self.image[direction][self.index_img],(512+self.offsetX,128+self.offsetY))
		else:
				self.fenetre.blit(self.image_vol[direction][0],(480+self.offsetX,98+self.offsetY))

	def action(self):
		print("action")
		if self.niveau.structure[int((512+self.offsetX)/taille_sprite)][int((128+self.offsetY)/taille_sprite)] == 'F' :
			print("Fleur !")
			self.niveau.structure[int((512+self.offsetX)/taille_sprite)][int((128+self.offsetY)/taille_sprite)] == '0'

	def animerBouger(self):
		self.ressort()
		if self.dejadeplacement == True: # si = 0 : n'a pas finit son animation
			self.deplacer(self.dx, self.dy, self.dvol)
			if self.index_img == 0:
				self.dejadeplacement = False
			#self.afficher(self.ddirection, self.dvol)
			return True
		else:
			#if self.index_img == 0:
				#self.offsetX = round(self.offsetX/64)*64
				#self.offsetY = round(self.offsetY/64)*64
				#self.x = round(self.x/64)*64
				#self.y = round(self.y/64)*64
			#if round(self.offsetX/16)*16 != self.offsetX:
				#print(self.x)
				#self.offsetX = round(self.offsetX/16)*16
			return False # a finit son animation

	def animerAfficher(self):

		if self.dejadeplacement == True: # si = 0 : n'a pas finit son animation
			self.afficher(self.ddirection, self.dvol)
			if self.index_img == 0 and self.dejadeplacement == True:
				self.dejadeplacement = False
			#self.afficher(self.ddirection, self.dvol)
			return True;
		else:
			#self.dejadeplacement = False
			self.afficher(self.ddirection, self.dvol)
			return False # a finit son animation

	def afficherBarreVie(self):
        # Pour la barre de vol
		pygame.draw.rect(self.fenetre, (255,0,0), (12,200-self.tailleVie,40,self.tailleVie))
		pygame.draw.rect(self.fenetre, (0,0,0), (12,100,40,100),5)
		if self.tailleVie == 0:
			self.dvol = False
			self.bloquerVie = True;
		if self.tailleVie > 20 and self.bloquerVie:
			self.bloquerVie = False
		if self.tailleVie > 0 and self.dvol: self.tailleVie -= 1
		elif self.tailleVie < 100: self.tailleVie += 0.5

	def afficherBulle(self):
		return
