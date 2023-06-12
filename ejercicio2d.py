from interpreter import draw
from chessPictures import *

# Crear instancia con la imagen de una torre
imag = Picture(QUEEN)

# Repetir la imagen horizontalmente dos veces
image = imag.horizontalRepeat(2)

# Mostrar una fila del tablero de ajedrez
chess_row = image.join(image.horizontalMirror())

draw(chess_row)

