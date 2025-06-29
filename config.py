"""
Configuration file for Campers Wallet application.
Contains all settings, file paths, and constants.
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# File paths
USERS_FILE = BASE_DIR / "usuarios" / "registros.json"
ACCOUNTS_FILE = BASE_DIR / "gestion_cuentas" / "cuentas.json"
REGISTERED_ACCOUNTS_FILE = BASE_DIR / "gestion_cuentas" / "cuentas_registradas.json"
TRANSACTIONS_FILE = BASE_DIR / "transacciones" / "movimientos.json"
POCKETS_FILE = BASE_DIR / "bolsillos" / "bolsillos.json"
LOG_FILE = BASE_DIR / "app.log"

# API Configuration
EXCHANGE_RATE_API_URL = "https://api.exchangerate-api.com/v4/latest/COP"
SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "CAD"]

# Application Settings
MIN_PASSWORD_LENGTH = 8
MIN_AGE = 18
MIN_NAME_LENGTH = 3

# Menu options
MAIN_MENU_OPTIONS = {
    1: "Iniciar Sesión",
    2: "Registrarse", 
    3: "Salir"
}

DASHBOARD_MENU_OPTIONS = {
    1: "Gestión de Cuentas",
    2: "Transacciones",
    3: "Bolsillos",
    4: "Conversión de Divisas",
    5: "Cerrar Sesión"
}

# Transaction types
TRANSACTION_TYPES = {
    "PAYMENT": "Pago",
    "WITHDRAWAL": "Retiro", 
    "DEPOSIT": "Depósito",
    "TRANSFER": "Transferencia"
}

# Status types
STATUS_TYPES = {
    "APPROVED": "Aprobado",
    "PENDING": "Pendiente",
    "REJECTED": "Rechazado"
} 