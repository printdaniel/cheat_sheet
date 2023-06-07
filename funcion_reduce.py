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
