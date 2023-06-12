from interpreter import draw
from chessPictures import Picture, QUEEN

class Ajedrez:
    def mostrar_tablero(self):
        # Crear una instancia de la clase Picture con la imagen de la reina
        image = Picture(QUEEN)
        
        # Repetir horizontalmente la imagen dos veces
        image = image.horizontalRepeat(2)
        
        # Mostrar la imagen utilizando la función draw()
        draw(image)

# Crear una instancia de la clase Ajedrez
ajedrez = Ajedrez()

# Llamar al método mostrar_tablero() para mostrar el tablero de ajedrez
ajedrez.mostrar_tablero()

