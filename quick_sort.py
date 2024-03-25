import time

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
def quick_sort(arr):
    """
    Implementación del algoritmo de ordenamiento Quick Sort para ordenar una 
    lista de elementos en orden ascendente.

    Parámetros:
    arr (list): La lista de elementos a ordenar.

    Retorna:
    list: La lista ordenada en orden ascendente.

    Descripción:
    Este algoritmo de ordenamiento funciona dividiendo la lista en sub-listas 
    más pequeñas y luego ordenando esas sub-listas.
    Utiliza un elemento pivote para comparar y dividir la lista en dos partes: 
    una con elementos menores que el pivote y otra con elementos mayores que 
    el pivote.
    Luego aplica recursivamente el mismo proceso a cada sub-lista hasta que 
    toda la lista esté ordenada.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == '__main__':
    lista = [23,83,48,95,4,8,97,45,127,237,85,765,67,68,231,24,51,245,3]
    print(quick_sort(lista))
