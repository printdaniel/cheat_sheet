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

