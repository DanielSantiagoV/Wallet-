from data import *
from datetime import datetime

def registro():
    """
    Función principal para el registro de nuevos usuarios.
    Valida y almacena la información del usuario en el sistema.
    """
    cargar_datos("registros.json")

    nombre = input("Ingrese su nombre completo: ").strip()
    nom = nombre.replace(" ", "").lower()

    if len(nom) < 3:
        print("Error. El nombre debe tener al menos 3 caracteres.")
        return
    
    if not nom.isalpha():
        print("Error. El nombre solo debe contener letras.")
        return

    if not nom:
        print("Error. El nombre no puede estar vacío.")
        return
    
    if nom in registros:
        print("Error. El nombre ya está registrado.")
        return

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad <= 0:
                raise ValueError("La edad debe ser mayor a 0.")
            break
        except ValueError:
            print("Error: Debe ingresar un número positivo.")

    if edad < 18:
        print("Lo sentimos. Debe ser mayor de edad para continuar con el registro.")
        return

    correo = input("Ingrese su correo electrónico: ").strip()
    usuario = input("Ingrese su usuario: ").strip()

    print("\nLa contraseña debe cumplir con los siguientes requisitos:")
    print("- Tener al menos 8 caracteres.")
    print("- Incluir al menos un número.")
    print("- Incluir al menos una letra mayúscula.")
    print("- Incluir al menos una letra minúscula.\n")

    while True:
        contrasenia = input("Ingrese una contraseña: ")

        if len(contrasenia) < 8:
            print("Error. La contraseña debe tener al menos 8 caracteres.")
        elif not any(char.isdigit() for char in contrasenia):
            print("Error. La contraseña debe contener al menos un número.")
        elif not any(char.isupper() for char in contrasenia):
            print("Error. La contraseña debe contener al menos una letra mayúscula.")
        elif not any(char.islower() for char in contrasenia):
            print("Error. La contraseña debe contener al menos una letra minúscula.")
        else:
            print(f"***** Registro Exitoso. Bienvenido, {nombre} *****")
            break

    registros_actuales = cargar_datos("registros.json")
    if not registros_actuales:
        registros_actuales = {}

    registros_actuales[nom] = {
        "Edad": edad,
        "Correo": correo,
        "Usuario": usuario,
        "Contraseña": contrasenia
    }
    guardar_datos(registros_actuales, "registros.json")

def ver_gastos_ingresos_usuario(usuario_actual):
    movimientos_registrados = cargar_datos("transacciones/movimientos.json")

    if usuario_actual not in movimientos_registrados or not movimientos_registrados[usuario_actual]:
        print("\nNo tienes movimientos registrados.")
        return

    try:
        mes = int(input("Ingrese el mes que desea consultar (1-12): "))
        año = int(input("Ingrese el año que desea consultar (YYYY): "))

        if mes < 1 or mes > 12:
            print("Error: El mes debe estar entre 1 y 12.")
            return

        total_gastos = 0
        total_ingresos = 0

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
            except ValueError:
                print(f"Error al procesar la fecha: {fecha_str}")

        print(f"\n***** Resumen de Gastos e Ingresos - {mes}/{año} *****")
        print(f"Usuario: {usuario_actual}")
        print(f"Total Gastado: ${total_gastos:.2f} COP")
        print(f"Total Ingresado: ${total_ingresos:.2f} COP")
        print("-" * 40)

    except ValueError:
        print("Error: Debe ingresar un número válido para el mes y el año.")