import pygame
class Button:
    def __init__(self, text="", left=10, top=30, width=None, height=20, picture=None, size = 10):
        #text : permetde choisir son text à l'intérieur du bouton
        #rappel : x et y comme en svg
        #left : coordonnée en abscices
        #top : coordonnée en ordonnée
        #width : c'est la largeur que votre boutton aura
        #height : c'est la hauteur qu'aura votre bouton
        #picture : si vous voulez que votre bouton cotienne une image
        #size permet de modifier la size de votre texte

        self.text = text
        self.left = left
        self.top = top
        self.height = height
        self.colour1 = (0, 0, 255)  # main
        self.colour2 = (255, 255, 255)  # border
        self.colour3 = (0, 255, 26)  # hover
        self.colour4 = (245, 28, 225)
        self.fontname = "Arial"
        self.fontsize = self.height - size
        self.mouse_over = False
        self.mouse_down = False
        self.mouse = "off"
        self.clicked = False
        self.bordersize = 10          


        self.font = pygame.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pygame.font.Font.size(self.font, self.text)
        if width == None:
            self.width = self.text_width + 20
            self.width_type = "text"
        else:
            self.width = width
            self.width_type = "user"
        self.buttonUP = pygame.Surface((self.width, self.height))
        self.buttonDOWN = pygame.Surface((self.width, self.height))
        self.buttonHOVER = pygame.Surface((self.width, self.height))
        self.__update__()
        #permet de changer la border size de up et hover
    def setBorderSize(self, borderSize):
         self.bordersize = borderSize

    def __update__(self):


        # up
        r, g, b = self.colour1
        self.buttonUP.fill(self.colour1)
        pygame.draw.rect(self.buttonUP, (r, g, b), (0, 0,self.width, self.height/2), 0)
        pygame.draw.line(self.buttonUP,self.colour2, (2, 0), (self.width-3, 0), self.bordersize)
        pygame.draw.line(self.buttonUP, self.colour2, (2,self.height-1), (self.width-3, self.height-1), self.bordersize)
        pygame.draw.line(self.buttonUP, self.colour2, (0, 2), (0,self.height-3), self.bordersize)
        pygame.draw.line(self.buttonUP, self.colour2,(self.width-1, 2), (self.width-1, self.height-3), self.bordersize)
        self.buttonUP.set_at((1, 1), self.colour2)
        self.buttonUP.set_at((self.width-2, 1), self.colour2)
        self.buttonUP.set_at((1, self.height-2), self.colour2)
        self.buttonUP.set_at((self.width-2, self.height-2),self.colour2)
        self.buttonUP.blit(self.font.render(self.text, False, (0, 0, 0)), ((self.width/2)-(self.text_width/2), (self.height/2)-(self.text_height/2)))


        # hover
        self.buttonHOVER.fill(self.colour3)
        pygame.draw.rect(self.buttonHOVER, self.colour4, (0, 0, self.width, self.height/2), 0)
        pygame.draw.line(self.buttonHOVER, self.colour2, (2, 0), (self.width-3, 0), self.bordersize)
        pygame.draw.line(self.buttonHOVER, self.colour2, (2, self.height-1), (self.width-3, self.height-1), self.bordersize)
       # pygame.draw.line(self.buttonHOVER, self.colour4, (2, self.height-2), (self.width-3, self.height-2), 1)
        pygame.draw.line(self.buttonHOVER, self.colour2, (0, 2), (0, self.height-3), self.bordersize)
       # pygame.draw.line(self.buttonHOVER, self.colour4, (1, 2), (1, self.height-3), 1)
        pygame.draw.line(self.buttonHOVER, self.colour2, (self.width-1, 2), (self.width-1, self.height-3), self.bordersize)
        self.buttonHOVER.set_at((1, 1), self.colour2)
        self.buttonHOVER.set_at((self.width-2, 1), self.colour2)
        self.buttonHOVER.set_at((1, self.height-2), self.colour2)
        self.buttonHOVER.set_at((self.width-2, self.height-2), self.colour2)
        self.buttonHOVER.blit(self.font.render(self.text, False, (0, 0, 0)), ((self.width/2)-(self.text_width/2), (self.height/2)-(self.text_height/2)))

        # down
        r, g, b = self.colour3
        r2, g2, b2 = self.colour4
        self.buttonDOWN.fill((r, g, b))
        pygame.draw.rect(self.buttonDOWN, (r2, g2, b2), (0, 0, self.width, self.height/2), 0)
        pygame.draw.line(self.buttonDOWN, self.colour2, (2, 0), (self.width-3, 0), 1)
        pygame.draw.line(self.buttonDOWN, (r, g, b), (2, 1), (self.width-3, 1), 2)
        pygame.draw.line(self.buttonDOWN, self.colour2, (2, self.height-1), (self.width-3, self.height-1), 1)
        pygame.draw.line(self.buttonDOWN, self.colour2, (0, 2), (0, self.height-3), 1)
        pygame.draw.line(self.buttonDOWN, (r, g, b), (1, 2), (1, self.height-3), 2)
        pygame.draw.line(self.buttonDOWN, self.colour2, (self.width-1, 2), (self.width-1, self.height-3), 1)
        self.buttonDOWN.set_at((1, 1), self.colour2)
        self.buttonDOWN.set_at((self.width-2, 1), self.colour2)
        self.buttonDOWN.set_at((1, self.height-2), self.colour2)
        self.buttonDOWN.set_at((self.width-2, self.height-2), self.colour2)
        self.buttonDOWN.blit(self.font.render(self.text, False, (0, 0, 0)), ((self.width/2)-(self.text_width/2)+1, (self.height/2)-(self.text_height/2)))



    def __mouse_check__(self):
        _1, _2, _3 = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if not _1:
            self.mouse = "off"
        if mouse_x > self.left and mouse_x < self.left + self.width and mouse_y > self.top and mouse_y < self.top + self.height and not self.mouse == "down":
            self.mouse = "hover"
        if not self.mouse_down and _1 and self.mouse == "hover":
            self.mouse = "down"
            self.clicked = True
        if self.mouse == "off":
            self.clicked = False



    def draw(self, surface):
        self.__mouse_check__()
        if self.mouse == "hover":
            surface.blit(self.buttonHOVER, (self.left, self.top))
        elif self.mouse == "off":
            surface.blit(self.buttonUP, (self.left, self.top))
        elif self.mouse == "down":
            surface.blit(self.buttonDOWN, (self.left, self.top))

    def click(self):
        #cette foction pour avoir acces de l'exterieure sur l'eatat du boutton
        _1, _2, _3 = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.left and mouse_x < self.left + self.width and mouse_y > self.top and mouse_y < self.top + self.height and self.clicked and not _1:
            self.clicked = False
            return True
        else:
            return False

    def set_text(self, text, fontname="Arial", fontsize=None):
        self.text = text
        self.fontname = fontname
        if not fontsize == None:
            self.fontsize = fontsize
        self.font = pygame.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pygame.font.Font.size(self.font, self.text)
        if self.width_type == "text":
            self.width = self.text_width + 20
        self.buttonUP = pygame.Surface((self.width, self.height))
        self.buttonDOWN = pygame.Surface((self.width, self.height))
        self.buttonHOVER = pygame.Surface((self.width, self.height))
        #on remet à jour notre rectangle
        self.__update__()




"""usage:
import pygame
from pygame.locals import *
import boutton
import time
pygame.init()

fenetre = pygame.display.set_mode((640,480), RESIZABLE)
#color background
color = [0, 0, 0]
fenetre.fill(color)
pygame.display.set_caption("obcurs redemption")
pygame.display.flip()


b = boutton.Button(text="opt", left=10, top=30, width=300, height=200, picture=None, size = 100)
b.setBorderSize(30)
b.draw(fenetre)
pygame.display.flip()

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit
            run = False
            break
        # check if the button was clicked do stuff for when button is clicked
        if b.click():
            myfont = pygame.font.SysFont("Arial", 15)
            text = myfont.render("Bravo ca marche", 100, (255,255,0))
            fenetre.blit(text, (400,400))

    b.__update__()
    b.draw(fenetre)
    pygame.display.flip()


pygame.quit()


"""
