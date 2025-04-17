from data import *
from colorama import Fore, Style

def agregar_dinero_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print(f"\n{Fore.YELLOW}⚠️ No tienes bolsillos registrados.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}💰 Tus Bolsillos Registrados 💰{Style.RESET_ALL}")
    bolsillos_usuario = list(bolsillos[usuario_actual].keys())

    for i, bolsillo in enumerate(bolsillos_usuario, 1):
        monto = bolsillos[usuario_actual][bolsillo]["Monto"]
        cuenta_origen = bolsillos[usuario_actual][bolsillo]["Cuenta_origen"]
        print(f"{Fore.GREEN}{i}. {bolsillo} - Saldo: ${monto:.2f} COP - Cuenta Origen: {cuenta_origen}{Style.RESET_ALL}")

    try:
        opcion_bolsillo = int(input(f"\n{Fore.CYAN}👉 Seleccione el bolsillo al que desea agregar dinero: {Style.RESET_ALL}"))
        if opcion_bolsillo < 1 or opcion_bolsillo > len(bolsillos_usuario):
            print(f"\n{Fore.RED}❌ Error: Opción inválida{Style.RESET_ALL}")
            return

        bolsillo_seleccionado = bolsillos_usuario[opcion_bolsillo - 1]
        cuenta_origen = bolsillos[usuario_actual][bolsillo_seleccionado]["Cuenta_origen"]

        if usuario_actual not in cuentas_registradas or cuenta_origen not in cuentas_registradas[usuario_actual]:
            print(f"\n{Fore.RED}❌ Error: La cuenta origen '{cuenta_origen}' no está registrada{Style.RESET_ALL}")
            return

        saldo_disponible = cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"]

        print(f"\n{Fore.CYAN}💳 La única cuenta permitida para agregar dinero a este bolsillo es '{cuenta_origen}'")
        print(f"💰 Saldo disponible: ${saldo_disponible:.2f} COP{Style.RESET_ALL}")

        monto = float(input(f"\n{Fore.CYAN}💵 Ingrese el monto a agregar al bolsillo: {Style.RESET_ALL}"))

        if monto <= 0:
            print(f"\n{Fore.RED}❌ Error: El monto debe ser mayor que 0{Style.RESET_ALL}")
            return

        if monto > saldo_disponible:
            print(f"\n{Fore.RED}❌ Error: Fondos insuficientes{Style.RESET_ALL}")
            return

        cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"] -= monto
        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"] += monto
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        print(f"\n{Fore.GREEN}✅ Transacción exitosa")
        print(f"💰 Has agregado ${monto:.2f} COP al bolsillo '{bolsillo_seleccionado}'")
        print(f"💳 Nuevo saldo del bolsillo: ${bolsillos[usuario_actual][bolsillo_seleccionado]['Monto']:.2f} COP{Style.RESET_ALL}")

    except ValueError:
        print(f"\n{Fore.RED}❌ Error: Debe ingresar un número válido{Style.RESET_ALL}")

def retirar_dinero_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print(f"\n{Fore.YELLOW}⚠️ No tienes bolsillos registrados{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}💰 Tus Bolsillos Registrados 💰{Style.RESET_ALL}")
    bolsillos_usuario = list(bolsillos[usuario_actual].keys())

    for i, bolsillo in enumerate(bolsillos_usuario, 1):
        monto = bolsillos[usuario_actual][bolsillo]["Monto"]
        print(f"{Fore.GREEN}{i}. {bolsillo} - Saldo: ${monto:.2f} COP{Style.RESET_ALL}")

    try:
        opcion_bolsillo = int(input(f"\n{Fore.CYAN}👉 Seleccione el bolsillo del cual desea retirar dinero: {Style.RESET_ALL}"))
        if opcion_bolsillo < 1 or opcion_bolsillo > len(bolsillos_usuario):
            print(f"\n{Fore.RED}❌ Error: Opción inválida{Style.RESET_ALL}")
            return

        bolsillo_seleccionado = bolsillos_usuario[opcion_bolsillo - 1]
        saldo_bolsillo = bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"]
        cuenta_origen = bolsillos[usuario_actual][bolsillo_seleccionado]["Cuenta_origen"]

        monto = float(input(f"\n{Fore.CYAN}💵 Ingrese el monto a retirar: {Style.RESET_ALL}"))

        if monto <= 0:
            print(f"\n{Fore.RED}❌ Error: El monto debe ser mayor que 0{Style.RESET_ALL}")
            return

        if monto > saldo_bolsillo:
            print(f"\n{Fore.RED}❌ Error: Fondos insuficientes en el bolsillo{Style.RESET_ALL}")
            return

        bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"] -= monto
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"] += monto
        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        print(f"\n{Fore.GREEN}✅ Retiro exitoso")
        print(f"💰 Has retirado ${monto:.2f} COP del bolsillo '{bolsillo_seleccionado}'")
        print(f"💳 Nuevo saldo del bolsillo: ${bolsillos[usuario_actual][bolsillo_seleccionado]['Monto']:.2f} COP")
        print(f"💳 El dinero ha sido transferido de vuelta a la cuenta de origen '{cuenta_origen}'{Style.RESET_ALL}")

    except ValueError:
        print(f"\n{Fore.RED}❌ Error: Debe ingresar un número válido{Style.RESET_ALL}")

def eliminar_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print(f"\n{Fore.YELLOW}⚠️ No tienes bolsillos registrados para eliminar{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}💰 Tus Bolsillos Registrados 💰{Style.RESET_ALL}")
    bolsillos_usuario = list(bolsillos[usuario_actual].keys())

    for i, bolsillo in enumerate(bolsillos_usuario, 1):
        saldo = bolsillos[usuario_actual][bolsillo]["Monto"]
        print(f"{Fore.GREEN}{i}. {bolsillo} - Saldo: ${saldo:.2f} COP{Style.RESET_ALL}")

    try:
        opcion_bolsillo = int(input(f"\n{Fore.CYAN}👉 Seleccione el bolsillo que desea eliminar: {Style.RESET_ALL}"))
        if opcion_bolsillo < 1 or opcion_bolsillo > len(bolsillos_usuario):
            print(f"\n{Fore.RED}❌ Error: Opción inválida{Style.RESET_ALL}")
            return

        bolsillo_seleccionado = bolsillos_usuario[opcion_bolsillo - 1]
        saldo_bolsillo = bolsillos[usuario_actual][bolsillo_seleccionado]["Monto"]
        cuenta_origen = bolsillos[usuario_actual][bolsillo_seleccionado]["Cuenta_origen"]

        confirmacion = input(f"\n{Fore.YELLOW}⚠️ ¿Está seguro de que desea eliminar el bolsillo '{bolsillo_seleccionado}'? (S/N): {Style.RESET_ALL}").strip().lower()

        if confirmacion != "s":
            print(f"\n{Fore.CYAN}📝 Operación cancelada{Style.RESET_ALL}")
            return

        if saldo_bolsillo > 0:
            cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"] += saldo_bolsillo
            guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")
            print(f"\n{Fore.GREEN}✅ Se han transferido ${saldo_bolsillo:.2f} COP de '{bolsillo_seleccionado}' a su cuenta de origen '{cuenta_origen}'{Style.RESET_ALL}")

        del bolsillos[usuario_actual][bolsillo_seleccionado]
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        print(f"\n{Fore.GREEN}✅ El bolsillo '{bolsillo_seleccionado}' ha sido eliminado exitosamente{Style.RESET_ALL}")

    except ValueError:
        print(f"\n{Fore.RED}❌ Error: Debe ingresar un número válido{Style.RESET_ALL}")

def crear_bolsillo(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print(f"\n{Fore.YELLOW}⚠️ No tienes cuentas registradas para crear un bolsillo{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}💳 Tus Cuentas Registradas 💳{Style.RESET_ALL}")
    cuentas_usuario = list(cuentas_registradas[usuario_actual].keys())

    for i, cuenta in enumerate(cuentas_usuario, 1):
        saldo = cuentas_registradas[usuario_actual][cuenta]["Saldo"]
        print(f"{Fore.GREEN}{i}. {cuenta} - Saldo: ${saldo:.2f} COP{Style.RESET_ALL}")

    try:
        opcion = int(input(f"\n{Fore.CYAN}👉 Seleccione la cuenta de donde desea guardar dinero en el bolsillo: {Style.RESET_ALL}"))
        if opcion < 1 or opcion > len(cuentas_usuario):
            print(f"\n{Fore.RED}❌ Error: Opción inválida{Style.RESET_ALL}")
            return

        cuenta_seleccionada = cuentas_usuario[opcion - 1]

        nombre_bolsillo = input(f"\n{Fore.CYAN}📝 Ingrese el nombre del bolsillo: {Style.RESET_ALL}").strip().capitalize()
        monto = float(input(f"{Fore.CYAN}💵 Ingrese el monto a guardar en el bolsillo: {Style.RESET_ALL}"))

        if monto <= 0:
            print(f"\n{Fore.RED}❌ Error: El monto debe ser mayor que 0{Style.RESET_ALL}")
            return

        if monto > cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"]:
            print(f"\n{Fore.RED}❌ Error: Fondos insuficientes{Style.RESET_ALL}")
            return

        cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"] -= monto
        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        if usuario_actual not in bolsillos:
            bolsillos[usuario_actual] = {}

        bolsillos[usuario_actual][nombre_bolsillo] = {
            "Monto": monto,
            "Cuenta_origen": cuenta_seleccionada
        }
        guardar_datos(bolsillos, "bolsillos/bolsillos.json")

        print(f"\n{Fore.GREEN}✅ Bolsillo '{nombre_bolsillo}' creado con éxito")
        print(f"💰 Se han guardado ${monto:.2f} COP desde la cuenta {cuenta_seleccionada}{Style.RESET_ALL}")

    except ValueError:
        print(f"\n{Fore.RED}❌ Error: Debe ingresar un número válido{Style.RESET_ALL}")

def listar_bolsillos(usuario_actual):
    bolsillos = cargar_datos("bolsillos/bolsillos.json")

    if usuario_actual not in bolsillos or not bolsillos[usuario_actual]:
        print(f"\n{Fore.YELLOW}⚠️ No tienes bolsillos registrados{Style.RESET_ALL}")
        return

    print(f"\n{Fore.CYAN}💰 Tus Bolsillos Registrados 💰{Style.RESET_ALL}")
    
    for i, (nombre_bolsillo, datos) in enumerate(bolsillos[usuario_actual].items(), 1):
        saldo = datos["Monto"]
        print(f"{Fore.GREEN}{i}. {nombre_bolsillo} - Saldo: ${saldo:.2f} COP{Style.RESET_ALL}")

    print(f"{Fore.CYAN}{'-' * 40}{Style.RESET_ALL}")