# Main.py

from Estructura import Cola, Pila
from Metodos import procesar_cola

def main():
    cola = Cola()
    pila = Pila()

    cadena = input("Ingrese una cadena de texto: ")

    for caracter in cadena:
        cola.encolar(caracter)

    print("\nCola original:", cola.ver_elementos())

    procesar_cola(cola, pila)

    print("Cola final (posiciones pares):", cola.ver_elementos())
    print("Pila final (posiciones impares - orden LIFO):", pila.ver_elementos())

if __name__ == "__main__":
    main()
