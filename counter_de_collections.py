"""collections. Permite contar la frecuencia de elementos en una lista u otra estructura de datos """
from collections import Counter

"""Métodos de Counter:
Counter tiene varios métodos útiles. Algunos ejemplos son:
most_common(n): Devuelve una lista de los n elementos más comunes y sus frecuencias.
elements(): Devuelve un iterador que produce todos los elementos en el Counter.
update(iterable): Actualiza el Counter con elementos de otro iterable.
subtract(iterable): Resta elementos de otro iterable del Counter."""

if __name__ == '__main__':
    lista = [1,2,3,1,2,4,5,1,3]
    contador = Counter(lista)
    # Acceder a elementos específicos
    print(contador[1])

    # Obtener los 2 elmentos más comunes y uss frecuencias
    print(contador.most_common(2))

    # Obtner una lista de todos los elementos en el Counter
    print(list(contador.elements()))
