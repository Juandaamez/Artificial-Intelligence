# Juan David Amezquita Nuñez
from logic import *

# Definimos los símbolos para las casillas y los jugadores
X, O, VACIO = Symbol("X"), Symbol("O"), Symbol(".")
casillas = [Symbol(f"c{i}") for i in range(9)]


# Función para imprimir el tablero
def mostrar_tablero(tablero):
    print("\n")
    print("     |     |     ")
    print(f"  {tablero[0]}  |  {tablero[1]}  |  {tablero[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {tablero[3]}  |  {tablero[4]}  |  {tablero[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {tablero[6]}  |  {tablero[7]}  |  {tablero[8]}  ")
    print("     |     |     ")
    print("\n")


# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for (x, y, z) in combinaciones_ganadoras:
        if tablero[x] == tablero[y] == tablero[z] == jugador:
            return True
    return False


# Función principal para jugar al tic-tac-toe
def jugar_gato():
    tablero = [VACIO for _ in range(9)]
    turno_jugador = 'X'

    for _ in range(9):
        mostrar_tablero(tablero)
        print(f"Turno del jugador {turno_jugador}")

        casilla = int(input("Elige una casilla (1-9): ")) - 1
        if tablero[casilla] != VACIO:
            print("La casilla ya está ocupada, elige otra.")
            continue

        tablero[casilla] = turno_jugador

        if verificar_ganador(tablero, turno_jugador):
            mostrar_tablero(tablero)
            print(f"¡Ha ganado el jugador {turno_jugador}!")
            return

        turno_jugador = 'O' if turno_jugador == 'X' else 'X'

    mostrar_tablero(tablero)
    print("¡Es un empate!")


# Ejecutar el juego
if __name__ == "__main__":
    jugar_gato()
