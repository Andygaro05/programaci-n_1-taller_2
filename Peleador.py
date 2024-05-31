import pygame
import time

class Personaje:
    def __init__(self, x, y, name, vida_max, fuerza, defensa):
        self.name = name
        self.vida_max = vida_max
        self.hp = vida_max
        self.fuerza = fuerza
        self.defensa = defensa
        self.inventario =[]
        self.vivo = True
        #obtenemos el tiempo
        self.update_time = pygame.time.get_ticks()
        
        #creamos la lista que contendra los sprites para simular animación
        self.animation_list = []
        self.action = 0 #0 idle, 1:atacar, 2:herido, 3:lastimado, 4:muerto
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

    def update(self):
        animation_cooldown = 100
        #obtenemos la imagen acutal
        self.image = self.animation_list[self.action][self.frame_index]

        #si el tiempo entre el ultimo update y el cd de la animación es mayor muestra la siguiente imagen
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            time.sleep(0.125)
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #si la animación sobrepasa el tamaño del vector reinicia
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)


#clase base enemigo
class Enemigo(Personaje):
    def __init__(self, x, y, name, vida_max, fuerza, defensa):
        super().__init__(x, y, name, vida_max, fuerza, defensa)

        self.name = name
        self.vida_max = vida_max
        self.hp = vida_max
        self.fuerza = fuerza
        self.defensa = defensa
        self.experiencia = 10  # Experiencia otorgada al derrotarlo
        self.vivo = True    

    def atacar(self, objetivo):
        # Implementar lógica de ataque para enemigos
        pass

    def recibir_ataque(self, daño):
        # Implementar lógica para recibir daño, considerando la defensa
        pass

    def soltar_recompensa(self):
        # Implementar lógica para soltar recompensas aleatorias
        pass

#subclase ligero
class Ligero(Enemigo):

    def __init__(self, x, y, name):
        # Se heredan los valores iniciales del padre
        super().__init__(x, y, name, vida_max=50, fuerza=15, defensa=5)
        self.name = name
        self.hp = self.vida_max
        self.inventario =[]
        self.vivo = True

        #obtenemos el tiempo
        self.update_time = pygame.time.get_ticks()
        
        #creamos la lista que contendra los sprites para simular animación
        self.animation_list = []
        self.action = 0 #0 idle, 1:atacar, 2:herido, 3:lastimado, 4:recuperación, 5:muerto
        self.frame_index = 0

        #cargar imagenes idle
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(3):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Ligero/idle/LightBandit_Idle_{i}.png").convert_alpha()
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

    def update(self):
        animation_cooldown = 100
        #obtenemos la imagen acutal
        self.image = self.animation_list[self.action][self.frame_index]

        #si el tiempo entre el ultimo update y el cd de la animación es mayor muestra la siguiente imagen
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            time.sleep(0.125)
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #si la animación sobrepasa el tamaño del vector reinicia
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Redefinir métodos si es necesario (ataque, recibir_ataque, etc.)


#subclase pesado:
class Pesado(Enemigo):

    def __init__(self, x, y, name):
        # Se heredan los valores iniciales del padre
        super().__init__(x, y, name, vida_max=100, fuerza=10, defensa=20)
        self.name = name
        self.hp = self.vida_max
        self.inventario =[]
        self.vivo = True

        #obtenemos el tiempo
        self.update_time = pygame.time.get_ticks()
        
        #creamos la lista que contendra los sprites para simular animación
        self.animation_list = []
        self.action =  #0 idle, 1:atacar, 2:herido, 3:lastimado, 4:recuperación, 5:muerto
        self.frame_index = 0
        
        #cargar imagenes de ataque
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(7):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/Attack/HeavyBandit_Attack_{i}.png").convert_alpha()
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

        #cuando lo lastiman
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(2):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/Hurt/HeavyBandit_Hurt_{i}.png").convert_alpha()
            self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
            temp_list.append(self.image)
        self.animation_list.append(temp_list)
        
        #cargar imagenes idle
        temp_list = []  #almacenamos la acción que esta realizando
        for i in range(3):
            #insertamos la images
            img = pygame.image.load(f"img/bandidos/Pesado/idle/HeavyBandit_Idle_{i}.png").convert_alpha()
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

        #mostrar imagenes cuando muere
        temp_list = []  #almacenamos la acción que esta realizando
        img = pygame.image.load(f"img/bandidos/Pesado/Death/HeavyBandit_Death_{0}.png").convert_alpha()  # Cargamos solo la imagen en el índice 0
        self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))  # Escalamos la imagen
        temp_list.append(self.image)  # Agregamos la imagen a la lista
        self.animation_list.append(temp_list)  # Agregamos la lista de imágenes a la lista principal de animaciones
        self.image = self.animation_list[self.action][self.frame_index]
        
        #creamos la hitbox
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        animation_cooldown = 100
        #obtenemos la imagen acutal
        self.image = self.animation_list[self.action][self.frame_index]

        #si el tiempo entre el ultimo update y el cd de la animación es mayor muestra la siguiente imagen
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            time.sleep(0.125)
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #si la animación sobrepasa el tamaño del vector reinicia
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    # Redefinir métodos si es necesario (ataque, recibir_ataque, etc.)
