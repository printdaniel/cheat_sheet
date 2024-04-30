import random
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
def bubblesort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l [j +1]:
                l[j], l[j +1] = l[j+1], l[j]
    return l

def bubbleSort_you(l):
    n = len(l)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                count += 1
                l[j], l[j+1] = l[j+1], l[j]
    return l


@medir_tiempo
def bubble_sort_perplexity(l):
    """
    Implementación optimizada del algoritmo de ordenamiento Bubble Sort que
    ordena una lista de elementos en orden ascendente.

    Parámetros:
    l (list): La lista de elementos a ordenar.

    Retorna:
    list: La lista ordenada en orden ascendente.

    Descripción:
    Esta función utiliza una bandera 'swapped' para controlar si se realizan
    intercambios en cada pasada del arreglo.
    Si no se realizan intercambios en una pasada completa, se asume que el
    arreglo está ordenado y se detiene la ejecución.
    """
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            break
    return l

@medir_tiempo
def bubble_sort_gemini(l):
    """
    Implementación del algoritmo de ordenamiento Bubble Sort que ordena una
    lista de elementos en orden ascendente.

    Parámetros:
    l (list): La lista de elementos a ordenar.

    Retorna:
    list: La lista ordenada en orden ascendente.

    Descripción:
    Esta función utiliza una técnica de optimización con una variable 'intercambios'
    para controlar si se realizan intercambios en cada pasada del arreglo.
    Si no se realizan intercambios en una pasada completa, se asume que
    el arreglo está ordenado y se detiene la ejecución.
    """
    n = len(l)
    intercambios = True

    while intercambios:
        intercambios = False
        for i in range(n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                intercambios = True
    return l

if __name__ == '__main__':
    lista = [2,34,27,349,77,67,85,6,75,78,92,7,3812,91,47,66,734,12,31,8,9]
    print(bubblesort(lista))
    print("Blubble con YOU")
    print(bubbleSort_you(lista))
    print("Blubble con Perplexity")
    print(bubble_sort_perplexity(lista))
    print("Blubble con Gemini")
    print(bubble_sort_gemini(lista))
