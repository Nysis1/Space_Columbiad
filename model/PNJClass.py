import pygame
import sys
sys.path.append('..')
from data.constantes import *

class Pnj:
	"""Classe permettant de créer un personnage"""
	def __init__(self, fenetre, niveau, persprinc, image, dialogue,x,y,direct,endroit):
		#Sprites du personnage
            img = pygame.image.load(image).convert_alpha()
            img = pygame.transform.scale(img,(256,256))
		#Position du personnage en cases et en pixels
            self.x = x
            self.y = y
            self.direction = direct
            self.endroit = endroit
            self.depart = x

            self.offsetX = 0
            self.offsetY = 0
		#Direction par défaut
            self.image = dict([(direction,[img.subsurface(x,y,64,64)for x in range(0,256,64)]) for direction,y in zip((pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP),range(0,256,64))])
		#Niveau dans lequel le personnage se trouves
            self.niveau = niveau
            self.index_img = 0
            self.fenetre = fenetre
            self.deplacement = 1;
            self.persoprinc = persprinc

            self.bulle = pygame.image.load('data/images/bulledialogue.png').convert_alpha()
            self.bulle = pygame.transform.scale(self.bulle,(330,64))

            self.dialogue = dialogue

	def deplacer(self,x,y):
            self.index_img = (self.index_img+1)%4
            #if self.niveau.structure[self.y//64+vary][self.x//64+varx] not in ('1','A','B','C','m','R','b','p','d','n') or (vol==True and self.niveau.structure[self.y//64+vary][self.x//64+varx] != '1') :
            self.x += x*16
            self.y += y*16

	def afficher(self, direction):
            self.fenetre.blit(self.image[direction][self.index_img],(self.x+self.niveau.offsetX*taille_sprite,self.y+self.niveau.offsetY*taille_sprite))

	def animerBouger(self):
            return True;

	def animerAfficher(self):
		if (self.persoprinc.dvol == False and 512+self.persoprinc.offsetX-taille_sprite < self.x+self.niveau.offsetX*taille_sprite and 512+self.persoprinc.offsetX+taille_sprite > self.x+self.niveau.offsetX*taille_sprite and 128+self.persoprinc.offsetY-taille_sprite < self.y+self.niveau.offsetY*taille_sprite and 128+self.persoprinc.offsetY+taille_sprite > self.y+self.niveau.offsetY*taille_sprite):
			if self.deplacement == 1: self.afficher(pygame.K_RIGHT)
			else: self.afficher(pygame.K_LEFT)
		elif self.deplacement == 1:
			if self.direction == 0:
				self.deplacer(1,0)
				self.afficher(pygame.K_RIGHT)
				if self.x > self.endroit:
					self.deplacement = 0
			else:
				self.deplacer(0,1)
				self.afficher(pygame.K_DOWN)
				if self.y > self.endroit:
					self.deplacement = 0
		else:
			if self.direction == 0:
				self.deplacer(-1,0)
				self.afficher(pygame.K_LEFT)
				if self.x < self.depart:
					self.deplacement = 1
			else:
				self.deplacer(0,-1)
				self.afficher(pygame.K_UP)
				if self.y < self.depart:
					self.deplacement = 1

	def afficherBulle(self):
		if self.persoprinc.dvol == False and 512+self.persoprinc.offsetX-taille_sprite < self.x+self.niveau.offsetX*taille_sprite and 512+self.persoprinc.offsetX+taille_sprite > self.x+self.niveau.offsetX*taille_sprite and 128+self.persoprinc.offsetY-taille_sprite < self.y+self.niveau.offsetY*taille_sprite and 128+self.persoprinc.offsetY+taille_sprite > self.y+self.niveau.offsetY*taille_sprite:
			#print("stop")
			#if self.deplacement == 1: self.afficher(pygame.K_RIGHT)
			#else: self.afficher(pygame.K_LEFT)

			self.fenetre.blit(self.bulle, (self.x+self.niveau.offsetX*taille_sprite-220,self.y+self.niveau.offsetY*taille_sprite-50) )
			myfont = pygame.font.SysFont("Arial", 17)
			# render text
			label = myfont.render(self.dialogue[0], 1, (0,0,0))
			self.fenetre.blit(label, (self.x+self.niveau.offsetX*taille_sprite-200,self.y+self.niveau.offsetY*taille_sprite-35))
