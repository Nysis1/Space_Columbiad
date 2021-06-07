import pygame
import sys
sys.path.append('..')

class Scenario:
    def __init__(self,fenetre):
        self.fenetre = fenetre
        img1 = pygame.image.load("data/scenario/frame1.png")
        img2 = pygame.image.load("data/scenario/frame2.png")
        img3 = pygame.image.load("data/scenario/frame3.png")
        img4 = pygame.image.load("data/scenario/frame4.png")
        self.imgs = [img1,img2,img3,img4]
        self.rect = pygame.Surface((1024,576), pygame.SRCALPHA)
        self.font =pygame.font.Font(None, 35);
        self.text = self.font.render("Passer(Entrée)", 1, (255,255,255)) 
        self.op = 255  
        self.clock = pygame.time.Clock()
    def draw(self):
        curframe = 0
        curtime = 0
        while curframe<4:
            self.rect.fill((0,0,0,self.op))
            self.fenetre.blit(self.imgs[curframe],(0,0))
            self.fenetre.blit(self.rect,(0,0))
            self.fenetre.blit(self.text,(5,5))
            self.clock.tick(40)
            pygame.display.flip()
            curtime += 0.025
            if curtime < 2:
                self.op -= 2
            elif curtime > 7:
                self.op += 4
            if self.op<0:
                self.op = 0
            elif self.op>255:
                self.op=255
                curframe +=1
                curtime = 0
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT: break
            k = pygame.key.get_pressed()
            if k[pygame.K_ESCAPE]:
                break
            elif k[pygame.K_RETURN]:
                curframe = 4
    
