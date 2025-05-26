# Main.py

from Estructura import Cola, Pila #Uso de modularizacion
from Metodos import procesar_cola

def main():
    cola = Cola() #iniicializa la cola cola
    pila = Pila() # los mismo pero con la pila 

    cadena = input("Ingrese una cadena de texto: ") # Ingresar los datos 

    for caracter in cadena:
        cola.encolar(caracter)

    print("\nCola original:", cola.ver_elementos())

    procesar_cola(cola, pila)

    print("Cola final (posiciones pares):", cola.ver_elementos()) # Imprime la cola con los numeros pares
    print("Pila final (posiciones impares - orden LIFO):", pila.ver_elementos()) #Ingresa la pila con numeros impares

if __name__ == "__main__":
    main()
