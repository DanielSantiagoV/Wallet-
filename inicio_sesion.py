"""
User login module for Campers Wallet application.
Handles user authentication with improved security and validation.
"""

from typing import Optional
import data
from utils import verify_password, get_valid_input, print_success, print_error, print_warning, print_info


def inicio_sesion() -> None:
    """
    Main function for user login.
    Verifies user credentials and allows access to the system.
    """
    print_info("=== INICIO DE SESIÓN ===")
    
    # Load registered users
    registros = data.load_data("users")
    
    # Check if there are any registered users
    if not registros:
        print_warning("No hay usuarios registrados. Por favor, regístrese primero.")
        return
    
    # Get username
    usuario = get_valid_input("Ingrese su usuario: ", "str")
    if not usuario:
        print_error("El usuario no puede estar vacío.")
        return
    
    # Find user by username
    usuario_actual = None
    for nombre, datos in registros.items():
        if datos.get("Usuario", "").strip().lower() == usuario.lower():
            usuario_actual = nombre
            break
    
    # Verify user exists
    if not usuario_actual:
        print_error("Usuario no encontrado. Primero debe registrarse.")
        return
    
    # Get password
    contrasenia = get_valid_input("Ingrese su contraseña: ", "str")
    if not contrasenia:
        print_error("La contraseña no puede estar vacía.")
        return
    
    # Verify password
    stored_password_hash = registros[usuario_actual].get("Contraseña", "")
    if not stored_password_hash:
        print_error("Error: Contraseña no encontrada en el sistema.")
        return
    
    if verify_password(contrasenia, stored_password_hash):
        print_success(f"Inicio de sesión exitoso. ¡Bienvenido de nuevo, {usuario_actual}!")
        
        # Import and execute main menu after successful login
        from utilidades_menu import ejecucion_menu_inicio
        ejecucion_menu_inicio(usuario_actual)
    else:
        print_error("Contraseña incorrecta.")
 