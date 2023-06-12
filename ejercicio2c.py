from interpreter import draw
from chessPictures import Picture, QUEEN

# Crear una instancia de la clase Picture con la imagen de la reina
image = Picture(QUEEN)

# Repetir horizontalmente la imagen dos veces
image = image.horizontalRepeat(2)

# Mostrar la imagen utilizando la función draw()
draw(image)
