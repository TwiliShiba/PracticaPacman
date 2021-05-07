# Andres Yarte
# A00829535
# Reflexión - que aprendimos
# Mayo 6 2021

# Se le hace import a todas las librerias al inicio
from random import choice
from turtle import *
from freegames import floor, vector

# almacena el score - cantidad de galletas comidas por pacman
state = {'score': 0}

# hace invisible -> creando 2 objetos de clase turtle
path = Turtle(visible=False)
writer = Turtle(visible=False)

# Direccion del pacman iual a snake
aim = vector(5, 0)

# Crea pacman en la posición (-40,-80)
pacman = vector(-40, -80)

# lista de listas de la posicion y direccion de cada fantasma
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
# Lista del tablero
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# Dibuja un square con su esq/ inf. isquierda (x,y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

#
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# retornar True si point es un tile valido
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)
    
    # si la celda es 0 return False - pared
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    # si la celda es 0 return False - pared
    if tiles[index] == 0:
        return False

    # return True ?
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')
    # Recorre toda la lista de (tiles)
    for index in range(len(tiles)):
        # Extrae el valor que existe en la posicion index
        tile = tiles[index]
        
        # si el valor es 1
        if tile > 0:
            # calcula la x, y donde se dibuja el square
            x = (index % 20) * 20 - 200 # si el index es (21%20)*20 - 200 = 180
            y = 180 - (index // 20) * 20 # 180 - (21//20) * 20 = 160
            square(x, y) # dibuja el square(-180, 160)(-160, 160)

            # Dibuja la galleta sobre el square en el centro
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10) # el +10 es para que este en el centro del cubo la galleta. los cubos son de 20 * 20
                path.dot(8, 'white')

def move():
    
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])
    
    # limpia la ventana
    clear()
    
    # si es una posición valida para el pacman incrementa move en esa direccion
    if valid(pacman + aim):
        pacman.move(aim)

    # retorna la posicion del pacman en el tablero
    index = offset(pacman)

    # 1 - camino
    if tiles[index] == 1:
        # a esa posicion le asigna 2 - comer la galleta
        tiles[index] = 2
        # se incrementa el score
        state['score'] += 1
        # calcula la pocición x,y del pacman
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        # dibujar el square - sin la galleta
        square(x, y)

    up()
    # se va a la posicion del pacman
    goto(pacman.x + 10, pacman.y + 10)
    # dibuja el pacman
    dot(20, 'yellow')

    # [vector (-180, 160), vector(5,0)]
    colores = ['red','green','#bebebe','white'] 
    k = 0
    for point, course in ghosts:
        # valida si el fantasma poin se puede mover en course
        if valid(point + course):
            point.move(course)
        else: # si no se puede mover el fantasma en esa dirección
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            #quitar opciones y choice
            # cond. de pacman y point 
            # actualizar el course.x y .y de cada 
            # plan guarda la nueva dirección del fantasma
            # AQUI ES DONDE USTEDES VAN A HACER LOS FANTASMAS MAS INTELIGENTES
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, colores[k])
        k = k + 1

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            writer.goto(-120,10)
            writer.write('GAME OVER', font=('Arial',30,'normal'))
            return
    #vuelve a llamar la fucnion dentro de 100 milisegundos
    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# inicializa la ventana ancho y alto 420,420
# 0,0 indica la ubicacion de la esquina superior isq. de la ventana en mi pantalla
setup(420, 420, 370, 0)
# esconde la turtle (la flecha)
hideturtle()
# oculta toda la forma de dibujar
tracer(False)
# mueve la turtle writer a la posicion 160, 160
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
# Activar, escuchar los eventos del teclado
listen()
# en caso de que el usuario oprima la indicada
# llama a la funcion change con los argumentos indicados
# que indican la nueva direccion del pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')

world()
move()
done()