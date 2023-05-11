class Wektor:
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __str__(self):
      return '[{0.x};{0.y}]'.format(self)
 
   def __mul__(self, liczba):
      return Wektor(liczba*self.x, liczba*self.y)
   __rmul__ = __mul__
   
   def __add__(self, other):
      return Wektor(self.x + other.x, self.y + other.y)
   
   def __
   
x = Wektor(1,3)
y = Wektor(2, -4)

z = x.__add__(y)
print(z)
