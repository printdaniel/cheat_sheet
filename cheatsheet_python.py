import unittest

##############
# Función MAP# 
##############

"""
map es una función en Python que permite aplicar una función a cada elemento de 
un objeto iterable, como una lista, y devuelve un nuevo objeto iterable con los
resultados. La sintaxis de map es la siguiente:
    map(function, iterable)

function: es la función que se aplicará a cada elemento del objeto iterable.
iterable: es el objeto iterable (por ejemplo, una lista) sobre el cual se aplicará 
la función.
El resultado de map es un objeto map que se puede convertir a una lista, 
tupla, etc. utilizando la función list(), tuple(), etc.

Ejemplo:
"""
def cuadrado(x):
    return x**2

numeros = [1,2,4,5,6]
cuadrado_num = list(map(cuadrado, numeros))
print(cuadrado_num)


class TestCuadarado(unittest.TestCase):
    def test_cuadrado(self):
        self.assertEqual(cuadrado(2),4)
        self.assertEqual(cuadrado(0),0)
        self.assertEqual(cuadrado(-2),4)
        self.assertEqual(cuadrado(3),9)
        self.assertEqual(cuadrado(7),49)

unittest.main()

#################
# Función FILTER# 
#################


""" 
filter es una función en Python que permite filtrar elementos de un objeto 
iterable utilizando una función. La sintaxis de filter es la siguiente:

    filter(function, iterable)

function: es la función que se usará para filtrar elementos. La función debe 
devolver True o False para cada elemento.
iterable: es el objeto iterable (por ejemplo, una lista) que se filtrará.
El resultado de filter es un objeto filter que se puede convertir a una lista, 
tupla, etc. utilizando la función list(), tuple(), etc.

Ejemplo:
"""

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # [2, 4]


def is_even(x):
    return x % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(-1))

unittest.main()





























