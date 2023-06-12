from colors import inverter


class Picture:
  
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """Devuelve el espejo vertical de la imagen"""
    vertical = [value[::-1] for value in self.img]
    return vertical

  def horizontalMirror(self):
    """Devuelve el espejo horizontal de la imagen"""
    horizon = [row[::-1] for row in self.img]
    return horizon

  def negative(self):
    """Devuelve un negativo de la imagen"""
    inverted_img = [self._invColor(color) for row in self.img for color in row]
    return Picture(inverted_img)

  def join(self, chess):
    """Devuelve una nueva figura poniendo la figura del argumento
       al lado derecho de la figura actual"""
    new_img = [row + chess_row for row, chess_row in zip(self.img, chess.img)]
    return Picture(new_img)

  def up(self, chess):
    """Devuelve una nueva figura poniendo la figura del argumento
       debajo de la figura actual"""
    new_img = self.img + chess.img
    return Picture(new_img)

  def under(self, p):
    """Devuelve una nueva figura poniendo la figura p sobre la
       figura actual"""
    return Picture(None)

  def horizontalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual al costado
       la cantidad de veces que indique el valor de n"""
    new_img = self.img.copy()
    for _ in range(n - 1):
      new_img.extend(self.img)
    return Picture(new_img)

  def verticalRepeat(self, n):
    """Devuelve una nueva figura repitiendo la figura actual arriba y abajo
       la cantidad de veces que indique el valor de n"""
    new_img = self.img.copy()
    for _ in range(n - 1):
      new_img += self.img
    return Picture(new_img)

  def rotate(self):
    """Devuelve una figura rotada en 90 grados en sentido horario"""
    rotated = [list(row[::-1]) for row in zip(*self.img)]
    return Picture(rotated)

