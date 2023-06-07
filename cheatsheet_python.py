########################
# Decoradores más usados
########################

"""
@staticmethod: Este decorador se utiliza para definir métodos estáticos en una 
clase. Los métodos estáticos son aquellos que no requieren acceso a los 
atributos de instancia de la clase.

@classmethod: Este decorador se utiliza para definir métodos de clase en una 
clase. Los métodos de clase son aquellos que operan en la clase en sí misma, 
en lugar de en una instancia de la clase.

@property: Este decorador se utiliza para definir propiedades de instancia en 
una clase. Las propiedades son atributos que se comportan como métodos, 
permitiendo la validación o procesamiento adicional de los valores de los 
atributos antes de asignarlos o devolverlos.

@abstractmethod: Este decorador se utiliza para definir métodos abstractos 
en una clase. Los métodos abstractos son aquellos que deben ser implementados 
en las subclases, y no tienen una implementación en la clase base.

@wraps: Este decorador se utiliza para preservar la información de la 
función original en una función envoltorio, incluyendo el nombre, la 
documentación y los argumentos.

@lru_cache: Este decorador se utiliza para cachear los resultados de una 
función y evitar que se vuelvan a calcular en futuras llamadas con los mismos 
argumentos.
"""

###########################
# *args **kwargs
###########################
""" *args:

El parámetro args se utiliza para pasar un número variable de argumentos 
posicionales a una función. Los argumentos posicionales son aquellos que se 
especifican en la llamada a la función, sin incluir los argumentos con nombre. 
El asterisco () antes del nombre del parámetro indica que la función puede 
recibir cualquier número de argumentos posicionales. Los argumentos se pasan
como una tupla y se pueden acceder dentro de la función utilizando su índice 
en la tupla."""

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(1, 2, 3))  # 6
print(suma(4, 5, 6, 7))  # 22

"""
**kwargs:

El parámetro kwargs se utiliza para pasar un número variable de argumentos 
con nombre a una función. Los argumentos con nombre se especifican en la 
llamada a la función utilizando el formato clave=valor. El doble asterisco () 
antes del nombre del parámetro indica que la función puede recibir cualquier 
número de argumentos con nombre. Los argumentos se pasan como un diccionario 
y se pueden acceder dentro de la función utilizando la clave del diccionario.
"""
def imprimir_nombres(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

imprimir_nombres(nombre="Juan", apellido="Pérez", edad=30)
# nombre: Juan
# apellido: Pérez
# edad: 30
