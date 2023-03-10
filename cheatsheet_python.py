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

#################
# Función REDUCE# 
#################

""" 
reduce es una función en Python que permite reducir una secuencia (por ejemplo, 
una lista) a un solo valor combinando elementos de la secuencia de forma secuencial. 
La función reduce se encuentra en el módulo functools.

La sintaxis de reduce es la siguiente:
    from functools import reduce

    reduce(function, iterable)

function: es la función que se aplicará para reducir la secuencia. 
La función debe aceptar dos argumentos y devolver un solo valor.
iterable: es la secuencia que se reducirá.
El resultado de reduce es el valor final después de aplicar la función 
function a los elementos de la secuencia.

Ejemplo:

"""
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers) # 15


#################
# Función REDUCE# 
#################


""" 
set es una estructura de datos en Python que permite almacenar valores únicos. 
La función intersection se usa para calcular la intersección entre dos conjuntos, 
es decir, para encontrar los valores que están presentes en ambos conjuntos.

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

############################################################
# Unittest con suites, (crear varias instancias)
############################################################

from math_functions import *
from string_functions import *

# Creamos dos clases de prueba, una para cada archivo
class TestMathFunctions(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)
        
    def test_resta(self):
        self.assertEqual(restar(5, 3), 2)

class TestStringFunctions(unittest.TestCase):
    
    def test_concatenar(self):
        self.assertEqual(concatenar('Hola', 'mundo'), 'Hola mundo')
        
    def test_mayusculas(self):
        self.assertEqual(convertir_a_mayusculas('Hola mundo'), 'HOLA MUNDO')

# Creamos una suite de pruebas que incluye ambas clases de prueba
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestMathFunctions))
suite.addTest(unittest.makeSuite(TestStringFunctions))

# Ejecutamos la suite de pruebas
runner = unittest.TextTestRunner()
runner.run(suite)



#########################################################
# ! Utilización de logger para debuggear
#########################################################

""" 
Logger es un módulo de registro de eventos en Python que se utiliza para recopilar 
información sobre los eventos que ocurren en una aplicación. Los registros 
son útiles para el análisis y la depuración de la aplicación, así como para 
mantener un registro de las actividades de la aplicación.
"""

import logging

"""
Configura el nivel de registro adecuado para el módulo logger. El nivel de 
registro indica el tipo de mensajes que se registran. Por ejemplo, si se 
establece el nivel de registro en DEBUG, se registrarán mensajes de depuración, 
información, advertencias y errores.
"""
logging.basicConfig(level=logging.DEBUG)
""" 
Crea un objeto logger utilizando el método getLogger() del módulo logging. 
Puedes pasar el nombre del objeto logger como argumento. El nombre es útil 
si deseas crear varios objetos logger en tu aplicación.
"""
logger = logging.getLogger('my_app')
""" 
Utiliza el objeto logger para registrar mensajes en tu aplicación utilizando 
los métodos de registro disponibles (debug(), info(), warning(), error() y 
critical()).
"""

logger.debug('Este es un mensaje de depuración')
logger.info('Este es un mensaje de información')
logger.warning('Este es un mensaje de advertencia')
logger.error('Este es un mensaje de error')
logger.critical('Este es un mensaje crítico')

"""Opcionalmente, puedes utilizar formateadores para personalizar la forma en 
que se registran los mensajes. Por ejemplo, puedes utilizar el formateador de 
registro predeterminado de la siguiente manera:

"""
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


#######################
# Decorador para perfo
#######################

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(
            f"La función {func.__name__} tardó {fin - inicio:.5f} segundos en ejecutarse.")
        return resultado
    return wrapper


@medir_tiempo
def tiempo():
    time.sleep(3)

