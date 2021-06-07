import pygame

# class Task:
#     def __init__(self, text, name, score):
#         self.text = 0
#         self.name = name
#         self.score = score
#         self.check = False

class BucketList:
    """Classe permettant de créer une Bucket List"""
    def __init__(self, events):
        self.events = events[0:5]
        self.img_back = "data/images/BucketList.png"
        self.img_backFerme = "data/images/BucketListFerme.png"
        self.x = 750
        self.y = 5
        self.width = 270
        self.height = 300
        self.open = False
        self.load()

    def load(self):
        self.img_back = pygame.image.load(self.img_back).convert_alpha()
        self.img_backFerme = pygame.image.load(self.img_backFerme).convert_alpha()

    def draw(self, screen):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > self.x and mouse_x < self.x + 270 and mouse_y > self.y and mouse_y < self.y + 300:
            self.height = 300
            self.open = True
            pos = 0
            screen.blit(pygame.transform.scale(self.img_back, (self.width, self.height)), [self.x, self.y])
            for ev in self.events:
                pos += 1
                ev.draw(screen, pos)
        else:
            self.height = 93
            self.open = False
            for ev in self.events:
                ev.visible = False
            screen.blit(pygame.transform.scale(self.img_backFerme, (self.width, self.height)), [self.x, self.y])
