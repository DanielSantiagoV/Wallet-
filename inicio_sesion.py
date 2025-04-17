# Importación de módulos necesarios
from data import *  # Importa funciones de manejo de datos

def inicio_sesion():    
    """
    Función para manejar el proceso de inicio de sesión de usuarios.
    Verifica las credenciales y permite el acceso al sistema.
    """
    # Carga los datos de usuarios registrados
    registros = cargar_datos("registros.json")

    # Verifica si hay usuarios registrados
    if not registros:
        print("***** No hay usuarios registrados. Por favor, regístrese primero. *****")
        return  

    # Solicita credenciales al usuario
    print("\n***** INICIO DE SESIÓN *****")  
    usuario = input("Ingrese su usuario: ").strip()  

    # Busca el usuario en los registros
    usuario_actual = None  
    for nombre, datos in registros.items():  
        if datos["Usuario"].strip().lower() == usuario.lower():
            usuario_actual = nombre  
            break  

    # Verifica las credenciales
    if usuario_actual:  
        contrasenia = input("Ingrese su contraseña: ").strip()  
        if registros[usuario_actual]["Contraseña"] == contrasenia:  
            print(f"***** Inicio de sesión exitoso. Bienvenido de nuevo, {usuario_actual} *****")
            
            # Importa y ejecuta el menú principal después del inicio de sesión exitoso
            from utilidades_menu import ejecucion_menu_inicio  
            ejecucion_menu_inicio(usuario_actual)
        else:  
            print("***** Error: Contraseña incorrecta. *****")  
    else:  
        print("***** Usuario no encontrado. Primero debe registrarse. *****")  
 