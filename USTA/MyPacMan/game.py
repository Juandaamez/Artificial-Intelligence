#Author: Juan David Amezquita Nuñez

import time
import random
import os

class Map:
    def __init__(self, archive):
        self.archive = archive
        self.maze = None

    def load_map(self):
        with open(self.archive, 'r') as file:
            self.maze = [list(line.replace('1', '🧱').replace('0', '⬜').strip()) for line in file.readlines()]

    def is_wall(self, x, y):
        return self.maze[x][y] == '🧱'

    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in self.maze:
            print(''.join(line))

class Entity:
    def __init__(self, x, y, image, game_map):
        self.x = x
        self.y = y
        self.prev_x = x
        self.prev_y = y
        self.image = image
        self.game_map = game_map

    def move(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, abajo, izquierda, arriba
        random.shuffle(directions)  # Aleatoriza las direcciones para movimiento variado

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if not self.game_map.is_wall(new_x, new_y) and not self.is_occupied(new_x, new_y):
                # Limpiar la posición anterior
                self.game_map.maze[self.prev_x][self.prev_y] = '⬜'
                # Actualizar a la nueva posición
                self.x = new_x
                self.y = new_y
                self.prev_x = self.x
                self.prev_y = self.y
                return  # Salir después de moverse

        # Si no se puede mover en ninguna dirección, permanece en su lugar (puede ocurrir en un rincón)

    def is_occupied(self, x, y):
        # Verifica si la posición está ocupada por otro personaje
        return self.game_map.maze[x][y] in ['😁', '👻']

    def show(self):
        self.game_map.maze[self.x][self.y] = self.image

class Pacman(Entity):
    pass

class Ghost(Entity):
    pass

class Game:
    def __init__(self, timer, game_map):
        self.timer = timer
        self.game_map = game_map
        self.pacman = None
        self.ghosts = []

    def run(self):
        self.game_map.load_map()

        self.pacman = Pacman(1, 1, '😁', self.game_map)
        self.ghosts = [Ghost(1, 3, '👻', self.game_map) for _ in range(4)]

        while True:
            self.game_map.show()
            self.pacman.move()  # Actualizado para no pasar parámetros
            self.pacman.show()

            for ghost in self.ghosts:
                ghost.move()  # Actualizado para no pasar parámetros
                ghost.show()

            time.sleep(self.timer)

game_map = Map('maze.txt')
pacman_game = Game(0.5, game_map)
pacman_game.run()
