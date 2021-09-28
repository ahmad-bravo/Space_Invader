import pygame
import random
import math


class Bitcoin(pygame.sprite.Sprite):

    def __init__(self):
    
        super().__init__()
        self.image = pygame.image.load("media/bitcoin.png")
        self.rect = self.image.get_rect()
        self.fire = False
        self.display = False
        self.speed = 10
        self.angle = 0

        self.mining = 0
        self.super = False

    def fire_firsttime(self,pos_x,pos_y):
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.display = True

    def fire_bitcoin(self,settings):
        if self.rect.x <= settings.screen_width:
            self.rect.x += self.speed
        else :
            self.fire = False
            self.display = False

    def on_collision(self):
        self.display = False
        self.fire = False
        self.rect.x = 0
        self.rect.y = 0



    def Super_fire_firsttime(self,pos_x,pos_y):
        self.angle = random.randint(0,359)
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.display = True


    def Super_fire_bitcoin(self,settings):
        if self.rect.x <= settings.screen_width and self.rect.y <= settings.screen_height and self.rect.x >= 0 and self.rect.y >= 0:
            self.rect.x += 10*math.cos(math.radians(self.angle))
            self.rect.y += 10*math.sin(math.radians(self.angle))

        else :
            self.fire = False
            self.display = False


    def Super_on_collision(self):
        self.fire_firsttime(self.rect.x,self.rect.y)
