from data import *
import datetime
import json


def realizar_pago(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("No tienes cuentas registradas para realizar pagos.")
        return

    print("\n***** Tus Cuentas Registradas *****")
    cuentas_usuario = list(cuentas_registradas[usuario_actual].keys())

    for i, cuenta in enumerate(cuentas_usuario, 1):
        saldo = cuentas_registradas[usuario_actual][cuenta]["Saldo"]
        print(f"{i}. {cuenta} - Saldo: ${saldo:.2f} COP")

    try:
        opcion_origen = int(input("Seleccione la cuenta de origen: "))
        if opcion_origen < 1 or opcion_origen > len(cuentas_usuario):
            print("Opción inválida.")
            return

        cuenta_origen = cuentas_usuario[opcion_origen - 1]

        usuario_destino = input("\nIngrese el usuario destinatario: ").strip().lower()

        if usuario_destino not in cuentas_registradas:
            print("***** El usuario destinatario no existe o no tiene cuentas registradas. *****")
            return

        print(f"\n***** Cuentas Registradas de {usuario_destino} *****")
        cuentas_destino = list(cuentas_registradas[usuario_destino].keys())

        for i, cuenta in enumerate(cuentas_destino, 1):
            print(f"{i}. {cuenta}")

        opcion_destino = int(input("Seleccione la cuenta destino del destinatario: "))
        if opcion_destino < 1 or opcion_destino > len(cuentas_destino):
            print("Opción inválida.")
            return

        cuenta_destino = cuentas_destino[opcion_destino - 1]

        monto = float(input("\nIngrese el monto a transferir en COP: "))

        if monto <= 0:
            print("Error. El monto debe ser mayor que 0.")
            return

        if monto > cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"]:
            print("Error. Fondos insuficientes.")
            return

        cuentas_registradas[usuario_actual][cuenta_origen]["Saldo"] -= monto
        cuentas_registradas[usuario_destino][cuenta_destino]["Saldo"] += monto

        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        registrar_movimiento(usuario_actual, "Pago", monto, usuario_destino, "Aprobado")
        registrar_movimiento(usuario_destino, "Depósito", monto, usuario_actual, "Aprobado")

        print(f"\n***** El pago ha sido realizado con éxito *****")
        print(f"Has enviado ${monto:.2f} COP desde {cuenta_origen} a {usuario_destino} ({cuenta_destino}).")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def registrar_movimiento(usuario, tipo, monto, destinatario=None, estado="Aprobado"):
    archivo_movimientos = "transacciones/movimientos.json"

    try:
        with open(archivo_movimientos, "r") as archivo:
            movimientos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        movimientos = {}

    if usuario not in movimientos:
        movimientos[usuario] = []

    movimiento = {
        "Fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Tipo": tipo, 
        "Monto": monto,
        "Destinatario": destinatario if destinatario else "N/A",
        "Estado": estado 
    }

    movimientos[usuario].append(movimiento)

    with open(archivo_movimientos, "w") as archivo:
        json.dump(movimientos, archivo, indent=4)

    print("***** Movimiento registrado *****")

def listar_movimientos(usuario_actual):
    movimientos_registrados = cargar_datos("transacciones/movimientos.json")

    if usuario_actual not in movimientos_registrados or not movimientos_registrados[usuario_actual]:
        print("\nNo tienes movimientos registrados.")
        return

    print("\n***** Historial de Movimientos *****")
    print(f"Usuario: {usuario_actual}")

    for i, mov in enumerate(movimientos_registrados[usuario_actual], 1):
        fecha = mov.get("Fecha", "Desconocida")
        tipo = mov.get("Tipo", "Desconocido")
        monto = mov.get("Monto", 0)
        destinatario = mov.get("Destinatario", "Desconocido")
        estado = mov.get("Estado", "Pendiente")

        print(f"\nMovimiento {i}:")
        print(f"Fecha: {fecha}")
        print(f"Tipo: {tipo}")
        print(f"Monto: ${monto:.2f} COP")
        print(f"Destinatario: {destinatario}")
        print(f"Estado: {estado}")
        print("-" * 30)

def retirar_dinero(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("No tienes cuentas registradas para realizar retiros.")
        return

    print("\n***** Tus Cuentas Registradas *****")
    cuentas_usuario = list(cuentas_registradas[usuario_actual].keys())

    for i, cuenta in enumerate(cuentas_usuario, 1):
        saldo = cuentas_registradas[usuario_actual][cuenta]["Saldo"]
        print(f"{i}. {cuenta} - Saldo: ${saldo:.2f} COP")

    try:
        opcion = int(input("Seleccione la cuenta de la que desea retirar dinero: "))
        if opcion < 1 or opcion > len(cuentas_usuario):
            print("Error. Opción inválida.")
            return

        cuenta_seleccionada = cuentas_usuario[opcion - 1]
        saldo_disponible = cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"]

        monto = float(input("\nIngrese el monto a retirar en COP: "))

        if monto <= 0:
            print("Error. El monto debe ser mayor que 0.")
            return

        if monto > saldo_disponible:
            print("Error. Fondos insuficientes.")
            return

        cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"] -= monto
        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        registrar_movimiento(usuario_actual, "Retiro", monto, "Efectivo", "Aprobado")

        print(f"\n***** Retiro exitoso. Has retirado ${monto:.2f} COP de {cuenta_seleccionada}. *****")
        print(f"Su saldo restante es: ${cuentas_registradas[usuario_actual][cuenta_seleccionada]['Saldo']:.2f} COP.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")

def depositar_dinero(usuario_actual):
    cuentas_registradas = cargar_datos("gestion_cuentas/cuentas.json")

    if usuario_actual not in cuentas_registradas or not cuentas_registradas[usuario_actual]:
        print("No tienes cuentas registradas para realizar depósitos.")
        return

    print("\n***** Tus Cuentas Registradas *****")
    cuentas_usuario = list(cuentas_registradas[usuario_actual].keys())

    for i, cuenta in enumerate(cuentas_usuario, 1):
        saldo = cuentas_registradas[usuario_actual][cuenta]["Saldo"]
        print(f"{i}. {cuenta} - Saldo: ${saldo:.2f} COP")

    try:
        opcion = int(input("Seleccione la cuenta a la que desea depositar dinero: "))
        if opcion < 1 or opcion > len(cuentas_usuario):
            print("Error. Opción inválida.")
            return

        cuenta_seleccionada = cuentas_usuario[opcion - 1]

        monto = float(input("\nIngrese el monto a depositar en COP: "))

        if monto <= 0:
            print("Error. El monto debe ser mayor que 0.")
            return

        cuentas_registradas[usuario_actual][cuenta_seleccionada]["Saldo"] += monto

        guardar_datos(cuentas_registradas, "gestion_cuentas/cuentas.json")

        registrar_movimiento(usuario_actual, "Depósito", monto, "Efectivo", "Aprobado")

        print(f"\n***** Depósito exitoso. Has depositado ${monto:.2f} COP en {cuenta_seleccionada}. *****")
        print(f"Su nuevo saldo es: ${cuentas_registradas[usuario_actual][cuenta_seleccionada]['Saldo']:.2f} COP.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")