import pygame
from pygame.locals import *
import pygame.mixer
import menu.boutton
from menu.option_page import *
from menu.Menu import *
from menu.HighScore import *
from menu.Tuto import *
import os
from menu.page_fin import *
from game import *


pygame.init()

fenetre = pygame.display.set_mode((1024,568))#,FULLSCREEN)
#color background
color = [0, 0, 0]
fenetre.fill(color)
pygame.display.set_caption("Zorg's redemption")
pygame.display.flip()
option = False
menu = True
play = False
highscore = False
tuto = False
play = False

pygame.mixer.init()

bouba = pygame.mixer.music.load('data/musics/menu.wav')
pygame.mixer.music.play()

levelSound = 10

Mn = Menu(fenetre)

Hso = HighScore(fenetre)
touto = Tuto(fenetre)
Opt = Option(fenetre)
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit
            pygame.mixer.music.stop()
            run = False
            break
    if menu == True and option == False and highscore == False and tuto == False and play == False:
        Mn.update()
        Mn.draw(fenetre)
        pygame.display.set_caption("Zorg's redemption - Menu")

        if Mn.options:
            pygame.display.set_caption("Zorg's redemption - Options")
            option = True
        elif Mn.quit:
            pygame.display.quit
            pygame.mixer.music.stop()
            run = False
            break
        elif Mn.jouer:
            pygame.display.set_caption("Zorg's redemption - Jeux")
            pygame.mixer.music.stop()
            play = True
        elif Mn.hightscore:
            pygame.display.set_caption("Zorg's redemption - HighScore")
            highscore = True
        elif Mn.regle:
            pygame.display.set_caption("Zorg's redemption - Règle du jeu")
            tuto = True
    elif option == True:
        sons = levelSound*4
        pygame.mixer.music.set_volume(sons/100)
        Opt.changerSons(levelSound)
        Opt.update(fenetre)
        Opt.draw(fenetre)
        if Opt.menu:
            menu = True
            option = False
        elif Opt.plus:
            if (levelSound < 25):
                levelSound += 5
                Opt.changerSons(levelSound)
        elif Opt.moins:
            if (levelSound > 0):
                levelSound -= 5
                Opt.changerSons(levelSound)
    elif highscore == True:
        Hso.update()
        Hso.draw(fenetre)
        if Hso.menu:
            highscore = False
            menu = True
    elif tuto == True:
        touto.update()
        touto.draw(fenetre)
        if touto.menu:
            menu = True
            tuto = False
    elif play==True:
        game = Game(fenetre,levelSound)
        game.draw()
        play=False
        menu = True
        bouba  = pygame.mixer.music.load("data/musics/menu.wav")
        pygame.mixer.music.play(-1)
    #manque le jouer
    pygame.display.flip()


pygame.quit()
