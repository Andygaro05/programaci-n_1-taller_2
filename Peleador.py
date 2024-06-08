from typing import Any
import pygame

pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 24)
negro = (0,0,0)
rojo = (255,0,0)
verde = (0,255,0)
damage_text_group = pygame.sprite.Group()

class Personaje:
    def __init__(self, x, y, name, vida_max, fuerza, defensa, pociones):
        self.name = name
        self.vida_max = vida_max
        self.hp = vida_max
        self.fuerza = fuerza
        self.defensa = defensa
        self.pociones = pociones
        self.inventario =[]
        self.vivo = True
        #obtenemos el tiempo
        self.update_time = pygame.time.get_ticks()
        
        #creamos la lista que contendra los sprites para simular animación
        self.animation_list = []
        self.action = 0 #0 idle, 1:caminar, 2:atacar, 2:herido, 3:lastimado, 4:muerto
        self.frame_index = 0

        #cargar imagenes idle
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(3):
            #insertamos la images
            img = pygame.image.load(f"img/caballero/idle/knight 3 idle ({i}).png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #cargar imagenes caminando
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(7):
            #insertamos la images
            img = pygame.image.load(f"img/caballero/walk/knight walk ({i}).png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #cargar imagenes ataque
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(9):
            #insertamos la images
            img = pygame.image.load(f"img/caballero/attack/knight 3 attack ({i}).png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #cargar imagenes bloqueo
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(9):
            #insertamos la images
            img = pygame.image.load(f"img/caballero/block/knight 3 block ({i}).png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)
        
        #cargar cuando muere
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(8):
            #insertamos la images
            img = pygame.image.load(f"img/caballero/death/knight death ({i}).png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]

        #creamos la hitbox
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def death(self):
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def attack(self, objetivo):
        #efectuar daño al objetivo
        damage = self.fuerza - objetivo.defensa
        objetivo.hp -= damage
        damage_text = DamageText(objetivo.rect.centerx, objetivo.rect.y, str(damage), rojo)
        damage_text_group.add(damage_text)
        objetivo.lastimado()

        #si el jugador muere
        if objetivo.hp <1:
            objetivo.hp = 0
            objetivo.vivo = False

        #configurar animación de ataque
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def lastimado(self):
        #configurar animación de daño
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def idle(self):
        #configurar animación idle
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self):
        animation_cooldown = 200
            #obtenemos la imagen acutal
        self.image = self.animation_list[self.action][self.frame_index]

        #   si el tiempo entre el ultimo update y el cd de la animación es mayor muestra la siguiente imagen
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            #si la animación sobrepasa el tamaño del vector reinicia
            if self.frame_index >= len(self.animation_list[self.action]):
                self.idle()
            if self.hp < 1:
                self.lastimado()
                self.death()
                #self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

#subclase ligero
class Ligero(Personaje):

    def __init__(self, x, y, name, pociones):
        # Se heredan los valores iniciales del padre
        super().__init__(x, y, name, vida_max=100, fuerza=60, defensa=5, pociones=pociones)
        self.name = name
        self.vida_max = self.vida_max
        self.hp = self.vida_max
        self.pociones = pociones
        self.vivo = True

        #obtenemos el tiempo
        self.update_time = pygame.time.get_ticks()
        
        #creamos la lista que contendra los sprites para simular animación
        self.animation_list = []
        self.action = 0 #0 idle, 1:atacar, 2:herido, 3:recuperación, 4:muerto
        self.frame_index = 0

        #cargar imagenes idle
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(3):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Ligero/Combat Idle/LightBandit_Combat Idle_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #cargar imagenes de ataque
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(7):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Ligero/Attack/LightBandit_Attack_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        # Cuando lo lastiman
        temp_list = []  # Almacenamos la acción que está realizando
        for i in range(2):  # Iteramos para cargar 2 imágenes
            img = pygame.image.load(f"img/bandidos/Ligero/Hurt/LightBandit_Hurt_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))  # Escalamos la imagen
            temp_list.append(self.image)  # Agregamos la imagen a la lista
        self.animation_list.append(temp_list)  # Agregamos la lista de imágenes a la lista principal de animaciones

        #cargar imagenes recuperación
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(7):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Ligero/Recover/LightBandit_Recover_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #mostrar imagenes cuando muere
        temp_list = []  #almacenamos la acción que esta realizando
        img = pygame.image.load(f"img/bandidos/Ligero/Death/LightBandit_Death_{0}.png").convert_alpha()  # Cargamos solo la imagen en el índice 0
        self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))  # Escalamos la imagen
        temp_list.append(self.image)  # Agregamos la imagen a la lista
        self.animation_list.append(temp_list)  # Agregamos la lista de imágenes a la lista principal de animaciones

        self.image = self.animation_list[self.action][self.frame_index]

        #creamos la hitbox
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def attack(self, objetivo):
        #efectuar daño al objetivo
        damage = self.fuerza - objetivo.defensa
        objetivo.hp -= damage
        damage_text = DamageText(objetivo.rect.centerx, objetivo.rect.y, str(damage), rojo)
        damage_text_group.add(damage_text)
        objetivo.lastimado()

        #si el jugador muere
        if objetivo.hp <1:
            objetivo.hp = 0
            objetivo.vivo = False

        #configurar animación de ataque
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def idle(self):
        #configurar animación idle
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        #configurar animación de muerte
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def lastimado(self):
        #configurar animación de daño
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self):
        animation_cooldown = 200
            #obtenemos la imagen acutal
        self.image = self.animation_list[self.action][self.frame_index]

        #   si el tiempo entre el ultimo update y el cd de la animación es mayor muestra la siguiente imagen
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            #si la animación sobrepasa el tamaño del vector reinicia
            if self.frame_index >= len(self.animation_list[self.action]):
                self.idle()
            if self.hp < 1:
                self.lastimado()
                self.death()
                #self.kill()


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Redefinir métodos si es necesario (ataque, recibir_ataque, etc.)
#subclase pesado:
class Pesado(Personaje):

    def __init__(self, x, y, name, pociones):
        # Se heredan los valores iniciales del padre
        super().__init__(x, y, name, vida_max=300, fuerza=20, defensa=20, pociones=pociones)
        self.name = name
        self.vida_max = self.vida_max
        self.hp = self.vida_max
        self.pociones = pociones
        self.vivo = True

        #obtenemos el tiempo
        self.update_time = pygame.time.get_ticks()
        
        #creamos la lista que contendra los sprites para simular animación
        self.animation_list = []
        self.action = 0  #0 idle, 1:atacar, 2:herido, 3:lastimado, 4:recuperación, 5:muerto
        self.frame_index = 0

        #cargar imagenes idle
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(3):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/Combat idle/HeavyBandit_CombatIdle_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)
        
        #cargar imagenes de ataque
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(7):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/Attack/HeavyBandit_Attack_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #cuando lo lastiman
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(2):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/Hurt/HeavyBandit_Hurt_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #cargar imagenes recuperación
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(7):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/Recover/HeavyBandit_Recover_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)

        #cargar imagenes cuando muere
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(1):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/Death/HeavyBandit_Death_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        
        #creamos la hitbox
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def attack(self, objetivo):
        #efectuar daño al objetivo
        damage = self.fuerza - objetivo.defensa
        objetivo.hp -= damage
        damage_text = DamageText(objetivo.rect.centerx, objetivo.rect.y, str(damage), rojo)
        damage_text_group.add(damage_text)
        objetivo.lastimado()

        #si el jugador muere
        if objetivo.hp <1:
            objetivo.hp = 0
            objetivo.vivo = False
            objetivo.death()
        
        
        #configurar animación de ataque
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        
    def idle(self):
        #configurar animación idle
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def lastimado(self):
        #configurar animación de daño
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def death(self):
        #configurar animación de muerte
        self.action = 4
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.vivo = False

    def update(self):
        animation_cooldown = 200
            #obtenemos la imagen acutal
        self.image = self.animation_list[self.action][self.frame_index]

        #   si el tiempo entre el ultimo update y el cd de la animación es mayor muestra la siguiente imagen
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            #si la animación sobrepasa el tamaño del vector reinicia
            if self.frame_index >= len(self.animation_list[self.action]):
                self.idle()
            if self.hp < 1:
                self.lastimado()
                self.death()
                #self.kill()


    def draw(self, screen):
        screen.blit(self.image, self.rect)


    # Redefinir métodos si es necesario (ataque, recibir_ataque, etc.)

""""Creamos una clase con la barra de vida
Seran 2 cuadrados uno rojo y verde, que cambiaran según
el daño recibido"""

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, screen, hp):
        #actualizar con la salud actual
        self.hp = hp
        #controlar el tamaño del rectangulo verde
        ratio = self.hp/self.max_hp
        # Dibujar la barra de vida
        pygame.draw.rect(screen, rojo, (self.x, self.y, 150, 20))#posición en X y Y
        pygame.draw.rect(screen, verde, (self.x, self.y, 150*ratio, 20))

    
class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(damage), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        #borrar el texto tras unos segundos
        self.counter += 1
        if self.counter > 30:
            self.kill()