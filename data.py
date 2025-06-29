"""
Data handling module for Campers Wallet application.
Provides functions for loading and saving data with proper error handling.
"""

import json
import os
import logging
import tempfile
import shutil
from typing import Dict, Any, Optional
from pathlib import Path
from colorama import Fore, Style
import config
from utils import print_success, print_error, print_warning, print_info

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=config.LOG_FILE
)

# Global variables for caching data
_registry_cache: Dict[str, Any] = {}
_accounts_cache: Dict[str, Any] = {}
_transactions_cache: Dict[str, Any] = {}
_pockets_cache: Dict[str, Any] = {}


def get_file_path(file_type: str) -> Path:
    """
    Get the file path for a specific data type.
    
    Args:
        file_type (str): Type of data file ("users", "accounts", "transactions", "pockets")
        
    Returns:
        Path: Full path to the data file
    """
    file_paths = {
        "users": config.USERS_FILE,
        "accounts": config.ACCOUNTS_FILE,
        "registered_accounts": config.REGISTERED_ACCOUNTS_FILE,
        "transactions": config.TRANSACTIONS_FILE,
        "pockets": config.POCKETS_FILE
    }
    
    if file_type not in file_paths:
        raise ValueError(f"Unknown file type: {file_type}")
    
    return file_paths[file_type]


def ensure_directory_exists(file_path: Path) -> None:
    """
    Ensure the directory for a file exists.
    
    Args:
        file_path (Path): Path to the file
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)


def validate_data(data: Any) -> bool:
    """
    Validate that data is a dictionary.
    
    Args:
        data (Any): Data to validate
        
    Returns:
        bool: True if data is valid, False otherwise
    """
    if not isinstance(data, dict):
        logging.error(f"Invalid data type: {type(data)}, expected dict")
        return False
    return True


def load_data(file_type: str, use_cache: bool = True) -> Dict[str, Any]:
    """
    Load data from a JSON file with caching and error handling.
    
    Args:
        file_type (str): Type of data file to load
        use_cache (bool): Whether to use cached data if available
        
    Returns:
        Dict[str, Any]: Loaded data or empty dict if error
    """
    # Check cache first
    cache_map = {
        "users": _registry_cache,
        "accounts": _accounts_cache,
        "registered_accounts": _accounts_cache,  # Same cache as accounts
        "transactions": _transactions_cache,
        "pockets": _pockets_cache
    }
    
    if use_cache and file_type in cache_map and cache_map[file_type]:
        return cache_map[file_type].copy()
    
    file_path = get_file_path(file_type)
    
    try:
        if not file_path.exists():
            logging.warning(f"File not found: {file_path}")
            print_warning(f"Archivo no encontrado: {file_path.name}")
            print_info("Se iniciará con una base de datos vacía.")
            return {}
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        if not validate_data(data):
            raise ValueError("Invalid data format")
        
        # Update cache
        if file_type in cache_map:
            cache_map[file_type] = data.copy()
        
        logging.info(f"Data loaded successfully from {file_path}")
        return data
        
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error in {file_path}: {e}")
        print_error(f"Error: El archivo {file_path.name} está corrupto")
        print_info("Se iniciará con una base de datos vacía.")
        return {}
        
    except Exception as e:
        logging.error(f"Unexpected error loading {file_path}: {e}")
        print_error(f"Error inesperado al cargar {file_path.name}")
        print_info("Se iniciará con una base de datos vacía.")
        return {}


def save_data(data: Dict[str, Any], file_type: str, atomic: bool = True) -> bool:
    """
    Save data to a JSON file with atomic write support.
    
    Args:
        data (Dict[str, Any]): Data to save
        file_type (str): Type of data file to save
        atomic (bool): Whether to use atomic write (recommended)
        
    Returns:
        bool: True if save was successful, False otherwise
    """
    if not validate_data(data):
        print_error("Error: Los datos deben ser un diccionario")
        return False
    
    file_path = get_file_path(file_type)
    ensure_directory_exists(file_path)
    
    try:
        if atomic:
            # Atomic write using temporary file
            with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
                json.dump(data, temp_file, indent=4, ensure_ascii=False)
                temp_file_path = temp_file.name
            
            # Move temporary file to final location
            shutil.move(temp_file_path, file_path)
        else:
            # Direct write (not atomic)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        
        # Update cache
        cache_map = {
            "users": _registry_cache,
            "accounts": _accounts_cache,
            "registered_accounts": _accounts_cache,
            "transactions": _transactions_cache,
            "pockets": _pockets_cache
        }
        
        if file_type in cache_map:
            cache_map[file_type] = data.copy()
        
        logging.info(f"Data saved successfully to {file_path}")
        print_success(f"Datos guardados exitosamente en {file_path.name}")
        return True
        
    except Exception as e:
        logging.error(f"Error saving data to {file_path}: {e}")
        print_error(f"Error al guardar datos en {file_path.name}")
        return False


def clear_cache(file_type: Optional[str] = None) -> None:
    """
    Clear the data cache.
    
    Args:
        file_type (Optional[str]): Specific cache to clear, or None for all
    """
    if file_type is None:
        global _registry_cache, _accounts_cache, _transactions_cache, _pockets_cache
        _registry_cache.clear()
        _accounts_cache.clear()
        _transactions_cache.clear()
        _pockets_cache.clear()
        logging.info("All caches cleared")
    else:
        cache_map = {
            "users": _registry_cache,
            "accounts": _accounts_cache,
            "registered_accounts": _accounts_cache,
            "transactions": _transactions_cache,
            "pockets": _pockets_cache
        }
        
        if file_type in cache_map:
            cache_map[file_type].clear()
            logging.info(f"Cache cleared for {file_type}")


# Backward compatibility functions
def cargar_datos(archivo: str) -> Dict[str, Any]:
    """
    Legacy function for loading data (maintains backward compatibility).
    
    Args:
        archivo (str): File path (legacy format)
        
    Returns:
        Dict[str, Any]: Loaded data
    """
    # Map legacy file paths to new file types
    file_mapping = {
        "registros.json": "users",
        "gestion_cuentas/cuentas.json": "accounts",
        "gestion_cuentas/cuentas_registradas.json": "registered_accounts",
        "transacciones/movimientos.json": "transactions",
        "bolsillos/bolsillos.json": "pockets"
    }
    
    file_type = file_mapping.get(archivo, "users")
    return load_data(file_type)


def guardar_datos(datos: Dict[str, Any], archivo: str) -> bool:
    """
    Legacy function for saving data (maintains backward compatibility).
    
    Args:
        datos (Dict[str, Any]): Data to save
        archivo (str): File path (legacy format)
        
    Returns:
        bool: True if save was successful
    """
    # Map legacy file paths to new file types
    file_mapping = {
        "registros.json": "users",
        "gestion_cuentas/cuentas.json": "accounts",
        "gestion_cuentas/cuentas_registradas.json": "registered_accounts",
        "transacciones/movimientos.json": "transactions",
        "bolsillos/bolsillos.json": "pockets"
    }
    
    file_type = file_mapping.get(archivo, "users")
    return save_data(datos, file_type)