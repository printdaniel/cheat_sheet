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
