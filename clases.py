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

"""
 Python tiene métodos especiales que podemos usar para proporcionar esa funcionalidad.
Son métodos como __lt__, __gt__, __le__, et
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
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

"""
En un lenguaje como Java, implementaríamos getWidth y setWidth y haríamos width
privado - lo que rompería cualquier código que accediera directamente a la 
propiedad width.
En Python podemos usar algunos decoradores especiales (los veremos más adelante) 
para encapsular nuestros getters y setters de propiedades:
"""
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height

r1 = Rectangle(10, 20)
print(r1.width)
r1.width = 100
print(r1)

"""
ay más cosas que deberíamos hacer para implementar correctamente todo esto, 
en particular deberíamos comprobar también los valores positivos y negativos 
durante la fase __init__. Lo hacemos mediante el uso de los métodos de acceso 
para la altura y la anchura:
"""
class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height

r1 = Rectangle(0, 10)


