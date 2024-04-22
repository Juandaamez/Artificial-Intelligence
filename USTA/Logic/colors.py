from logic import *

# Suponiendo que tenemos 4 posiciones para los colores
positions = range(1, 5)
colors = ['red', 'blue', 'green', 'yellow']

# Crear símbolos para cada color en cada posición
symbols = {color: {position: Symbol(f"{color}{position}") for position in positions} for color in colors}

# Crear la base de conocimientos
KB = And()

# Añadir restricciones: cada color debe estar en una y solo una posición
for color in colors:
    KB.add(Or(*[symbols[color][position] for position in positions]))
    for (pos1, pos2) in itertools.combinations(positions, 2):
        KB.add(Implication(symbols[color][pos1], Not(symbols[color][pos2])))

# Añadir restricciones: cada posición debe tener un y solo un color
for position in positions:
    KB.add(Or(*[symbols[color][position] for color in colors]))
    for (color1, color2) in itertools.combinations(colors, 2):
        KB.add(Implication(symbols[color1][position], Not(symbols[color2][position])))

# Aquí iría el código para resolver la KB y encontrar una asignación válida
# Esto podría implicar un algoritmo de backtracking o algún otro método de satisfacción de restricciones

# Imprimir la fórmula de la base de conocimientos
print(KB.formula())
