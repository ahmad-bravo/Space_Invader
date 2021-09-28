import pygame

class Roadster(pygame.sprite.Sprite):

    def __init__(self,speed,pos_y,pos_x = 1200):
        
        # The characterisics of the roadsters
        super().__init__()

        self.image = pygame.image.load("media/roadster.png")
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x,pos_y)
        self.speed = speed