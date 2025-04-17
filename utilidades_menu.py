# Importación de módulos necesarios para las funcionalidades del sistema
from registro import *  # Importa funciones de registro de usuarios para el proceso de registro
from inicio_sesion import inicio_sesion  # Importa función de inicio de sesión para autenticación
from gestion_cuentas.registro_cuentas import *  # Importa funciones de gestión de cuentas bancarias
from transacciones.transacciones import *  # Importa funciones de transacciones financieras
from bolsillos.bolsillos import *  # Importa funciones de gestión de bolsillos de ahorro
from divisas.divisas import *  # Importa funciones de conversión de divisas
from colorama import init, Fore, Back, Style  # Importa módulos para colores en consola

# Inicializa colorama
init()

# Definición de menús del sistema con sus opciones correspondientes
menu_principal = f"""
{Fore.CYAN}***** {Fore.YELLOW}💰 Bienvenido a Campers Wallet 💰{Fore.CYAN} *****{Style.RESET_ALL}
{Fore.GREEN}1. 👤 Iniciar Sesión{Style.RESET_ALL}
{Fore.GREEN}2. 📝 Registrarse{Style.RESET_ALL}
{Fore.GREEN}3. 🚪 Salir{Style.RESET_ALL}
{Fore.CYAN}***************************************{Style.RESET_ALL}
"""

menu_inicio = f"""
{Fore.CYAN}***************************************{Style.RESET_ALL}
{Fore.GREEN}1. 💳 Gestión de Cuentas{Style.RESET_ALL}
{Fore.GREEN}2. 💰 Transacciones{Style.RESET_ALL}
{Fore.GREEN}3. 🏦 Bolsillos{Style.RESET_ALL}
{Fore.GREEN}4. 💱 Conversión de Divisas{Style.RESET_ALL}
{Fore.GREEN}5. 👋 Cerrar Sesión{Style.RESET_ALL}
{Fore.CYAN}***************************************{Style.RESET_ALL}
"""

menu_gestion_cuentas = f"""
{Fore.CYAN}***************************************{Style.RESET_ALL}
{Fore.GREEN}1. 📝 Registrar Cuenta{Style.RESET_ALL}
{Fore.GREEN}2. ✏️ Modificar Cuenta{Style.RESET_ALL}
{Fore.GREEN}3. 🗑️ Eliminar Cuenta{Style.RESET_ALL}
{Fore.GREEN}4. 👀 Ver Cuentas Registradas{Style.RESET_ALL}
{Fore.GREEN}5. 📊 Ver Gastos/Ingresos{Style.RESET_ALL}
{Fore.GREEN}6. 💵 Saldo Total{Style.RESET_ALL}
{Fore.GREEN}7. ↩️ Regresar al menú principal{Style.RESET_ALL}
{Fore.CYAN}***************************************{Style.RESET_ALL}
"""

menu_transacciones = f"""
{Fore.CYAN}***************************************{Style.RESET_ALL}
{Fore.GREEN}1. 💸 Realizar pagos{Style.RESET_ALL}
{Fore.GREEN}2. 💰 Retirar dinero{Style.RESET_ALL}
{Fore.GREEN}3. 📥 Depositar dinero{Style.RESET_ALL}
{Fore.GREEN}4. 📋 Movimientos{Style.RESET_ALL}
{Fore.GREEN}5. ↩️ Regresar menu principal{Style.RESET_ALL}
{Fore.CYAN}***************************************{Style.RESET_ALL}
"""

menu_bolsillos = f"""
{Fore.CYAN}***************************************{Style.RESET_ALL}
{Fore.GREEN}1. ➕ Crear bolsillo{Style.RESET_ALL}
{Fore.GREEN}2. 💰 Agregar dinero a bolsillo{Style.RESET_ALL}
{Fore.GREEN}3. 💸 Retirar dinero de bolsillo{Style.RESET_ALL}
{Fore.GREEN}4. 🗑️ Eliminar bolsillo{Style.RESET_ALL}
{Fore.GREEN}5. 👀 Ver bolsillos{Style.RESET_ALL}
{Fore.GREEN}6. ↩️ Regresar menu principal{Style.RESET_ALL}
{Fore.CYAN}***************************************{Style.RESET_ALL}
"""

menu_conversion_divisas = f"""
{Fore.CYAN}***************************************{Style.RESET_ALL}
{Fore.GREEN}1. 🇺🇸 Convertir de COP a USD (Dolar){Style.RESET_ALL}
{Fore.GREEN}2. 🇪🇺 Convertir de COP a EUR (Euros){Style.RESET_ALL}
{Fore.GREEN}3. 🇬🇧 Convertir de COP a GBP (Libras Esterlinas){Style.RESET_ALL}
{Fore.GREEN}4. 🇯🇵 Convertir de COP a JPY (Yenes Japoneses){Style.RESET_ALL}
{Fore.GREEN}5. 🇨🇦 Convertir de COP a CAD (Dolares Canadienses){Style.RESET_ALL}
{Fore.GREEN}6. ↩️ Regresar menu principal{Style.RESET_ALL}
{Fore.CYAN}***************************************{Style.RESET_ALL}
"""

# Funciones para mostrar los diferentes menús del sistema
def mostrar_menu():
    return print(menu_principal)  # Muestra el menú principal en la consola

def mostrar_menu_inicio():
    return print(menu_inicio)  # Muestra el menú después del inicio de sesión

def mostrar_menu_gestion_cuentas():
    return print(menu_gestion_cuentas)  # Muestra el menú de gestión de cuentas

def mostrar_menu_transacciones():
    return print(menu_transacciones)  # Muestra el menú de transacciones

def mostrar_menu_bolsillos():
    return print(menu_bolsillos)  # Muestra el menú de bolsillos

def mostrar_menu_conversion_divisas():
    return print(menu_conversion_divisas)  # Muestra el menú de conversión de divisas

# Función para solicitar la opción al usuario
def pedir_opcion():
    return int(input("Bienvenido. Elija una opción: "))  # Solicita y retorna la opción elegida por el usuario

# Función principal que maneja el menú principal
def ejecucion_menu_principal():
    while True:  # Bucle infinito para mantener el menú activo
        mostrar_menu()  # Muestra el menú principal
        try:
            opc = pedir_opcion()  # Solicita la opción al usuario
        except ValueError:
            print("Error: Debe ingresar una opción válida.")  # Maneja errores de entrada
            continue
        match opc:  # Estructura de control para las diferentes opciones
            case 1:
                inicio_sesion()  # Llama a la función de inicio de sesión
            case 2:
                registro()  # Llama a la función de registro
            case 3:
                print("Saliendo...")  # Mensaje de salida
                break  # Termina el bucle y cierra el programa
            case _:
                print("Error. Elija una opcion válida")  # Mensaje para opciones inválidas

# Función que maneja el menú después del inicio de sesión
def ejecucion_menu_inicio(usuario_actual):
    while True:  # Bucle para mantener el menú activo
        mostrar_menu_inicio()  # Muestra el menú de inicio
        try:
            opc_inicio = pedir_opcion()  # Solicita la opción al usuario
        except ValueError:
            print("Error: Debe ingresar una opción válida.")  # Maneja errores de entrada
            continue
        match opc_inicio:  # Estructura de control para las diferentes opciones
            case 1:
                ejecucion_menu_gestion_cuentas(usuario_actual)  # Llama al menú de gestión de cuentas
            case 2:
                ejecucion_menu_transacciones(usuario_actual)  # Llama al menú de transacciones
            case 3:
                ejecucion_menu_bolsillos(usuario_actual)  # Llama al menú de bolsillos
            case 4:
                ejecucion_menu_conversion_divisas()  # Llama al menú de conversión de divisas
            case 5:
                print("Cerrando sesión...")  # Mensaje de cierre de sesión
                break  # Termina el bucle y cierra la sesión
            case _:
                print("Error. Elija una opcion válida")  # Mensaje para opciones inválidas

# Función que maneja el menú de gestión de cuentas
def ejecucion_menu_gestion_cuentas(usuario_actual):
    while True:  # Bucle para mantener el menú activo
        mostrar_menu_gestion_cuentas()  # Muestra el menú de gestión de cuentas
        try:
            opc_gestion_cuentas = pedir_opcion()  # Solicita la opción al usuario
        except ValueError:
            print("Error: Debe ingresar una opción válida.")  # Maneja errores de entrada
            continue
        match opc_gestion_cuentas:  # Estructura de control para las diferentes opciones
            case 1:
                registrar_cuentas(usuario_actual)  # Llama a la función de registro de cuentas
            case 2:
                modificar_cuenta(usuario_actual)  # Llama a la función de modificación de cuentas
            case 3:
                eliminar_cuenta(usuario_actual)  # Llama a la función de eliminación de cuentas
            case 4:
                ver_cuentas_registradas(usuario_actual)  # Llama a la función de visualización de cuentas
            case 5:
                ver_gastos_ingresos_usuario(usuario_actual)  # Llama a la función de visualización de gastos/ingresos
            case 6:
                ver_saldo_total(usuario_actual)  # Llama a la función de visualización de saldo total
            case 7:
                break  # Regresa al menú anterior
            case _:
                print("Error. Elija una opcion válida")  # Mensaje para opciones inválidas

# Función que maneja el menú de transacciones
def ejecucion_menu_transacciones(usuario_actual):
    while True:  # Bucle para mantener el menú activo
        mostrar_menu_transacciones()  # Muestra el menú de transacciones
        try:
            opc_transacciones = pedir_opcion()  # Solicita la opción al usuario
        except ValueError:
            print("Error: Debe ingresar una opción válida.")  # Maneja errores de entrada
            continue
        match opc_transacciones:  # Estructura de control para las diferentes opciones
            case 1:
                realizar_pago(usuario_actual)  # Llama a la función de realización de pagos
            case 2:
                retirar_dinero(usuario_actual)  # Llama a la función de retiro de dinero
            case 3:
                depositar_dinero(usuario_actual)  # Llama a la función de depósito de dinero
            case 4:
                listar_movimientos(usuario_actual)  # Llama a la función de listado de movimientos
            case 5:
                break  # Regresa al menú anterior
            case _:
                print("Error. Elija una opcion válida")  # Mensaje para opciones inválidas

# Función que maneja el menú de bolsillos
def ejecucion_menu_bolsillos(usuario_actual):
    while True:  # Bucle para mantener el menú activo
        mostrar_menu_bolsillos()  # Muestra el menú de bolsillos
        try:
            opc_bolsillos = pedir_opcion()  # Solicita la opción al usuario
        except ValueError:
            print("Error: Debe ingresar una opción válida.")  # Maneja errores de entrada
            continue
        match opc_bolsillos:  # Estructura de control para las diferentes opciones
            case 1:
                crear_bolsillo(usuario_actual)  # Llama a la función de creación de bolsillos
            case 2:
                agregar_dinero_bolsillo(usuario_actual)  # Llama a la función de agregar dinero a bolsillos
            case 3:
                retirar_dinero_bolsillo(usuario_actual)  # Llama a la función de retiro de dinero de bolsillos
            case 4:
                eliminar_bolsillo(usuario_actual)  # Llama a la función de eliminación de bolsillos
            case 5:
                listar_bolsillos(usuario_actual)  # Llama a la función de listado de bolsillos
            case 6:
                break  # Regresa al menú anterior
            case _:
                print("Error. Elija una opcion válida")  # Mensaje para opciones inválidas

# Función que maneja el menú de conversión de divisas
def ejecucion_menu_conversion_divisas():
    while True:  # Bucle para mantener el menú activo
        mostrar_menu_conversion_divisas()  # Muestra el menú de conversión de divisas
        try:
            opc_conversion_divisas = pedir_opcion()  # Solicita la opción al usuario
        except ValueError:
            print("Error: Debe ingresar una opción válida.")  # Maneja errores de entrada
            continue
        match opc_conversion_divisas:  # Estructura de control para las diferentes opciones
            case 1:
                convertir_cop_a_usd()  # Llama a la función de conversión COP a USD
            case 2:
                convertir_cop_a_eur()  # Llama a la función de conversión COP a EUR
            case 3:
                convertir_cop_a_gbp()  # Llama a la función de conversión COP a GBP
            case 4:
                convertir_cop_a_jpy()  # Llama a la función de conversión COP a JPY
            case 5:
                convertir_cop_a_cad()  # Llama a la función de conversión COP a CAD
            case 6:
                break  # Regresa al menú anterior
            case _:
                print("Error. Elija una opcion válida")  # Mensaje para opciones inválidas