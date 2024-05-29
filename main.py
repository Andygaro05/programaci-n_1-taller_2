import pygame
from Peleador import Personaje  # Importar Personaje primero
from Peleador import Enemigo, Ligero, Pesado

pygame.init()

clock = pygame.time.Clock() #optimizar cada cuanto refresca
fps = 60    #frames x segundo

#pantalla de juego
panel_bajo = 150
screen_width = 1200
screen_heigt = 675 + panel_bajo

#inicializa la pantalla
screen = pygame.display.set_mode((screen_width, screen_heigt))
pygame.display.set_caption("World of fantasy") #nombre del juego

#cargamos las imagenes necesarias según las rutas
fondo_img = pygame.image.load("img/fondo/fondo resize.png").convert_alpha()#"img/fondo/fondo resize.png" 1200, 675
panel_img = pygame.image.load("img/iconos/boton madera.png").convert_alpha()

#creamos la instancia caballero
Caballero = Personaje(400, 560, "Caballero", 250, 50, 10)
Bandido_ligero = Ligero(800, 530, "Bandido Ligero")

#para mostrar el fondo
def dibujar_fondo():
    screen.blit(fondo_img, (0,0))
    
def dibujar_panel():
    screen.blit(panel_img, (0, screen_heigt - panel_bajo))#el panel solo ocupa la parte baja de la pantalla



#validamos que el juego se este ejecutando
run = True
while run:
    clock.tick(fps) #para optimizar la tasa de actualización 

    #dibujar el fondo panel y caballero
    dibujar_fondo()
    dibujar_panel()
    Caballero.draw(screen)
    Bandido_ligero.draw(screen)

    #iteramos atraves de todos los eventos que ocurren
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #actualizamos todas las acciones/funciones
    pygame.display.update()

pygame.quit()