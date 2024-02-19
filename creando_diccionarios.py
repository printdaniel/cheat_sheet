# Crear diccinarios
"""
Estructura básica key : value

value -> cualquier objeto python
key -> cualquier objeto hashable 

hashables: int, float, complex, binary, decimal, fraction
strings, frozenset, tuples (si los elementos son hashables)
funciones, clases (tal vez)

No hashables:
    set, dicitionary
    list
"""


a = {'k1': 100, 'k2': 200}
print(type(a))
print(hash((1,2,3)))

###############################################################################
# Qué sucede ahora?
t1 = (1,2,3)
t2 = (1,2,3)

print(t1 == t2)
print(hash(t1) == hash(t2))
"""
Comparación de tuplas (t1 == t2): En Python, la comparación de tuplas se realiza 
elemento por elemento. En este caso, ambas tuplas t1 y t2 tienen los mismos 
elementos en el mismo orden, por lo que la comparación t1 == t2 devuelve True.

Comparación de hashes (hash(t1) == hash(t2)): Cuando calculas el hash de cada 
tupla, obtienes dos valores enteros. Estos valores de hash se calculan 
basándose en los elementos y el orden de la tupla. Dado que t1 y t2 son 
idénticas, sus valores de hash también deberían ser idénticos.
"""
