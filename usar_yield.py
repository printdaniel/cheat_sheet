""" 
yield en Python se utiliza dentro de una función para convertirla en un 
generador. Un generador es una función especial que produce una secuencia de 
valores en lugar de devolver un solo valor. Cada vez que el generador produce 
un valor, la función se suspende y conserva su estado, permitiendo que se 
reanude más tarde para producir el siguiente valor.
"""
def generador():
    yield 1
    yield 2
    yield 3

mi_generador = generador()

for valor in mi_generador:
    print(valor)
