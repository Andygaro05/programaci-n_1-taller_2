# **¡Bienvenido a World of Fantasy!**
Este proyecto en Python te permite ejecutar un juego basado en combate por turnos, donde tu eres el caballero que está encargado de derrotar y matar a un grupo de bandidos, conformado por dos enemigos ligeros, y su jefe, los cuales van a tratar de eliminarte a toda costa para seguir comentiendo sus maldades.

## **Controles:**
- Click izquierdo sobre el enemigo para atacar con tu espada.
- Barra espaciadora para pausar el juego y poder acceder al menú principal.

## **Funcionalidades:**

### **Clases Principales:**

```Personaje```
Esta clase representa un personaje en el juego. Cada personaje tiene varias propiedades y métodos para gestionar su comportamiento y animaciones.

- Propiedades:

    - ```name```: Nombre del personaje.
    - ```vida_max```: Vida máxima del personaje.
    - ```hp```: Vida actual del personaje.
    - ```fuerza```: Fuerza del personaje.
    - ```defensa```: Defensa del personaje.
    - ```pociones```: Número de pociones que tiene el personaje.
    - ```xp```: Experiencia del personaje.
    - ```monedas```: Monedas que posee el personaje.
    - ```inventario```: Lista de ítems en el inventario del personaje.
    - ```vivo```: Estado del personaje (vivo o muerto).
    - ```animation_list```: Lista de animaciones del personaje.
    - ```action```: Acción actual del personaje (idle, caminar, atacar, herido, lastimado, muerto).
    - ```frame_index```: Índice de la animación actual.
    - ```rect```: Hitbox del personaje.

- Métodos:

    - ```__init__(self, x, y, name, vida_max, fuerza, defensa, pociones)```: Inicializa un nuevo personaje con sus atributos y carga las animaciones.
    - ```death(self)```: Configura la animación de muerte.
    - ```attack(self, objetivo)```: Realiza un ataque al objetivo, calcula el daño y actualiza la animación.
    - ```lastimado(self)```: Configura la animación de daño recibido.
    - ```idle(self)```: Configura la animación idle.
    - ```update(self)```: Actualiza la animación del personaje.
    - ```draw(self, screen)```: Dibuja el personaje en la pantalla.

### **Subclases**
```Ligero```:
Hereda de Personaje y representa un tipo específico de personaje con menor vida y defensa, pero mayor fuerza de ataque.

```Pesado```
Hereda de Personaje y representa un tipo específico de personaje con mayor vida y defensa, pero menor fuerza de ataque.

### **Clases Adicionales**
```HealthBar```:
Representa la barra de vida de los personajes.

- Propiedades:

    - ```x, y```: Coordenadas de la barra de vida.
    - ```hp```: Vida actual.
    - ```max_hp```: Vida máxima.

- Métodos:

    - ```draw(self, screen, hp)```: Dibuja la barra de vida en la pantalla.
    

```DamageText```:
Representa el texto que muestra el daño infligido.

- Propiedades:

    - ```rect```: Rectángulo del texto.
    - ```counter```: Contador para eliminar el texto tras un tiempo.

- Métodos:

    - ```__init__(self, x, y, damage, color)```: Inicializa el texto con el daño infligido.
    - ```update(self)```: Actualiza la posición del texto y lo elimina tras un tiempo.


### **Sistema de tienda**
Con cada enemigo que derrotes vas a obtener 10 puntos de experiencia, los cuales podrás intercambiar por dos pociones especiales:
- Poción de vida: Regenera 20 puntos de vida. Costo 20xp
- Poción de aumento de nivel: Al comprarla aumentas de nivel, y con eso, tambien aumenta tu vida en 5 puntos de vida, por lo que tu vida máxima aumenta en 5 puntos. Costo 30xp

## **Instalación:**
### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local usando el siguiente comando:
```bash
git clone https://github.com/Andygaro05/programaci-n_1-taller_2.git
```

### 2. Cambiar al directorio del juego

Ahora, para que carguen todos los recursos y que el juego funcione perfectamente, cambiaremos al directorio del juego:
```bash
cd programaci-n_1-taller_2
```

### 3. Ejecutar el juego

Finalmente, para ejecutar el programa escribiremos este comando:

```bash
python main.py
```


###**La aventura te espera ¡Buena suerte impidiendo que los bandidos se salgan con la suya!**
![Juego](https://paste.c-net.org/PamphletPlatter)