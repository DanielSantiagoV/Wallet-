import requests

#Instalar la API de requests con el siguiente comando:
#pip install requests
#Una API ​ es una pieza de código que permite a dos aplicaciones comunicarse 
#entre sí para compartir información y funcionalidades. Se usan generalmente 
#en bibliotecas de programación.​

def convertir_cop_a_usd():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/COP")
        data = response.json()
        tasa_cambio = data["rates"]["USD"]

        monto_cop = float(input("Ingrese el monto en COP a convertir: "))
        if monto_cop <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return

        monto_usd = monto_cop * tasa_cambio
        print(f"\n{monto_cop:.2f} COP equivale a {monto_usd:.2f} USD")

    except requests.exceptions.RequestException:
        print("Error: No se pudo obtener la tasa de cambio.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def convertir_cop_a_eur():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/COP")
        data = response.json()
        tasa_cambio = data["rates"]["EUR"]

        monto_cop = float(input("Ingrese el monto en COP a convertir: "))
        if monto_cop <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return

        monto_eur = monto_cop * tasa_cambio
        print(f"\n{monto_cop:.2f} COP equivale a {monto_eur:.2f} EUR")

    except requests.exceptions.RequestException:
        print("Error: No se pudo obtener la tasa de cambio.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def convertir_cop_a_gbp():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/COP")
        data = response.json()
        tasa_cambio = data["rates"]["GBP"]

        monto_cop = float(input("Ingrese el monto en COP a convertir: "))
        if monto_cop <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return

        monto_gbp = monto_cop * tasa_cambio
        print(f"\n{monto_cop:.2f} COP equivale a {monto_gbp:.2f} GBP")

    except requests.exceptions.RequestException:
        print("Error: No se pudo obtener la tasa de cambio.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def convertir_cop_a_jpy():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/COP")
        data = response.json()
        tasa_cambio = data["rates"]["JPY"]

        monto_cop = float(input("Ingrese el monto en COP a convertir: "))
        if monto_cop <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return

        monto_jpy = monto_cop * tasa_cambio
        print(f"\n{monto_cop:.2f} COP equivale a {monto_jpy:.2f} JPY")

    except requests.exceptions.RequestException:
        print("Error: No se pudo obtener la tasa de cambio.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def convertir_cop_a_cad():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/COP")
        data = response.json()
        tasa_cambio = data["rates"]["CAD"]

        monto_cop = float(input("Ingrese el monto en COP a convertir: "))
        if monto_cop <= 0:
            print("Error: El monto debe ser mayor a 0.")
            return

        monto_cad = monto_cop * tasa_cambio
        print(f"\n{monto_cop:.2f} COP equivale a {monto_cad:.2f} CAD")

    except requests.exceptions.RequestException:
        print("Error: No se pudo obtener la tasa de cambio.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")