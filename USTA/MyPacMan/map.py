#Author: Juan David Amezquita Nuñez

import os
import time

def map():
    # Abre el archivo maze.txt en modo de lectura
    with open('maze.txt', 'r') as file:
        # Lee el contenido del archivo
        maze = file.read()

    # Reemplaza todos los '1' por muro
    maze = maze.replace('1', '🧱')

    # Reemplaza todos los '0' por camino blanco
    maze = maze.replace('0', '⬜')

    print(maze)

map()

