"""
Una estructura de datos de lista enlazada (linked list) es un tipo de estructura
de datos que organiza sus elementos en nodos individuales, donde cada nodo contiene
un valor y una referencia (o enlace) al siguiente nodo en la secuencia. Esta estructura
es fundamental en programación y se utiliza por varias razones importantes:

Flexibilidad en la Inserción y Eliminación de Elementos: A diferencia de otras
estructuras como los arrays, donde las operaciones de inserción y eliminación
pueden ser costosas en términos de tiempo, en una lista enlazada estas operaciones
suelen ser más eficientes. Esto se debe a que solo se necesita modificar las
referencias de los nodos, sin tener que mover todos los elementos de la estructura.
- Uso Eficiente de Memoria: Las listas enlazadas pueden adaptarse dinámicamente al
tamaño de los datos que contienen. Esto significa que ocupan la cantidad exacta
de memoria necesaria para almacenar los elementos que tienen, evitando el
desperdicio de memoria que puede ocurrir en estructuras de tamaño fijo como los arrays.
- Acceso Secuencial a los Elementos: Al recorrer una lista enlazada, se accede a
los elementos de manera secuencial siguiendo los enlaces entre nodos. Esto facilita
la implementación de algoritmos que requieren recorrer los elementos en un orden específico.
Implementación de Pilas y Colas: Las listas enlazadas son la base para implementar
estructuras de datos más complejas como pilas (stacks) y colas (queues). Estas
estructuras se utilizan para gestionar datos de manera LIFO (Last In, First Out)
en el caso de las pilas, y FIFO (First In, First Out) en el caso de las colas.
- Manipulación de Datos Dinámicos: Cuando se trabaja con datos cuyo tamaño puede
variar durante la ejecución del programa, como en aplicaciones que manejan listae
de reproducción de música o listas de tareas, las listas enlazadas son una opción
eficiente para manejar estos datos dinámicos.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Head of the Linked List

    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        # Update the reference of the new node to point to the current head
        new_node.ref = self.head
        # Update the head of the linked list to point to the new node
        self.head = new_node
        # Return the LinkedList object (optional)
        return self

    def add_end(self, data):
        new_node = Node(data) # Crea un nuevo nodo con el dato proporcionado
        if self.head is None: # Si la lista esta vacía, el nuevo nodo se convierte en la cabecera.
            self.head = new_node
        else: # Si la lista no está vacía, se agrega el nuevo nodo al final de la lista
            n = self.head
            while n.ref is not None: # Recorre la lista esta encontrar el último nodo
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_value(self, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref = n.ref.ref


