import pygame
from Peleador import *  # Importamos todo
from Peleador import damage_text_group  #toca hacer el llamado individual

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


#variables de juego
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
clicked = False
pocion = False
efecto_pocion = 20  #La pocion sana de a 20 de salud
game_over = 0

#fuente de juego
font = pygame.font.SysFont("Times New Roman", 24)

#definir colores
negro = (0,0,0)
rojo = (255,0,0)
verde = (0,255,0)

#cargamos las imagenes
fondo_img = pygame.image.load("img/fondo/fondo resize.png").convert_alpha()
panel_img = pygame.image.load("img/iconos/boton madera.png").convert_alpha()
pocion_img = pygame.image.load("img/iconos/pocion salud.png").convert_alpha()
victoria =  pygame.image.load("img/iconos/victoria.png").convert_alpha()
derrota = pygame.image.load("img/iconos/derrota.png").convert_alpha()

#imagen de la espada para el mouse
mouse_img = pygame.image.load("img/iconos/espada mouse.png").convert_alpha()

#función para dibujar texto
def dibujar_texto(texto, font, text_col, x, y):
    img = font.render(texto, True, text_col)
    screen.blit(img,(x,y))

#para mostrar el fondo
def dibujar_fondo():
    screen.blit(fondo_img, (0,0))
    
def dibujar_panel():
    screen.blit(panel_img, (0, screen_heigt - panel_bajo))#el panel solo ocupa la parte baja de la pantalla

    #mostrar stats del caballero
    dibujar_texto(f"{Caballero.name} HP: {Caballero.hp}", font, negro, 100, screen_heigt - panel_bajo+ 10)

    #mostrar stats bandidos
    for count, i in enumerate(bandidos):
        #mostrar nombre y vida
        dibujar_texto(f"{i.name} HP: {i.hp}", font, negro, 800, (screen_heigt - panel_bajo+10)+ count * 60)

#creamos la instancias de los personajes
Caballero = Personaje(400, 560, "Caballero", 150, 50, 10,3)
ligero1 = Ligero(800, 530, "Bandido Ligero",1)
pesado1 = Pesado(1000, 530, "Enemigo Pesado",3)

bandidos = []
bandidos.append(ligero1)
bandidos.append(pesado1)

#Creamos las barras de vida
barra_vida_caballero = HealthBar(100, screen_heigt-panel_bajo+40, Caballero.hp, Caballero.vida_max)
barra_vida_ligero1 = HealthBar(800, screen_heigt-panel_bajo+40, ligero1.hp, ligero1.vida_max)
barra_vida_pesado1 = HealthBar(800, screen_heigt-panel_bajo+100, pesado1.hp, pesado1.vida_max)

#creamos los botones
boton_pocion = Button(screen, 100, screen_heigt - panel_bajo + 70, pocion_img, 64, 64)

#validamos que el juego se este ejecutando
run = True
while run:
    clock.tick(fps) #para optimizar la tasa de actualización 

    #dibujar el fondo panel y caballero
    dibujar_fondo()
    dibujar_panel()
    barra_vida_caballero.draw(screen, Caballero.hp)
    barra_vida_ligero1.draw(screen, ligero1.hp)
    barra_vida_pesado1.draw(screen, pesado1.hp)

    #dibujamos el estado actual del caballero
    Caballero.update()
    Caballero.draw(screen)

    #iteramos la lista de enemigos
    for bandido in bandidos:
        bandido.update()
        bandido.draw(screen)

    #dibujar el daño
    damage_text_group.update()
    damage_text_group.draw(screen)

    #Controlar las acciones del jugador
    #reset las acciones
    attack = False
    objetivo = None
    pocion = False
    pos = pygame.mouse.get_pos()

    #permitimos la visualización del mouse
    pygame.mouse.set_visible(True)

    #si tocamos la hitbox de un enemigo, cambiar el cursor a espada
    for count, bandido in enumerate(bandidos):
        if bandido.rect.collidepoint(pos):
            #ocultamos el mouse
            pygame.mouse.set_visible(False)
            #mostramos la espada
            screen.blit(mouse_img, pos)
            #si se presiona el mouse atacamos al objetivo
            if clicked == True and bandido.vivo == True:
                attack = True
                objetivo = bandidos[count]
    if boton_pocion.draw():
        pocion = True
    #mostrar las pociones restantes
    dibujar_texto(str(Caballero.pociones), font, rojo, 150, screen_heigt - panel_bajo + 110)

    #validamos que el juego no haya finalizado
    if game_over == 0:
        #acción del jugador
        if Caballero.vivo == True:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #buscar acción de jugador
                    #atacar
                    if attack == True and objetivo != None:
                        Caballero.attack(objetivo)
                        current_fighter +=1
                        action_cooldown = 0

                    #pocion
                    if pocion == True:
                        if Caballero.pociones > 0:
                            #validar para evitar overhealth
                            if Caballero.vida_max - Caballero.hp > efecto_pocion:
                                sanacion = efecto_pocion
                            else:
                                sanacion = Caballero.vida_max - Caballero.hp
                            Caballero.hp += sanacion
                            Caballero.pociones -= 1
                            damage_text = DamageText(Caballero.rect.centerx, Caballero.rect.y, str(sanacion), verde)
                            damage_text_group.add(damage_text)
                            current_fighter += 1
                            action_cooldown = 0
        else:
            game_over = -1

        #acción del enemigo
        #creamos el enumerate para recorrer bandidos y almacenar sus indices
        for count,bandido in enumerate(bandidos):
            if current_fighter == count + 2:#se inicia en 2 pq se arranca en 0 y 1 es el caballero
                if bandido.vivo == True:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #validamos si necesita curarse primero
                        if (bandido.hp / bandido.vida_max) < 0.5 and bandido.pociones >0:
                            #validar que no haya overhealth
                            if bandido.vida_max - bandido.hp > efecto_pocion:
                                sanacion = efecto_pocion
                            else:
                                sanacion = bandido.vida_max - bandido.hp
                            bandido.hp += sanacion
                            bandido.pociones -= 1
                            damage_text = DamageText(bandido.rect.centerx, bandido.rect.y, str(sanacion), verde)
                            damage_text_group.add(damage_text)
                            current_fighter += 1
                            action_cooldown = 0
                        else:    
                            bandido.attack(Caballero)
                            current_fighter += 1    #cambia de turno
                            action_cooldown = 0 #reinicia el cd de cada acción
                else:
                    bandido.death()
                    current_fighter += 1

        #si todos los enemigos ya usaron su movida
        if current_fighter > total_fighters:
            current_fighter = 1
    #validamos si game over
    elif game_over != 0:
        if game_over == 1:
            screen.blit(victoria, (350, 400))
        else:
            screen.blit(derrota, (360, 250))

    #validar si todos los bandidos estan muertos
    bandidos_vivos = 0
    for bandido in bandidos:
        if bandido.vivo == True:
            bandidos_vivos += 1

    if bandidos_vivos == 0:
        game_over = 1    

    #iteramos atraves de todos los eventos que ocurren
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    #actualizamos todas las acciones/funciones
    pygame.display.update()

pygame.quit()