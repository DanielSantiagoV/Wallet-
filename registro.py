"""
User registration module for Campers Wallet application.
Handles user registration with improved validation and security.
"""

from datetime import datetime
from typing import Dict, Any
import data
import config
from utils import (
    hash_password, validate_email, validate_password_strength, 
    get_valid_input, print_success, print_error, print_warning, print_info
)


def registro() -> None:
    """
    Main function for user registration.
    Validates and stores user information in the system with improved security.
    """
    print_info("=== REGISTRO DE USUARIO ===")
    
    # Load existing users
    registros = data.load_data("users")
    
    # Get and validate name
    nombre = get_valid_input("Ingrese su nombre completo: ", "str")
    if not nombre:
        print_error("El nombre no puede estar vacío.")
        return
    
    # Clean and validate name
    nom = nombre.replace(" ", "").lower()
    
    if len(nom) < config.MIN_NAME_LENGTH:
        print_error(f"El nombre debe tener al menos {config.MIN_NAME_LENGTH} caracteres.")
        return
    
    if not nom.isalpha():
        print_error("El nombre solo debe contener letras.")
        return
    
    # Check if user already exists
    if nom in registros:
        print_error("El nombre ya está registrado.")
        return
    
    # Get and validate age
    edad = get_valid_input("Ingrese su edad: ", "int", min_value=1)
    if edad < config.MIN_AGE:
        print_error(f"Debe ser mayor de {config.MIN_AGE} años para continuar con el registro.")
        return
    
    # Get and validate email
    correo = get_valid_input("Ingrese su correo electrónico: ", "str")
    if not validate_email(correo):
        print_error("El formato del correo electrónico no es válido.")
        return
    
    # Check if email is already registered
    for user_data in registros.values():
        if user_data.get("Correo", "").lower() == correo.lower():
            print_error("Este correo electrónico ya está registrado.")
            return
    
    # Get username
    usuario = get_valid_input("Ingrese su usuario: ", "str")
    if not usuario:
        print_error("El usuario no puede estar vacío.")
        return
    
    # Check if username is already taken
    for user_data in registros.values():
        if user_data.get("Usuario", "").lower() == usuario.lower():
            print_error("Este usuario ya está en uso.")
            return
    
    # Get and validate password
    print_info("La contraseña debe cumplir con los siguientes requisitos:")
    print_info(f"- Tener al menos {config.MIN_PASSWORD_LENGTH} caracteres.")
    print_info("- Incluir al menos un número.")
    print_info("- Incluir al menos una letra mayúscula.")
    print_info("- Incluir al menos una letra minúscula.")
    
    while True:
        contrasenia = get_valid_input("Ingrese una contraseña: ", "str")
        
        is_valid, error_message = validate_password_strength(contrasenia)
        if is_valid:
            break
        else:
            print_error(error_message)
    
    # Hash the password before storing
    contrasenia_hash = hash_password(contrasenia)
    
    # Create user record
    registros[nom] = {
        "Nombre": nombre,
        "Edad": edad,
        "Correo": correo,
        "Usuario": usuario,
        "Contraseña": contrasenia_hash,
        "Fecha_Registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Save user data
    if data.save_data(registros, "users"):
        print_success(f"Registro exitoso. ¡Bienvenido, {nombre}!")
        print_info("Ya puede iniciar sesión con su usuario y contraseña.")
    else:
        print_error("Error al guardar el registro. Inténtelo de nuevo.")


def ver_gastos_ingresos_usuario(usuario_actual: str) -> None:
    """
    View user's expenses and income for a specific month and year.
    
    Args:
        usuario_actual (str): Current user's name
    """
    movimientos_registrados = data.load_data("transactions")
    
    if usuario_actual not in movimientos_registrados or not movimientos_registrados[usuario_actual]:
        print_warning("No tienes movimientos registrados.")
        return
    
    try:
        mes = get_valid_input("Ingrese el mes que desea consultar (1-12): ", "int", min_value=1, max_value=12)
        año = get_valid_input("Ingrese el año que desea consultar (YYYY): ", "int", min_value=2000, max_value=2100)
        
        total_gastos = 0
        total_ingresos = 0
        movimientos_mes = []
        
        for mov in movimientos_registrados[usuario_actual]:
            fecha_str = mov.get("Fecha", "")
            monto = mov.get("Monto", 0)
            tipo = mov.get("Tipo", "").lower()
            
            try:
                fecha_movimiento = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
                if fecha_movimiento.month == mes and fecha_movimiento.year == año:
                    if "retiro" in tipo or "pago" in tipo or "transferencia" in tipo:
                        total_gastos += monto
                    elif "depósito" in tipo or "ingreso" in tipo:
                        total_ingresos += monto
                    
                    movimientos_mes.append(mov)
            except ValueError:
                print_warning(f"Error al procesar la fecha: {fecha_str}")
        
        if not movimientos_mes:
            print_warning(f"No hay movimientos registrados para {mes}/{año}.")
            return
        
        print_info(f"=== Resumen de Gastos e Ingresos - {mes}/{año} ===")
        print_info(f"Usuario: {usuario_actual}")
        print_success(f"Total Ingresado: ${total_ingresos:,.2f} COP")
        print_error(f"Total Gastado: ${total_gastos:,.2f} COP")
        
        balance = total_ingresos - total_gastos
        if balance >= 0:
            print_success(f"Balance: ${balance:,.2f} COP")
        else:
            print_error(f"Balance: ${balance:,.2f} COP")
        
        print_info("-" * 50)
        
        # Show recent transactions
        print_info("Movimientos del mes:")
        for i, mov in enumerate(movimientos_mes[-5:], 1):  # Show last 5 transactions
            fecha = mov.get("Fecha", "Desconocida")
            tipo = mov.get("Tipo", "Desconocido")
            monto = mov.get("Monto", 0)
            
            if "retiro" in tipo.lower() or "pago" in tipo.lower():
                print_error(f"{i}. {fecha} - {tipo}: -${monto:,.2f} COP")
            else:
                print_success(f"{i}. {fecha} - {tipo}: +${monto:,.2f} COP")
        
    except Exception as e:
        print_error(f"Error al procesar los datos: {str(e)}")