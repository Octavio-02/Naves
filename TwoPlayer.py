import pygame
from Nave import Nave
from Enemigo import Enemigo

class TwoPlayer:

    CANTIDAD_ENEMIGOS = 0

    def __init__(self):
        self.CANTIDAD_ENEMIGOS = 10

    def colision(self,nave,enemigo):
        if enemigo.y + 63 >= nave.y and enemigo.y <= nave.y + 100 and enemigo.x + 56 >= nave.x  and enemigo.x <= nave.x + 95:
            return 1
    
    def modulo(self,num):
        if num < 0:
            num = num * (-1)
        return num

    def diferenciacion(self,enemigos):
        tam = len(enemigos)
        for i in range(0,tam,1):
            for j in range(i+1,tam,1):
                if enemigos[j].y < 0:
                    while self.modulo(enemigos[i].y - enemigos[j].y) < 84 or self.modulo(enemigos[i].x - enemigos[j].x) < 30:
                        enemigos[j].generar()

    def iniciar(self,screen):

        font = pygame.font.SysFont("Garamond", 30)
        titulo = pygame.font.SysFont("Garamond", 80)

        running = True
        perdedor = 0

        uno = Nave("images/nave.png")
        dos = Nave("images/naveAzul.png")

        enemigo = []
        puntuacion = 1

        for i in range(self.CANTIDAD_ENEMIGOS):
            enemigo.append(Enemigo())
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            lista = pygame.key.get_pressed()
            if lista[pygame.K_UP] == True and uno.y >= 10:
                uno.y = uno.y - 2
            if lista[pygame.K_DOWN] == True and uno.y <= 600:
                uno.y = uno.y + 2
            if lista[pygame.K_LEFT] == True and uno.x >= 10:
                uno.x = uno.x - 2
            if lista[pygame.K_RIGHT] == True and uno.x <= 1170:
                uno.x = uno.x + 2
            if lista[pygame.K_w] == True and dos.y >= 10:
                dos.y = dos.y - 2
            if lista[pygame.K_s] == True and dos.y <= 600:
                dos.y = dos.y + 2
            if lista[pygame.K_a] == True and dos.x >= 10:
                dos.x = dos.x - 2
            if lista[pygame.K_d] == True and dos.x <= 1170:
                dos.x = dos.x + 2
            
            for i in range(self.CANTIDAD_ENEMIGOS):
                enemigo[i].bajar(puntuacion)
                enemigo[i].chequear()
                bandera = self.colision(uno,enemigo[i])
                banderaDos = self.colision(dos,enemigo[i])
                if bandera == 1:
                    running = 0
                    perdedor = 1
                if banderaDos == 1:
                    running = 0
                    perdedor = 2
            self.diferenciacion(enemigo)

            screen.fill("grey")
            screen.blit(uno.image,(uno.x,uno.y))
            screen.blit(dos.image,(dos.x,dos.y))
            for i in range(self.CANTIDAD_ENEMIGOS):
                screen.blit(enemigo[i].image,(enemigo[i].x,enemigo[i].y))
            screen.blit(font.render("Puntos: " + str(puntuacion), True, (0, 0, 0)),(10,10))
            puntuacion = puntuacion + 1

            pygame.display.flip()
        
        running = 1

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    running = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = 0

            screen.fill("grey")
            screen.blit(titulo.render("Puntuacion: " + str(puntuacion), True, (0, 0, 0)),(360,300))
            if perdedor == 1:
                screen.blit(titulo.render("Ha perdido el Jugador Rojo",True, (0,0,0)),(210,400))
            elif perdedor == 2:
                screen.blit(titulo.render("Ha perdido el jugador Azul",True, (0,0,0)),(210,400))
            pygame.display.flip()