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

print(id(t1), id(t2))
print(id(t1) == id(t2))


d = {(1,2,3): "esto es una tupla"}
print(d[(1,2,3)])

###############################################################################
# Funciones en la key

def my_func(a,b,c):
    print(a, b, c)

print(hash(my_func))

d = {my_func: [12,23,45]}
print(d[my_func])


def fn_add(a, b):
    return a + b

def fn_inv(a):
    return 1 / a

def fn_mult(a, b):
    return a * b

funcs = {fn_add:(10,34), fn_inv:(7,), fn_mult:(180, 192) }

for f in funcs:
    result = f(*funcs[f])
    print(result)

for f, args in funcs.items():
    print(f(*args))


###############################################################################
# Creación de diccionarios usando el constructor

d = dict([('a',100), ['x',200]])

print(d)
###############################################################################
# otra manera de crear diccionarios

keys = ['a', 'b', 'c']
values = (1,2,3)

d = {}
for k, v in zip(keys,values):
    d[k] = v

print(d)


d = {k:v for k, v in zip(keys, values)}
print(d)


keys = 'abcd'
values = range(1,10)

d = {k: v for  k,v in zip(keys, values) if v % 2==0}
print(d)

x_coords = (-2,-1,0,1,2)
y_coords = (-2,-1,0,1,2)

grid = [(x,y) for x in x_coords for y in y_coords]

print(grid)

import math


grid_extended = [(x,y, math.hypot(x,y)) for x, y in grid]

print(grid_extended)

dict_grid_extended = {(x,y): math.hypot(x,y) for x, y in grid}
print(dict_grid_extended)

counters = dict.fromkeys(['a', 'b', 'c'], 0)
print(counters)

d = dict.fromkeys('python')
print(d)
###############################################################################
# Operaciones básicas

d = dict(zip("abc", range(1,4)))
print(d)

print(len(d))
print(d['a'])
print(d.get('a'))

d.get('z', 'N/A')

print(d)

# Hacer un contador

text = 'Programa siempre tu código como si el tipo que va a tener que mantenerlo en el futuro fuera un violento psicópata que sabe donde vives.'

counts = dict()

for c in text:
    counts[c] = counts.get(c,0) + 1

print(counts)

# otro contador
counts = dict()

for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1 
print(counts)

# contador de upercase y lowercase

import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        if key not in categories:
            categories[key] = set()

        categories[key].add(c)

for cat in categories:
    print(f'{cat}:',''.join(categories[cat]))

# Más simple
categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        categories.setdefault(key, set()).add(c)


for cat in categories:
    print(f'{cat}:',''.join(categories[cat]))

# Con una función
def cat_key(c):
    if c == ' ':
        return None
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_uppercase:
        return 'upper'
    else:
        return 'other'

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:',''.join(categories[cat]))

# Una versión más Pro 

def cat_key(c):
    categories = {' ': None,
                  string.ascii_lowercase: 'lower',
                  string.ascii_uppercase: 'upper'}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return 'other'


print(cat_key('a'))
print(cat_key('A'))
print(cat_key(','))

# Otra manera

from itertools import chain

def cat_key(c):
    cat_1 = {' ': None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase: 'upper')

    return categories.get(c, 'other')

    categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))







