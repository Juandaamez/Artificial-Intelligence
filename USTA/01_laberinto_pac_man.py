# Importar el módulo emoji
import emoji

# Abrir el archivo de entrada
with open("maze.txt", "r") as f:
  # Leer el contenido del archivo
  content = f.read()

# Crear un diccionario para mapear los caracteres del archivo a los emojis
char_to_emoji = {
  "1": emoji.emojize(":brick:", use_aliases=True), # Muro
  "0": emoji.emojize(":white_1large_square:", use_aliases=True), # Camino
  "\n": "\n" # Salto de línea
}

# Crear una variable para almacenar el laberinto en emojis
maze_emoji = ""

# Recorrer el contenido del archivo
for char in content:
  # Si el caracter está en el diccionario, reemplazarlo por el emoji correspondiente
  if char in char_to_emoji:
    maze_emoji += char_to_emoji[char]
  # Si no, dejar el caracter como está
  else:
    maze_emoji += char

# Mostrar el laberinto en emojis en la terminal
print(maze_emoji)
