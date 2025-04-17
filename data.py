# Importación de módulos necesarios
import json  # Importa el módulo para manejo de archivos JSON

# Variables globales para almacenar datos en memoria
registros = {}  # Almacena datos de usuarios
cuentas = {}  # Almacena datos de cuentas bancarias
cuentas_registradas = {}  # Almacena información de cuentas registradas
bolsillos = {}  # Almacena datos de bolsillos de ahorro
movimientos = {}  # Almacena historial de movimientos

def cargar_datos(archivo):
    """
    Función para cargar datos desde un archivo JSON.
    
    Args:
        archivo (str): Ruta del archivo JSON a cargar
        
    Returns:
        dict: Datos cargados del archivo o diccionario vacío si hay error
    """
    try:
        with open(archivo, "r") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        print("No se encontró el archivo, iniciando con una base de datos vacía.")
        return {}
    except json.JSONDecodeError:
        print("Error al leer los datos, el archivo puede estar corrupto.")
        return {}


def guardar_datos(datos, archivo):
    """
    Función para guardar datos en un archivo JSON.
    
    Args:
        datos (dict): Datos a guardar
        archivo (str): Ruta del archivo donde se guardarán los datos
    """
    try:
        if datos:
            with open(archivo, "w") as file:
                json.dump(datos, file, indent=4)  # Guarda los datos con formato indentado
        else:
            print("Advertencia: No hay datos para guardar.")
    except Exception as e:
        print(f"Error al guardar datos: {e}")