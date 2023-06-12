from interpreter import draw
from chessPictures import *

# Crear instancia con la imagen de una torre
imag = Picture(QUEEN)

# Obtener el número de filas y columnas de la imagen
num_rows = len(imag.img)
num_cols = len(imag.img[0])

# Obtener la mitad de la imagen
half_image = []
for i in range(num_rows):
    half_image.append(imag.img[i][:num_cols//2])

# Mostrar la mitad del tablero de ajedrez
draw(half_image)

