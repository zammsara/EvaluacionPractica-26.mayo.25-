#Definienfo la clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
    def __str__(self):
        return str(self.dato)

class Pila: 
    def __init__(self):
        self.tope = None # Inicia vacía
    
    # Agregar un elemento
    def push(self, dato):
        nuevo_nodo = Nodo(dato) 
        nuevo_nodo.siguiente = self.tope #el nuevo apunta al anterior tope
        self.tope = nuevo_nodo #el nuevo ahora es el tope
        
    # Eliminar y retornar el último elemento insertado
    def pop(self):
        if self.tope is None:
            print("Pila vacía. No se puede eliminar.")
            return None
        eliminado = self.tope.dato
        self.tope = self.tope.siguiente #avanza el tope al siguiente nodo
        return eliminado
    
    # Retornar el último elemento sin eliminarlo
    def peek(self):
        if self.tope is None:
            print("Pila vacía. No se puede mostrar el elemento.")
            return None
        return self.tope.dato  # Retorna el dato del nodo superior
    
    ## Imprimir todos los elementos de la pila
    def imprimir(self):
        if self.tope is None:
            print("La pila está vacía.")
            return None
        else:
            actual = self.tope  # Empieza desde el nodo superior
            while actual is not None:  # Recorre todos los nodos
                print(actual, end=" ")  # Imprime el dato del nodo
                actual = actual.siguiente  # Avanza al siguiente nodo

#Definiendo la clase Cola
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.pila = Pila()  # Instancia de la pila para manejar los precios
        
    # Método para insertar un elemento en la cola
    def Insertar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    # Método para eliminar el primer elemento de la cola
    def Eliminar(self):
        if self.primero is None:
            return None
        else:
            dato = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero is None:
                self.ultimo = None
            return dato
    
    #Pasa los elementos de la cola a la pila según su posición
    def ProcesarCola(self):
        nueva_cola = Cola()  # Cola temporal para los elementos en posiciones pares
        actual = self.primero
        indice = 0
        # Verifica si la cola está vacía
        if actual is None:
            print("Cola vacía. No se puede procesar.")
            return
        
        while actual is not None:
            if indice % 2 == 0: # Verifica si la posición es par
                nueva_cola.Insertar(actual.dato)  # Posición par: permanece en la cola
            else:
                # Se asume que dato tiene atributos tipo y precio
                self.pila.push(actual.dato)  # Posición impar: va a la pila
            actual = actual.siguiente
            indice += 1
        # Actualizar la cola original con los elementos pares
        self.primero = nueva_cola.primero
        self.ultimo = nueva_cola.ultimo
        print("Cola Procesada. Los elementos en posiciones impares se han movido a la pila.")
        
    # Método para imprimir los elementos de la cola 
    def ImprimirCola(self):
        actual = self.primero
        if actual is None:
            print("Cola vacía.")
            return
        while actual is not None:
            print(actual, end=" ")  # Imprime el dato del nodo
            actual = actual.siguiente
    
    # Método para imprimir los elementos de la pila
    def ImprimirPila(self):
        self.pila.imprimir()
        