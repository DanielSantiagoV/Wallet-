# Importación de módulos necesarios
import json  # Importa el módulo para manejo de archivos JSON
import os    # Importa el módulo para manejo de rutas
import logging  # Importa el módulo para logging
from colorama import Fore, Style
from typing import Dict, Any, Optional  # Importa tipos para type hints

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Variables globales para almacenar datos en memoria
registros: Dict[str, Any] = {}  # Almacena datos de usuarios
cuentas: Dict[str, Any] = {}  # Almacena datos de cuentas bancarias
cuentas_registradas: Dict[str, Any] = {}  # Almacena información de cuentas registradas
bolsillos: Dict[str, Any] = {}  # Almacena datos de bolsillos de ahorro
movimientos: Dict[str, Any] = {}  # Almacena historial de movimientos

def obtener_ruta_archivo(archivo: str) -> str:
    """
    Obtiene la ruta completa del archivo, manejando casos especiales.
    
    Args:
        archivo (str): Nombre del archivo
        
    Returns:
        str: Ruta completa del archivo
    """
    try:
        if archivo == "registros.json":
            ruta_base = os.path.dirname(os.path.abspath(__file__))
            return os.path.join(ruta_base, "usuarios", "registros.json")
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), archivo)
    except Exception as e:
        logging.error(f"Error al obtener ruta del archivo: {str(e)}")
        raise

def validar_datos(datos: Dict[str, Any]) -> bool:
    """
    Valida que los datos sean un diccionario no vacío.
    
    Args:
        datos (Dict[str, Any]): Datos a validar
        
    Returns:
        bool: True si los datos son válidos, False en caso contrario
    """
    if not isinstance(datos, dict):
        logging.error("Los datos no son un diccionario")
        return False
    return True

def cargar_datos(archivo: str) -> Dict[str, Any]:
    """
    Función para cargar datos desde un archivo JSON.
    
    Args:
        archivo (str): Ruta del archivo JSON a cargar
        
    Returns:
        Dict[str, Any]: Datos cargados del archivo o diccionario vacío si hay error
    """
    ruta_completa = obtener_ruta_archivo(archivo)
    
    try:
        if not os.path.exists(ruta_completa):
            raise FileNotFoundError(f"El archivo {ruta_completa} no existe")
            
        with open(ruta_completa, "r", encoding='utf-8') as file:
            datos = json.load(file)
            if not validar_datos(datos):
                raise ValueError("Los datos cargados no son válidos")
                
            logging.info(f"Archivo {ruta_completa} cargado exitosamente")
            print(f"\n{Fore.GREEN}✅ Archivo cargado exitosamente: {ruta_completa}{Style.RESET_ALL}\n")
            return datos
            
    except FileNotFoundError:
        mensaje = f"\n{Fore.YELLOW}🔍 ⚠️  No se encontró el archivo {ruta_completa}"
        print(mensaje)
        print(f"{Fore.CYAN}📂 Se iniciará con una base de datos vacía.{Style.RESET_ALL}\n")
        logging.warning(f"Archivo no encontrado: {ruta_completa}")
        return {}
        
    except json.JSONDecodeError:
        mensaje = f"\n{Fore.RED}❌ 🚫 Error: El archivo {ruta_completa} está corrupto o tiene un formato inválido"
        print(mensaje)
        print(f"{Fore.CYAN}📂 Se iniciará con una base de datos vacía.{Style.RESET_ALL}\n")
        logging.error(f"Error al decodificar JSON en {ruta_completa}")
        return {}
        
    except Exception as e:
        mensaje = f"\n{Fore.RED}❌ ⚠️ Error inesperado al cargar {ruta_completa}:"
        print(mensaje)
        print(f"{Fore.CYAN}🔍 Detalles del error: {str(e)}{Style.RESET_ALL}\n")
        logging.error(f"Error inesperado al cargar {ruta_completa}: {str(e)}")
        return {}

def guardar_datos(datos: Dict[str, Any], archivo: str) -> bool:
    """
    Función para guardar datos en un archivo JSON.
    
    Args:
        datos (Dict[str, Any]): Datos a guardar
        archivo (str): Ruta del archivo donde se guardarán los datos
        
    Returns:
        bool: True si se guardó exitosamente, False en caso contrario
    """
    if not validar_datos(datos):
        print(f"\n{Fore.RED}❌ 🚫 Error: Los datos deben ser un diccionario{Style.RESET_ALL}\n")
        logging.error("Intento de guardar datos que no son un diccionario")
        return False
        
    ruta_completa = obtener_ruta_archivo(archivo)
    
    try:
        # Asegurarse de que el directorio existe
        os.makedirs(os.path.dirname(ruta_completa), exist_ok=True)
        
        if datos:
            with open(ruta_completa, "w", encoding='utf-8') as file:
                json.dump(datos, file, indent=4, ensure_ascii=False)
            logging.info(f"Datos guardados exitosamente en {ruta_completa}")
            print(f"\n{Fore.GREEN}✅ Datos guardados exitosamente en: {ruta_completa}{Style.RESET_ALL}\n")
            return True
        else:
            print(f"\n{Fore.YELLOW}⚠️ 📂 Advertencia: No hay datos para guardar en {ruta_completa}{Style.RESET_ALL}\n")
            logging.warning(f"No hay datos para guardar en {ruta_completa}")
            return False
            
    except Exception as e:
        mensaje = f"\n{Fore.RED}❌ ⚠️ Error al guardar datos en {ruta_completa}:"
        print(mensaje)
        print(f"{Fore.CYAN}🔍 Detalles del error: {str(e)}{Style.RESET_ALL}\n")
        logging.error(f"Error al guardar datos en {ruta_completa}: {str(e)}")
        return False