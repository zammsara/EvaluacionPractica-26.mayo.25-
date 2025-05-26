
import Estructura 


"""Estructura de datos: Pila
   Clase para manejar una pila con operaciones básicas."""

cola = Estructura.Cola()
pila = Estructura.Pila() 

def verificar_par(cola, pila): 
    """Verifica si la cadena (numerica) es par o impar."""
    
    tamaño_original = cola.tamaño() # Obtiene el tamaño original de la cola 
    for i in range(tamaño_original): # Recorre el tamaño original de la cola 
        elemento = cola.desencolar() # Desencola el elemento de la cola 
        if i % 2 == 0:               # Si el índice es par 
            cola.encolar(elemento)   # Reencola el elemento en la cola
        else:
            pila.apilar(elemento)    # Apila el elemento en la pila si el índice es impar 

            

        
    
   