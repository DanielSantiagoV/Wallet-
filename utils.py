"""
Utility functions for Campers Wallet application.
Contains common functions for validation, security, and user interaction.
"""

import hashlib
import re
from typing import Optional, Union
from colorama import Fore, Style
import config


def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256.
    
    Args:
        password (str): Plain text password
        
    Returns:
        str: Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash.
    
    Args:
        password (str): Plain text password to verify
        hashed_password (str): Stored hash to compare against
        
    Returns:
        bool: True if password matches hash, False otherwise
    """
    return hash_password(password) == hashed_password


def validate_email(email: str) -> bool:
    """
    Validate email format using regex.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if email is valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    Validate password strength requirements.
    
    Args:
        password (str): Password to validate
        
    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if len(password) < config.MIN_PASSWORD_LENGTH:
        return False, f"La contraseña debe tener al menos {config.MIN_PASSWORD_LENGTH} caracteres."
    
    if not any(char.isdigit() for char in password):
        return False, "La contraseña debe contener al menos un número."
    
    if not any(char.isupper() for char in password):
        return False, "La contraseña debe contener al menos una letra mayúscula."
    
    if not any(char.islower() for char in password):
        return False, "La contraseña debe contener al menos una letra minúscula."
    
    return True, ""


def get_valid_input(prompt: str, input_type: str = "str", min_value: Optional[Union[int, float]] = None, 
                   max_value: Optional[Union[int, float]] = None, allow_empty: bool = False) -> Union[str, int, float]:
    """
    Get and validate user input.
    
    Args:
        prompt (str): Input prompt to display
        input_type (str): Type of input expected ("str", "int", "float")
        min_value: Minimum allowed value (for numeric inputs)
        max_value: Maximum allowed value (for numeric inputs)
        allow_empty (bool): Whether empty input is allowed
        
    Returns:
        Union[str, int, float]: Validated user input
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            if not user_input and not allow_empty:
                print(f"{Fore.RED}❌ Error: No se puede dejar vacío.{Style.RESET_ALL}")
                continue
            
            if not user_input and allow_empty:
                return user_input
            
            if input_type == "int":
                value = int(user_input)
            elif input_type == "float":
                value = float(user_input)
            else:
                value = user_input
            
            if min_value is not None and value < min_value:
                print(f"{Fore.RED}❌ Error: El valor debe ser mayor o igual a {min_value}.{Style.RESET_ALL}")
                continue
                
            if max_value is not None and value > max_value:
                print(f"{Fore.RED}❌ Error: El valor debe ser menor o igual a {max_value}.{Style.RESET_ALL}")
                continue
            
            return value
            
        except ValueError:
            print(f"{Fore.RED}❌ Error: Debe ingresar un valor válido.{Style.RESET_ALL}")


def confirm_action(prompt: str = "¿Está seguro? (S/N): ") -> bool:
    """
    Get user confirmation for an action.
    
    Args:
        prompt (str): Confirmation prompt
        
    Returns:
        bool: True if user confirms, False otherwise
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print(f"{Fore.YELLOW}⚠️ Por favor responda S/N.{Style.RESET_ALL}")


def format_currency(amount: float, currency: str = "COP") -> str:
    """
    Format currency amount with proper formatting.
    
    Args:
        amount (float): Amount to format
        currency (str): Currency code
        
    Returns:
        str: Formatted currency string
    """
    return f"${amount:,.2f} {currency}"


def clear_screen():
    """Clear the console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def print_success(message: str):
    """Print a success message with green color."""
    print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


def print_error(message: str):
    """Print an error message with red color."""
    print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}")


def print_warning(message: str):
    """Print a warning message with yellow color."""
    print(f"{Fore.YELLOW}⚠️ {message}{Style.RESET_ALL}")


def print_info(message: str):
    """Print an info message with cyan color."""
    print(f"{Fore.CYAN}ℹ️ {message}{Style.RESET_ALL}") 