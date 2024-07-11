import pygame
from OnePlayer import OnePlayer
from TwoPlayer import TwoPlayer

class Menu:

    def posMouse(self):
        pos = pygame.mouse.get_pos()
        if pos[0] >= 360 and pos[0] <= 930 and pos[1] >= 300 and pos[1] <= 400:
            return 1
        elif pos[0] >= 360 and pos[0] <= 1025 and pos[1] >= 400 and pos[1] <= 490:
            return 2
        elif pos[0] >= 360 and pos[0] <= 500 and pos[1] >= 490 and pos[1] <= 580:
            return 3

    def iniciar(self,screen):
        titulo = pygame.font.SysFont("Garamond", 80)

        while True:

            colorUno  = (0,0,0)
            colorDos  = (0,0,0)
            colorTres = (0,0,0)

            pos = self.posMouse()
            if pos == 1:
                colorUno = (243,221,0)
            elif pos == 2:
                colorDos = (243,221,0)
            elif pos == 3:
                colorTres = (243,221,0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.posMouse()
                    if pos == 1:
                        oneplayer = OnePlayer()
                        oneplayer.iniciar(screen)
                    if pos == 2:
                        twoplayer = TwoPlayer()
                        twoplayer.iniciar(screen)
                    if pos == 3:
                        quit()


            screen.fill("grey")

            screen.blit(titulo.render("Jugar: Un Jugador", True, colorUno),(360,300))
            screen.blit(titulo.render("Jugar: Dos Jugadores", True, colorDos),(360,390))
            screen.blit(titulo.render("Salir", True, colorTres),(360,490))

            pygame.display.flip()