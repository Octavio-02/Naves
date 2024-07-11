import pygame
import random
import os
import math
from Nave import Nave
from Enemigo import Enemigo
from Menu import Menu

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1280,720))

    menu = Menu()
    menu.iniciar(screen)

    pygame.quit()