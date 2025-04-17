from data import *

def registrar_cuentas(usuario_actual):

    cuentas_disponibles = cargar_datos("gestion_cuentas/cuentas_registradas.json")
    if not cuentas_disponibles:
        print("No hay cuentas disponibles para registrar.")
        return
    
    print("\n***** Cuentas Disponibles *****")
    for i, cuenta in enumerate(cuentas_disponibles, 1):
        print(f"{i}. {cuenta}")
    
    try:
        opcion = int(input("Seleccione el número de la cuenta que desea registrar: "))
        if opcion < 1 or opcion > len(cuentas_disponibles):
            print("Opción inválida. Inténtelo de nuevo.")
            return
        
        cuenta_seleccionada = list(cuentas_disponibles.keys())[opcion - 1]
        numero = input("Digite su número de celular: ").strip()
        monto = float(input(f"Ingrese el monto inicial para {cuenta_seleccionada} en COP: "))

        cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

        if usuario_actual not in cuentas_registradas:
            cuentas_registradas[usuario_actual] = {}

        if cuenta_seleccionada in cuentas_registradas[usuario_actual]:
            print(f"Error. Ya tienes una cuenta {cuenta_seleccionada} registrada.")
        else:
            cuentas_registradas[usuario_actual][cuenta_seleccionada] = {
                "Número": numero,
                "Saldo": monto
            }
            guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")
            print(f"***** Cuenta {cuenta_seleccionada} registrada con éxito con un saldo de ${monto:.2f} COP. *****")
    
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def modificar_cuenta(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("No tienes cuentas registradas para modificar.")
        return

    print("\n***** Cuentas Registradas *****")
    cuentas_usuario = list(cuentas_registradas[usuario_actual].keys())

    for i, cuenta in enumerate(cuentas_usuario, 1):
        print(f"{i}. {cuenta}")

    try:
        opcion = int(input("Seleccione el número de la cuenta que desea modificar: "))
        if opcion < 1 or opcion > len(cuentas_usuario):
            print("Opción inválida. Inténtelo de nuevo.")
            return
        
        cuenta_seleccionada = cuentas_usuario[opcion - 1]
        print(f"\nModificando cuenta: {cuenta_seleccionada}")

        print("1. Modificar número de celular")
        print("2. Modificar saldo")
        print("3. Cancelar")
        seleccion = input("Seleccione qué desea modificar: ")

        if seleccion == "1":
            nuevo_numero = input("Ingrese el nuevo número de celular: ")
            cuentas_registradas[usuario_actual][cuenta_seleccionada]["Número"] = nuevo_numero
            print("Número de celular actualizado correctamente.")

        elif seleccion == "2":
            nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
            cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"] = nuevo_saldo
            print("Saldo actualizado correctamente.")

        elif seleccion == "3":
            print("Modificación cancelada.")
            return

        else:
            print("Opción inválida. Inténtelo de nuevo.")
            return

        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")
        print("***** Cuenta modificada con éxito *****")

    except ValueError:
        print("Error: Debe ingresar una opción válida.")

def eliminar_cuenta(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("No tienes cuentas registradas para eliminar.")
        return

    print("\n***** Cuentas Registradas *****")
    cuentas_usuario = list(cuentas_registradas[usuario_actual].keys())

    for i, cuenta in enumerate(cuentas_usuario, 1):
        print(f"{i}. {cuenta}")

    try:
        opcion = int(input("Seleccione el número de la cuenta que desea eliminar: "))
        if opcion < 1 or opcion > len(cuentas_usuario):
            print("Opción inválida. Inténtelo de nuevo.")
            return
        
        cuenta_seleccionada = cuentas_usuario[opcion - 1]
        
        confirmar = input(f"¿Está seguro de que desea eliminar la cuenta {cuenta_seleccionada}? (S/N): ").strip().lower()
        if confirmar == "s":
            del cuentas_registradas[usuario_actual][cuenta_seleccionada]

            if not cuentas_registradas[usuario_actual]:
                del cuentas_registradas[usuario_actual]

            guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")
            print(f"***** La cuenta {cuenta_seleccionada} ha sido eliminada con éxito. *****")
        else:
            print("Operación cancelada.")

    except ValueError:
        print("Error: Debe ingresar una opción válida.")

def ver_cuentas_registradas(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("***** No tienes cuentas registradas. *****")
        return

    print("\n***** Cuentas Registradas *****")
    for cuenta, datos in cuentas_registradas[usuario_actual].items():
        print(f"- {cuenta}: ${datos['Saldo']:.2f} COP")
        
def ver_saldo_total(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("***** No tienes cuentas registradas. *****")
        return

    saldo_total = sum(datos["Saldo"] for datos in cuentas_registradas[usuario_actual].values())

    print(f"\n***** Saldo Total *****\nTu saldo total es: ${saldo_total:.2f} COP")
