# Importación de módulos necesarios
from utilidades_menu import *  # Importa todas las funciones del módulo de utilidades del menú
from data import *            # Importa las funciones de manejo de datos

# Función principal que inicia la ejecución del programa
ejecucion_menu_principal()    # Llama a la función que muestra y maneja el menú principal

def mostrar_menu():
    return print(menu_principal)  # Muestra el menú principal en la consola