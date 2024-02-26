import time

class Pacman:
    def __init__(self,x ,y):
        self._x = x
        self._y = y
        self._image = '😒'

    def show(self):
        for _ in range(self._x):
            print()
        print(" " * self._y, end='')
        print(self._image)

class Game:
    def __init__(self, timer):
        self._timer = timer

    def clear_screen(self):
        print('\033c')

    def run(self):     
        pac = Pacman(0, 40)
        while True:
            self.clear_screen()
            pac.show()
            pac._y += 1
            pac._x += 1
            time.sleep(self._timer)
            

pacman_game = Game(0.5)
pacman_game.run()
