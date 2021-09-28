import pygame

class Starship(pygame.sprite.Sprite):

    def __init__(self,pos_x,pos_y,settings):
        super().__init__()
        self.image = pygame.image.load("media/starship.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.damage = 0
        self.settings = settings

    #  These functions move the spaceship
    
    def right(self,settings):
        if self.rect.x < settings.screen_width:
            self.rect.x += 5

    def left(self,settings):
        if self.rect.x > settings.screen_width:
            self.rect.x -= 5

    def down(self,settings):
        if self.rect.y < settings.screen_height:
            self.rect.y += 5

    def up(self,settings):
        if self.rect.y > settings.screen_height:
            self.rect.y -= 5
