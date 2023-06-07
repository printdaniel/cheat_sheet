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


