from interpreter import draw
from chessPictures import *

imag = Picture(KNIGHT)
imagv = imag.join(KNIGHT)
imagvv = imag.horizontalMirror(imagv)

final = imag.up(imagvv)
draw(final)

