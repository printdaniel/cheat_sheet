"""
Cuando llamemos a str(r1), Python buscará primero si nuestra clase (Rectángulo) 
tiene un método especial llamado __str__.
Si el método __str__ está presente, entonces Python lo llamará y devolverá ese 
valor.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)

r1 = Rectangle(12, 20)
print(str(r1))

"""
Como puedes ver seguimos obteniendo ese valor por defecto. Eso es porque aquí 
Python no está convirtiendo r1 en una cadena, sino que está buscando una 
representación en cadena del objeto. Está buscando el método __repr__ 
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

r1 = Rectangle(10, 20)
print(r1)

"""
Como puedes ver, Python no considera r1 y r2 como iguales (usando el operador ==).
De nuevo, ¿cómo se supone que Python sabe que dos objetos Rectángulo con la 
misma altura y anchura deben considerarse iguales?
Sólo tenemos que decirle a Python cómo hacerlo, utilizando el método especial __eq__.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        print('self={0}, other={1}'.format(self, other))
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)



