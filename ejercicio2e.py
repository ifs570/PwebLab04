from interpreter import draw
from chessPictures import *

# Crear instancia con la imagen de una torre
imag = Picture(QUEEN)

# Repetir la imagen horizontalmente dos veces
image = imag.horizontalRepeat(2)

# Obtener el espejo horizontal de la imagen repetida
mirror_image = image.horizontalMirror()

# Mostrar una fila del tablero de ajedrez con el orden contrario
chess_row = mirror_image.join(image)

draw(chess_row)

