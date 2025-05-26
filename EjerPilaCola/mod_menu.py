import os

def limpiar_consola():
    # Detecta el sistema operativo y ejecuta el comando correspondiente
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS y Linux
        os.system('clear')
        
def menu_principal():
    print("Menu Principal")
    print("1. Ingresar Numeros")
    print("2. Procesar Cola")
    print("3. Imprimir Cola")
    print("4. Imprimir Pila")
    print("5. Imprimir Ambas")
    print("6. Salir")

def pausa():
    input("Presione Enter para continuar...")