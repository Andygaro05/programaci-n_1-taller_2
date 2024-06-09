import pygame
from Peleador import *
from boton import Button

pygame.init()

clock = pygame.time.Clock()  # Optimizar cada cuanto refresca
FPS = 60  # Frames por segundo

# Pantalla de juego
PANEL_BAJO = 150
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 675 + PANEL_BAJO

# Inicializa la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("World of Fantasy")  # Nombre del juego

# Variables de juego
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
clicked = False
pocion = False
efecto_pocion = 20  # La poción sana de a 20 de salud
game_over = 0
game_paused = True
menu_state = "main"
victory_timer = 0

# Fuente de juego
font = pygame.font.SysFont("Times New Roman", 24)

# Definir colores
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)

# Cargamos las imágenes
fondo_img = pygame.image.load("img/fondo/fondo resize.png").convert_alpha()
panel_img = pygame.image.load("img/iconos/boton madera.png").convert_alpha()
pocion_img = pygame.image.load("img/iconos/pocion_salud.png").convert_alpha()
victoria = pygame.image.load("img/iconos/victoria.png").convert_alpha()
derrota = pygame.image.load("img/iconos/derrota.png").convert_alpha()
# Iconos para el menú
play_img = pygame.image.load("img/iconos/play.png").convert_alpha()
tienda_img = pygame.image.load("img/iconos/tienda.png").convert_alpha()
quit_img = pygame.image.load("img/iconos/salida.png").convert_alpha()
fondo_menu_img = pygame.image.load("img/fondo/fondo_menu.jpg").convert_alpha()

#fondo para la tienda
back_img = pygame.image.load("img/iconos/back.png").convert_alpha()
fondo_tienda_img = pygame.image.load("img/fondo/fondo_tienda.png").convert_alpha()
#Objetos de la tienda
pocion_fuerza_img = pygame.image.load("img/tienda/pocion_fuerza.png")
pocion_vida_img = pygame.image.load("img/tienda/pocion_vida.png")

#botones de la tienda
pocion_fuerza_button = Button(100, 100, pocion_fuerza_img, 256, 256)	
pocion_vida_button = Button(300, 100, pocion_vida_img, 256, 256)	
# Imagen de la espada para el mouse
mouse_img = pygame.image.load("img/iconos/espada mouse.png").convert_alpha()

# Botones para el menú
play_button = Button(485, 200, play_img, 240, 111)
tienda_button = Button(500, 325, tienda_img, 215, 102)
quit_button = Button(500, 550, quit_img, 215, 115)
back_button = Button(500, 400, back_img, 193, 105)

# Función para dibujar texto
def dibujar_texto(texto, font, text_col, x, y):
    img = font.render(texto, True, text_col)
    screen.blit(img, (x, y))

# Para mostrar el fondo
def dibujar_fondo(fondo):
    screen.blit(fondo, (0, 0))

def dibujar_panel():
    screen.blit(panel_img, (0, SCREEN_HEIGHT - PANEL_BAJO))  # El panel solo ocupa la parte baja de la pantalla

    # Mostrar stats del caballero
    dibujar_texto(f"{Caballero.name} HP: {Caballero.hp}", font, negro, 100, SCREEN_HEIGHT - PANEL_BAJO + 10)

    # Mostrar stats bandidos
    for count, i in enumerate(bandidos):
        # Mostrar nombre y vida
        dibujar_texto(f"{i.name} HP: {i.hp}", font, negro, 800, (SCREEN_HEIGHT - PANEL_BAJO + 10) + count * 60)

# Creamos las instancias de los personajes
Caballero = Personaje(400, 560, "Caballero", 150, 50, 10, 3)
ligero1 = Ligero(800, 530, "Bandido Ligero", 1)
pesado1 = Pesado(1000, 530, "Enemigo Pesado", 3)

bandidos = []
bandidos.append(ligero1)
bandidos.append(pesado1)

# Creamos las barras de vida
barra_vida_caballero = HealthBar(100, SCREEN_HEIGHT - PANEL_BAJO + 40, Caballero.hp, Caballero.vida_max)
barra_vida_ligero1 = HealthBar(800, SCREEN_HEIGHT - PANEL_BAJO + 40, ligero1.hp, ligero1.vida_max)
barra_vida_pesado1 = HealthBar(800, SCREEN_HEIGHT - PANEL_BAJO + 100, pesado1.hp, pesado1.vida_max)

# Creamos los botones
boton_pocion = Button(100, SCREEN_HEIGHT - PANEL_BAJO + 70, pocion_img, 64, 64)

# Función para reiniciar enemigos
def reiniciar_personajes():
    for bandido in bandidos:
        bandido.hp = bandido.vida_max
        bandido.vivo = True
        bandido.pociones = 3
    Caballero.hp = Caballero.vida_max

# Validamos que el juego se esté ejecutando
run = True
while run:
    clock.tick(FPS)  # Optimizar la tasa de actualización

    # Iteramos a través de todos los eventos que ocurren
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = not game_paused  # Alternar el estado de pausa

        if event.type == pygame.QUIT:
            run = False

    if game_paused:

        if menu_state == "main":
            dibujar_fondo(fondo_menu_img)

            if play_button.draw(screen):
                game_paused = False

            if tienda_button.draw(screen):
                menu_state = "tienda"

            if quit_button.draw(screen):
                run = False
        if menu_state == "tienda":
            screen.fill((128, 128, 128))
            dibujar_fondo(fondo_tienda_img)
            dibujar_texto(f"Experiencia: {Caballero.xp}", pygame.font.SysFont("Cascadia Mono SemiBold", 64), negro, 50, 50)
            dibujar_texto("Costo: 30 xp", pygame.font.SysFont("Cascadia Mono SemiBold", 32), verde, 165, 300)
            dibujar_texto("5pts más de vida", pygame.font.SysFont("Cascadia Mono SemiBold", 32), verde, 150, 140)
            dibujar_texto("Costo: 20 xp", pygame.font.SysFont("Cascadia Mono SemiBold", 32), verde, 365, 300)
            dibujar_texto("Poción de vida", pygame.font.SysFont("Cascadia Mono SemiBold", 32), verde, 365, 140)
            pocion_vida_button.draw(screen)
            pocion_fuerza_button.draw(screen)

            if pocion_fuerza_button.clicked:
                if Caballero.xp >= 30:
                    Caballero.xp -= 30
                    Caballero.vida_max += 5 

            if pocion_vida_button.clicked:
                if Caballero.xp >= 20:
                    Caballero.xp -= 20
                    Caballero.pociones += 1

            if back_button.draw(screen):
                menu_state = "main"
    else:
        # Dibujar el fondo, panel y caballero
        dibujar_fondo(fondo_img)
        dibujar_panel()
        barra_vida_caballero.draw(screen, Caballero.hp)
        barra_vida_ligero1.draw(screen, ligero1.hp)
        barra_vida_pesado1.draw(screen, pesado1.hp)

        # Dibujamos el estado actual del caballero
        Caballero.update()
        Caballero.draw(screen)
        # Iteramos la lista de enemigos
        for bandido in bandidos:
            bandido.update()
            bandido.draw(screen)

        # Dibujar el daño
        damage_text_group.update()
        damage_text_group.draw(screen)

        # Controlar las acciones del jugador
        # Reset las acciones
        attack = False
        objetivo = None
        pocion = False
        pos = pygame.mouse.get_pos()

        # Permitimos la visualización del mouse
        pygame.mouse.set_visible(True)

        # Si tocamos la hitbox de un enemigo, cambiar el cursor a espada
        for count, bandido in enumerate(bandidos):
            if bandido.rect.collidepoint(pos):
                # Ocultamos el mouse
                pygame.mouse.set_visible(False)
                # Mostramos la espada
                screen.blit(mouse_img, pos)
                # Si se presiona el mouse, atacamos al objetivo
                if clicked and bandido.vivo:
                    attack = True
                    objetivo = bandidos[count]

        if boton_pocion.draw(screen):
            pocion = True

        # Mostrar las pociones restantes
        dibujar_texto(str(Caballero.pociones), font, rojo, 150, SCREEN_HEIGHT - PANEL_BAJO + 110)

        # Validamos que el juego no haya finalizado
        if game_over == 0:
            # Acción del jugador
            if Caballero.vivo:
                if current_fighter == 1:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        # Buscar acción de jugador
                        # Atacar
                        if attack and objetivo:
                            Caballero.attack(objetivo)
                            current_fighter += 1
                            action_cooldown = 0

                        # Poción
                        if pocion:
                            if Caballero.pociones > 0:
                                # Validar para evitar overhealth
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

            # Acciones de los enemigos
            for count, bandido in enumerate(bandidos):
                if current_fighter == 2 + count:
                    if bandido.vivo:
                        action_cooldown += 1
                        if action_cooldown >= action_wait_time:
                            # Comprobamos si el bandido puede usar poción
                            if (bandido.hp / bandido.vida_max) < 0.5 and bandido.pociones > 0:
                                # Validar que no haya overhealth
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
                                current_fighter += 1  # Cambia de turno
                                action_cooldown = 0  # Reinicia el cd de cada acción
                    else:
                            bandido.death()
                            Caballero.xp += 10
                            print(Caballero.xp)
                            current_fighter += 1

            # Si todos los enemigos ya usaron su movida
            if current_fighter > total_fighters:
                current_fighter = 1

        # Validamos si game over
        elif game_over != 0:
            if game_over == 1:
                screen.blit(victoria, (300, 100))
                victory_timer += 1
                if victory_timer > FPS * 5:  # 5 segundos
                    game_paused = True
                    menu_state = "main"
                    game_over = 0
                    victory_timer = 0
                    reiniciar_personajes()  # Reiniciar enemigos después de victoria
            else:
                screen.blit(derrota, (360, 250))
                victory_timer += 1
                if victory_timer > FPS * 5:  # 5 segundos
                    game_paused = True
                    menu_state = "main"
                    game_over = 0
                    victory_timer = 0
                    reiniciar_personajes()  # Reiniciar enemigos después de derrota

        # Validar si todos los bandidos están muertos
        bandidos_vivos = 0
        for bandido in bandidos:
            if bandido.vivo:
                bandidos_vivos += 1

        if bandidos_vivos == 0:
            game_over = 1

    # Actualizamos todas las acciones/funciones
    pygame.display.update()

pygame.quit()
