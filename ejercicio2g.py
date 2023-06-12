from interpreter import draw
from chessPictures import *

# Crear instancias de las imágenes de las piezas
pawn = Picture(PAWN)
rook = Picture(ROOK)
knight = Picture(KNIGHT)
bishop = Picture(BISHOP)
queen = Picture(QUEEN)
king = Picture(KING)

# Crear una fila del tablero con las piezas blancas
row1 = rook.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rook)

# Crear una fila del tablero con los peones blancos
row2 = pawn.horizontalRepeat(8)

# Crear una fila vacía para el espacio entre las piezas blancas y negras
empty_row = Picture([EMPTY] * 8)

# Crear una fila del tablero con los peones negros
row7 = pawn.horizontalRepeat(8).negative()

# Crear una fila del tablero con las piezas negras
row8 = rook.horizontalMirror().join(knight.horizontalMirror()).join(bishop.horizontalMirror()).join(queen.horizontalMirror()).join(king.horizontalMirror()).join(bishop.horizontalMirror()).join(knight.horizontalMirror()).join(rook.horizontalMirror())

# Crear el tablero completo uniendo todas las filas
chessboard = row1.up(row2).up(empty_row).up(empty_row).up(empty_row).up(empty_row).up(row7).up(row8)

# Mostrar el tablero de ajedrez completo
draw(chessboard)

