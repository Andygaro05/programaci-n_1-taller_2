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

#cargamos las imagenes
fondo_img = pygame.image.load("img/fondo/fondo resize.png").convert_alpha()#"img/fondo/fondo resize.png" 1200, 675
panel_img = pygame.image.load("img/iconos/boton madera.png").convert_alpha()

#creamos la instancias de los personajes
Caballero = Personaje(400, 560, "Caballero", 250, 50, 10)
ligero1 = Ligero(800, 530, "Bandido Ligero")
pesado1 = Pesado(1000, 530, "Pesado")

bandidos = []
bandidos.append(ligero1)
bandidos.append(pesado1)

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

    #dibujamos el estado actual del caballero
    Caballero.update()
    Caballero.draw(screen)

    #iteramos la lista de enemigos
    for bandido in bandidos:
        bandido.update()
        bandido.draw(screen)

    #iteramos atraves de todos los eventos que ocurren
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #actualizamos todas las acciones/funciones
    pygame.display.update()

pygame.quit()