####################
# Trabjando con SET# 
####################
""" 
set es una estructura de datos en Python que permite almacenar valores únicos. 
La función intersection se usa para calcular la intersección entre dos conjuntos, 
es decir, para encontrar los valores que están presentes en ambos conjuntos.

"""

""" 
Métodos:

add(elemento): Agrega un elemento al conjunto.
clear(): Elimina todos los elementos del conjunto.
copy(): Crea una copia superficial del conjunto.
difference(otros_conjuntos): Devuelve un nuevo conjunto con elementos presentes
en el conjunto original pero no en los otros conjuntos.
difference_update(otros_conjuntos): Actualiza el conjunto eliminando los 
elementos que también están en los otros conjuntos.
discard(elemento): Elimina un elemento del conjunto si está presente.
intersection(otros_conjuntos): Devuelve un nuevo conjunto con elementos que 
están presentes en el conjunto original y en los otros conjuntos.
intersection_update(otros_conjuntos): Actualiza el conjunto manteniendo solo 
los elementos que también están en los otros conjuntos.

isdisjoint(otro_conjunto): Verifica si el conjunto no tiene elementos en común 
con otro conjunto.

issubset(otro_conjunto): Verifica si todos los elementos del conjunto están 
presentes en otro conjunto.

issuperset(otro_conjunto): Verifica si el conjunto contiene todos los elementos 
de otro conjunto.

pop(): Elimina y devuelve un elemento aleatorio del conjunto.

remove(elemento): Elimina un elemento del conjunto. Genera un error si el 
elemento no está presente.

symmetric_difference(otro_conjunto): Devuelve un nuevo conjunto con elementos 
que están en uno de los conjuntos pero no en ambos.

symmetric_difference_update(otro_conjunto): Actualiza el conjunto con elementos 
que están en uno de los conjuntos pero no en ambos.

union(otros_conjuntos): Devuelve un nuevo conjunto que contiene todos los 
elementos del conjunto original y los elementos de los otros conjuntos.
update(otros_conjuntos): Actualiza el conjunto agregando elementos de los 
otros conjuntos.
"""
a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])


intersection = a.intersection(b)
print(intersection) # {4, 5}

class TestIntersection(unittest.TestCase):
    def test_intersection(self):
        a = set([1, 2, 3, 4, 5])
        b = set([4, 5, 6, 7, 8])

        intersection = a.intersection(b)
        self.assertEqual(intersection, {4, 5})

unittest.main()
