"""
Currency conversion module for Campers Wallet application.
Provides functions to convert COP to various currencies using external API.
"""

import requests
from typing import Optional
import config
from utils import get_valid_input, print_success, print_error, print_info

#Instalar la API de requests con el siguiente comando:
#pip install requests
#Una API ​ es una pieza de código que permite a dos aplicaciones comunicarse 
#entre sí para compartir información y funcionalidades. Se usan generalmente 
#en bibliotecas de programación.​

def convert_currency(amount_cop: float, target_currency: str) -> Optional[float]:
    """
    Convert COP to target currency using exchange rate API.
    
    Args:
        amount_cop (float): Amount in COP to convert
        target_currency (str): Target currency code (USD, EUR, etc.)
        
    Returns:
        Optional[float]: Converted amount or None if error
    """
    try:
        response = requests.get(config.EXCHANGE_RATE_API_URL, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        data = response.json()
        
        if target_currency not in data.get("rates", {}):
            print_error(f"Moneda {target_currency} no soportada.")
            return None
        
        exchange_rate = data["rates"][target_currency]
        converted_amount = amount_cop * exchange_rate
        
        return converted_amount
        
    except requests.exceptions.RequestException as e:
        print_error(f"Error de conexión: {str(e)}")
        print_info("Verifique su conexión a internet e inténtelo de nuevo.")
        return None
    except (KeyError, ValueError) as e:
        print_error(f"Error al procesar la respuesta de la API: {str(e)}")
        return None
    except Exception as e:
        print_error(f"Error inesperado: {str(e)}")
        return None


def get_currency_conversion_input(target_currency: str, currency_name: str) -> None:
    """
    Get user input and perform currency conversion.
    
    Args:
        target_currency (str): Target currency code
        currency_name (str): Human-readable currency name
    """
    print_info(f"=== Conversión COP a {target_currency} ({currency_name}) ===")
    
    # Get amount from user
    amount_cop = get_valid_input(
        f"Ingrese el monto en COP a convertir: ", 
        "float", 
        min_value=0.01
    )
    
    if amount_cop is None:
        return
    
    # Perform conversion
    converted_amount = convert_currency(amount_cop, target_currency)
    
    if converted_amount is not None:
        print_success(f"{amount_cop:,.2f} COP equivale a {converted_amount:,.2f} {target_currency}")
    else:
        print_error("No se pudo realizar la conversión.")


def convertir_cop_a_usd() -> None:
    """Convert COP to USD."""
    get_currency_conversion_input("USD", "Dólar Estadounidense")


def convertir_cop_a_eur() -> None:
    """Convert COP to EUR."""
    get_currency_conversion_input("EUR", "Euro")


def convertir_cop_a_gbp() -> None:
    """Convert COP to GBP."""
    get_currency_conversion_input("GBP", "Libra Esterlina")


def convertir_cop_a_jpy() -> None:
    """Convert COP to JPY."""
    get_currency_conversion_input("JPY", "Yen Japonés")


def convertir_cop_a_cad() -> None:
    """Convert COP to CAD."""
    get_currency_conversion_input("CAD", "Dólar Canadiense")


def get_exchange_rates() -> Optional[dict]:
    """
    Get current exchange rates for all supported currencies.
    
    Returns:
        Optional[dict]: Dictionary with exchange rates or None if error
    """
    try:
        response = requests.get(config.EXCHANGE_RATE_API_URL, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        rates = data.get("rates", {})
        
        # Filter only supported currencies
        supported_rates = {
            currency: rates.get(currency, 0) 
            for currency in config.SUPPORTED_CURRENCIES 
            if currency in rates
        }
        
        return supported_rates
        
    except Exception as e:
        print_error(f"Error al obtener tasas de cambio: {str(e)}")
        return None


def show_all_exchange_rates() -> None:
    """Display current exchange rates for all supported currencies."""
    print_info("=== Tasas de Cambio Actuales ===")
    
    rates = get_exchange_rates()
    if rates:
        for currency, rate in rates.items():
            print_info(f"1 COP = {rate:.6f} {currency}")
    else:
        print_error("No se pudieron obtener las tasas de cambio.")