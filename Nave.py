import pygame

class Nave:
    image = ""
    x = 10
    y = 10

    def __init__(self,ruta):
        self.image = pygame.image.load(ruta)
        self.x = 614
        self.y = 602