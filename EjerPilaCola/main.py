# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# REORDENAR COLA A PILA POS IMPARES || Versión 1.0
# 26.mayo.2025

#Descripción del programa: 
"""
Dado una cola con elementos y una pila vacía, desarrollar un programa que procese la cola de forma que:
	Los elementos que se encuentran en posiciones pares (0, 2, 4, ...) permanezcan en la cola.
	Los elementos que se encuentran en posiciones impares (1, 3, 5, ...) se transfieran a la pila.
# El programa permite al usuario interactuar con una cola y una pila, insertando números en la cola
"""
from mod import Cola
import mod_menu as menu

respuesta = 0
cola = Cola()

while respuesta != 6:
    menu.limpiar_consola()
    menu.menu_principal()
    #valida que la respuesta sea un número entero
    try:
        respuesta = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        menu.pausa()
        continue
    
    match respuesta:
        #Agrega un número a la cola
        case 1:
            #valida que sea un número entero
            try:
                numero = int(input("Ingrese un número: "))
                cola.Insertar(numero)
                print(f"Número {numero} agregado a la cola.")
                menu.pausa()
                
            except ValueError:
                print("Por favor, ingrese un número válido.")
                menu.pausa()
                continue
            
        #Procesa la cola, moviendo los elementos impares a la pila 
        case 2:
            cola.ProcesarCola()
            
            print("\n")
            menu.pausa()
            
        #Muestra los elementos que estaban en posiciones pares
        case 3:
            print("Elementos que estaban en posiciones pares:")
            cola.ImprimirCola()
            print("\n")
            menu.pausa()
        
        #Muestra los elementos que estaban en posiciones impares (en la pila)
        case 4:
            print("Elementos que estaban en posiciones impares (en la pila):")
            cola.ImprimirPila()
            print("\n")
            menu.pausa()
            
        #Muestra los elementos en la cola y en la pila
        case 5:
            print("Elementos en la cola:")
            cola.ImprimirCola()
            print("\n")
           
            print("\nElementos en la pila:")
            cola.ImprimirPila()
            print("\n")
            menu.pausa()
            
        #Sale del programa
        case 6:
            print("Saliendo del programa.")
            print("\n")
            menu.pausa()
            
        #Opción no válida
        case _:
            print("Opción no válida. Por favor, intente de nuevo.")
            print("\n")
            menu.pausa()
            
            
    