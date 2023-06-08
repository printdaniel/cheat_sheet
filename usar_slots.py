""" 
__slots__ es un mecanismo en Python que te permite limitar los atributos que
pueden ser creados y almacenados en una instancia de clase. Al definir
__slots__ en una clase, estás especificando explícitamente los nombres de los
atributos que la instancia de la clase puede tener.

El uso de __slots__ tiene varias implicaciones. Al limitar los atributos,
puedes ahorrar memoria y hacer que el acceso a los atributos sea más rápido.
Sin embargo, también hay algunas limitaciones. No puedes agregar atributos 
adicionales a las instancias de MyClass1 más allá de los especificados 
en __slots__. Además, __slots__ solo afecta a la clase en la que se define y
no a las subclases.

En resumen, __slots__ es una forma de limitar los atributos que se pueden 
agregar a una instancia de clase. Puede ser útil en ciertas situaciones para 
ahorrar memoria y mejorar el rendimiento, pero también impone restricciones en
cuanto a los atributos disponibles.
"""
# Sin Slots
class MyClass(object):
    def __init__(self, name, identifier):
        self.name= name
        self.identifier = identifier

# Con slots
class MyClass1(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name= name
        self.identifier = identifier
 
# En caso de usar herencia
class BaseClass(object):
    __slots__ = ['attribute1', 'attribute2']

class SubClass(BaseClass):
    __slots__ = ['attribute3']
