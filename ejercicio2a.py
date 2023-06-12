from interpreter import draw
from chessPictures import *

# Crear una instancia de la imagen del caballo
knight = Picture(KNIGHT)

# Unir dos imágenes del caballo horizontalmente
row1 = knight.join(knight)

# Obtener el espejo horizontal de la primera fila
row2 = row1.horizontalMirror()

# Unir las dos filas verticalmente para formar el tablero
board = row1.up(row2)

# Mostrar el tablero con los 4 caballos
draw(board)

