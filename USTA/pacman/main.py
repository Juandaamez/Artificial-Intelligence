import os
from utils.maze_reader import read_maze_file
from presentation.maze_printer import print_maze
from time import sleep
import threading

MAZE = read_maze_file()


def update_frame():
    i = 0
    while True:
        i += 1
        print_maze(MAZE)
        print(i)
        sleep(0.2)
        os.system("clear")


print_thread = threading.Thread(target=update_frame)

print_thread.start()
