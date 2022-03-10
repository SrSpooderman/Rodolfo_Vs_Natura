#importaciones
import pygame
import os
pygame.font.init()
#variables
WIDTH = 1000    
HEIGHT = 900
PANTALLA = pygame.display.set_mode((WIDTH, HEIGHT))
BORDE = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FUENTE = pygame.font.SysFont('comicsans', 40)
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40
pygame.display.set_caption("Uwu")
#colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#inisio
pygame.init()
#Sprites
arbol_sprite = pygame.image.load("Assets/Arbol.png")
rodolfo_sprite = pygame.image.load("Assets/Rodolfo.png")
fondo= pygame.image.load("Assets/fondo.png")
#pintar pantalla
def win_drawn(rodolfo, arbol, vida_rodolfo, vida_arbol):
    PANTALLA.blit(fondo, (0,0))
    pygame.draw.rect(PANTALLA, BLACK, BORDE)

    vida_rodolfo_texto = FUENTE.render("Salud Rodolfo: "+str(vida_rodolfo), 1, WHITE)
    vida_arbol_texto = FUENTE.render("Salud Arbol: "+str(vida_arbol), 1, WHITE)
    PANTALLA.blit(vida_rodolfo_texto,(WIDTH - vida_rodolfo_texto.get_width() - 10, 10))
    PANTALLA.blit(vida_arbol_texto, (10, 10))

    PANTALLA.blit(arbol_sprite, (arbol.x, arbol.y))
    PANTALLA.blit(rodolfo_sprite, (rodolfo.x, rodolfo.y))

    pygame.display.update()
#movimientos
#-arbol
def arbol_movimientos(keys_pressed, arbol):
    if keys_pressed[pygame.K_s]:
        arbol.y += 3
    if keys_pressed[pygame.K_w]:
        arbol.y -= 3
    if keys_pressed[pygame.K_d]:
        arbol.x += 3
    if keys_pressed[pygame.K_a]:
        arbol.x -= 3
#-rodolfo
def rodolfo_movimientos(keys_pressed, rodolfo):
    if keys_pressed[pygame.K_k]:
        rodolfo.y += 3
    if keys_pressed[pygame.K_i]:
        rodolfo.y -= 3
    if keys_pressed[pygame.K_l]:
        rodolfo.x += 3
    if keys_pressed[pygame.K_j]:
        rodolfo.x -= 3
#juego
def main():
    rodolfo = pygame.Rect(700, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
    arbol = pygame.Rect(100, 300, PLAYER_WIDTH, PLAYER_HEIGHT)

    vida_rodolfo = 10
    vida_arbol = 10

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                print("uwu")
        keys_pressed = pygame.key.get_pressed()
        rodolfo_movimientos(keys_pressed, rodolfo)
        arbol_movimientos(keys_pressed, arbol)
        win_drawn(rodolfo, arbol, vida_rodolfo, vida_arbol)


    pygame.display.update()

if __name__ == "__main__":
    main()