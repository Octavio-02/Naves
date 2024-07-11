import pygame
import random
import math

class Enemigo:
    image = ""
    x = 10
    y = 10

    def __init__(self):
        self.image = pygame.image.load("images/enemigo.png")
        self.generar()
    
    def bajar(self,puntuacion):
        self.y = self.y + (math.log(puntuacion,1.7)/20)

    def generar(self):
        self.x = random.randint(10,1200)
        self.y = random.randint(-1000,10)
    
    def chequear(self):
        if self.y >= 725:
            self.generar()