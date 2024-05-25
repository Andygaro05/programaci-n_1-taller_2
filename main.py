import pgzrun

# Define la imagen de la nave espacial
nave = Actor("nave.png")  # Reemplaza "nave.png" con el nombre de archivo real de tu imagen

# Define la posición inicial de la nave espacial
nave.pos = 600, 600

# Define el ancho y alto de la pantalla
WIDTH = 1200
HEIGHT = 1000

# Define la velocidad de movimiento de la nave espacial
velocidad = 5

# Define el color de fondo
fondo = "blue"

def draw():
    # Limpia la pantalla
    screen.clear()

    # Dibuja el fondo
    screen.fill(fondo)

    # Dibuja la nave espacial en su posición actual
    nave.draw()

def update():
    # Detecta las teclas presionadas
    if keyboard.left:
        nave.x -= 1
    elif keyboard.right:
        nave.x += 1
    elif keyboard.up:
        nave.y -= 1
    elif keyboard.down:
        nave.y += 1

    # Limita la posición de la nave espacial dentro de la pantalla
    nave.x = max(0, min(nave.x, WIDTH - nave.width))
    nave.y = max(0, min(nave.y, HEIGHT - nave.height))

# Inicia el juego
pgzrun.go()