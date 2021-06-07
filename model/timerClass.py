import pygame

class Timer:
     """Classe permettant la gestion du score"""
     def __init__(self):
        self.seconds = 181
        self.backImg = pygame.image.load('data/Sprites/score_bg.png')
        self.font =pygame.font.Font(None, 70)


     def update(self):
        self.seconds -= 0.0625

     def draw(self,fenetre):
        mins = self.seconds//60
        secs = self.seconds%60
        car = '0' if secs<10 else ''
        fenetre.blit(pygame.transform.scale(self.backImg, (300, 60)), [300, 2])
        if(self.seconds<=30):
             text = self.font.render(str(int(mins))+" : "+car+str(int(secs-secs%1)), 1, (255,0,0))
        else:
             text = self.font.render(str(int(mins))+" : "+car+str(int(secs-secs%1)), 1, (255,255,255))
        fenetre.blit(text,(390,10))

     def finTemps(self):
        return self.seconds<=0;
