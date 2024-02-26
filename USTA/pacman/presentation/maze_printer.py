def print_maze(MAZE: list[list[str]]):
    for line in MAZE:
        for ch in line:
            icon = ""
            if int(ch) == 0:
                icon = "  "
            elif int(ch) == 1:
                icon = "🧱"
            elif int(ch) == 2:
                icon = "👻"
            elif int(ch) == 3:
                icon = " ."
            print(icon, end="")

        print("")
