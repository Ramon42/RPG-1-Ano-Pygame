import pygame
import random








    class Bloco (pygame.sprite.Sprite):
        def __init__(self, cor, largura, altura):
            super().__init__()
            self.image = pygame.Surface([largura,altura])
            self.image.fill(cor)
            self.rect = self.image.get_rect()


    pygame.init()
    largura = 700
    altura = 400
