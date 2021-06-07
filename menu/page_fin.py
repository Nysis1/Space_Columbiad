import pygame
import boutton

class Fin :
    
    def __init__(self, fenetre, score):

        self.image = pygame.image.load("fond_score.png")
        
        self.brejouer = boutton.Button(text="Rejouer", left=20, top=450, width=175, height=75, picture=None, size = 40)
        self.brejouer.setBorderSize(10)
        self.rejouer = False
        self.bmenu = boutton.Button(text="Menu", left=825, top=450, width=175, height=75, picture=None, size = 40)
        self.bmenu.setBorderSize(10)
        self.menu =False

        #j'ai changer a partir d'ici
        self.myfont01 = pygame.font.SysFont("Comic Sans MS", 100)
        self.label01 = self.myfont01.render("BRAVO !", 1, (255,255,255))
        
        self.myfont02 = pygame.font.SysFont("Comic Sans MS", 40)
        self.label02 = self.myfont02.render("Vous avez réussis à amasser un score de : ", 1, (255,255,255))
        self.label03 = self.myfont01.render(score.__str__(), 1, (255,255,255))
        

    def update(self):
        self.brejouer.update()
        self.brejouer.update()
        self.rejouer = self.brejouer.click()
        self.menu = self.bmenu.click()

    def draw(self, fenetre):
        fenetre.blit(self.image, (0,0))
        self.brejouer.draw(fenetre)
        self.bmenu.draw(fenetre)
        fenetre.blit(self.label01, (350,50))
        fenetre.blit(self.label02, (100,225))
        fenetre.blit(self.label03, (400,300))
        
        
        
