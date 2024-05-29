import pygame

class Personaje:
    def __init__(self, x, y, name, vida_max, fuerza, defensa):
        self.name = name
        self.vida_max = vida_max
        self.hp = vida_max
        self.fuerza = fuerza
        self.defensa = defensa
        self.inventario =[]

        #validamos que la entidad esta viva
        self.vivo = True    
        #insertamos la image
        img = pygame.image.load("img/caballero/idle/knight 3 idle (0).png").convert_alpha()
        self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
        #creamos la hitbox
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


#clase base
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
        self.hp = self.vida_max
        #insertamos la image
        img = pygame.image.load("img/bandidos/Ligero/Combat Idle/LightBandit_Combat Idle_0.png").convert_alpha()
        self.image = pygame.transform.scale(img, (img.get_width()*6, img.get_height()*6))
        #creamos la hitbox
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        def draw(self, screen):
            screen.blit(self.image, self.rect)

    # Redefinir métodos si es necesario (ataque, recibir_ataque, etc.)


#subclase pesado:
class Pesado(Enemigo):

    def __init__(self, x, y, name):
        # Se heredan los valores iniciales del padre
        super().__init__(x, y, name, vida_max=100, fuerza=10, defensa=20)

    # Redefinir métodos si es necesario (ataque, recibir_ataque, etc.)
