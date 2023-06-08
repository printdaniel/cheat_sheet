"""
El deque de la biblioteca collections de Python y una lista normal tienen 
algunas diferencias importantes en cuanto a su implementación y rendimiento:

Eficiencia en inserción y eliminación: El deque es más eficiente que una lista
normal cuando se trata de realizar operaciones de inserción y eliminación en 
los extremos. Las operaciones append() y popleft() en un deque tienen una 
complejidad de tiempo constante O(1), mientras que las operaciones equivalentes 
en una lista normal tienen una complejidad de tiempo lineal O(n), donde n es 
el tamaño de la lista. Esto se debe a que el deque está implementado como una
estructura de datos doblemente enlazada.

Acceso a elementos: En cuanto al acceso a elementos por índice, una lista 
normal es más eficiente. Acceder a un elemento por índice en una lista normal 
tiene una complejidad de tiempo constante O(1), mientras que en un deque, 
el acceso a elementos por índice tiene una complejidad de tiempo lineal O(n).
Por lo tanto, si necesitas acceder a elementos por índice con frecuencia, una
lista normal es más adecuada.

Capacidad de crecimiento: Una lista normal en Python puede crecer y cambiar de 
tamaño dinámicamente según sea necesario. Puedes agregar o eliminar elementos 
en cualquier posición de la lista sin restricciones de tamaño fijo. En contraste,
aunque el deque también tiene capacidad de cambio de tamaño, agregar o eliminar 
elementos en posiciones intermedias puede ser menos eficiente que en una lista
normal debido a la estructura de datos doblemente enlazada.

Funcionalidad adicional: El deque proporciona métodos adicionales específicos 
para colas y pilas, como appendleft(), pop(), extendleft(), etc., que no están 
disponibles en una lista normal. Estos métodos facilitan el uso del deque como 
una estructura de datos FIFO (cola) o LIFO (pila).

En resumen, la elección entre un deque y una lista normal depende de las 
operaciones que planeas realizar con la estructura de datos. Si necesitas 
realizar operaciones de inserción y eliminación eficientes en los extremos 
de la estructura de datos y no te importa un acceso menos eficiente por índice, 
un deque puede ser una mejor opción. Si el acceso por índice es crítico y las 
operaciones de inserción y eliminación no se realizan principalmente en los
extremos, una lista normal es más adecuada.
"""

"""
Collections
defautldict
OrdereDict
Counter
deque
nametuple
enum.Enum (Python 3.4+)
"""

#  Defaultdict

from collections import defaultdict
colours = (
('Yasoob', 'Yellow'),
('Ali', 'Blue'),
('Arham', 'Green'),
('Ali', 'Black'),
('Yasoob', 'Red'),
('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)
print(favourite_colours)

# Counter
from collections import Counter
colours = (
('Yasoob', 'Yellow'),
('Ali', 'Blue'),
('Arham', 'Green'),
('Ali', 'Black'),
('Yasoob', 'Red'),
('Ahmed', 'Silver'),
)
favs = Counter(name for name, colour in colours)
print(favs)
print(type(favs))


from collections import deque
""" 
deque provides you with double ended queue which means that you can append and 
delete elements from either side of the queue. First of all you have to import 
the deque module from the colections library
"""
from collections import deque

d = deque()
d.append("1")
d.append("2")
d.append("3")
d.append("3")
print(len(d))

