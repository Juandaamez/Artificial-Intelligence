def read_maze_file() -> list:
    maze: list[list[str]]
    with open("data/maze.txt") as lines:
        maze = [line.strip().split() if line != "\n" else "" for line in lines]

    return maze
