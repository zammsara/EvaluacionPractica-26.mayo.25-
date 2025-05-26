# Definición de la clase Cola (estructura de datos FIFO: primero en entrar, primero en salir)
class Cola:
    def __init__(self):
        # Inicializa la cola como una lista vacía
        self.items = []

    def encolar(self, elemento):
        # Agrega un elemento al final de la cola
        self.items.append(elemento)

    def desencolar(self):
        # Elimina y devuelve el primer elemento de la cola, si no está vacía
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        # Retorna True si la cola está vacía, False en caso contrario
        return len(self.items) == 0

    def ver_elementos(self):
        # Devuelve una copia de la lista de elementos de la cola
        return self.items.copy()

    def tamaño(self):
        # Retorna el número de elementos en la cola
        return len(self.items)


# Definición de la clase Pila (estructura de datos LIFO: último en entrar, primero en salir)
class Pila:
    def __init__(self):
        # Inicializa la pila como una lista vacía
        self.items = []

    def apilar(self, elemento):
        # Agrega un elemento al final de la pila
        self.items.append(elemento)

    def desapilar(self):
        # Elimina y devuelve el último elemento agregado (tope de la pila), si no está vacía
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        # Retorna True si la pila está vacía, False en caso contrario
        return len(self.items) == 0

    def ver_elementos(self):
        # Devuelve una copia de la lista de elementos de la pila
        return self.items.copy()
