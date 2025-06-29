# 💰 Campers Wallet

Un sistema de billetera digital completo desarrollado en Python que permite gestionar finanzas personales de manera eficiente y segura.

## 🚀 Características

### 👤 Gestión de Usuarios
- **Registro seguro**: Validación de datos y contraseñas hasheadas
- **Inicio de sesión**: Autenticación segura con verificación de credenciales
- **Validación de edad**: Solo usuarios mayores de 18 años
- **Validación de email**: Formato de correo electrónico verificado

### 💳 Gestión de Cuentas
- **Registro de cuentas**: Múltiples cuentas bancarias por usuario
- **Modificación**: Actualizar información de cuentas existentes
- **Eliminación**: Remover cuentas con confirmación
- **Visualización**: Ver saldos y cuentas registradas
- **Saldo total**: Cálculo automático del saldo combinado

### 💸 Transacciones
- **Pagos**: Transferencias entre usuarios
- **Retiros**: Extraer dinero de cuentas
- **Depósitos**: Agregar fondos a cuentas
- **Historial**: Registro completo de movimientos
- **Validación**: Verificación de fondos antes de transacciones

### 🏦 Bolsillos de Ahorro
- **Creación**: Nuevos bolsillos con nombre personalizado
- **Gestión de fondos**: Agregar y retirar dinero
- **Eliminación**: Cerrar bolsillos con transferencia automática
- **Visualización**: Estado actual de todos los bolsillos

### 💱 Conversión de Divisas
- **Tiempo real**: Tasas de cambio actualizadas via API
- **Múltiples monedas**: USD, EUR, GBP, JPY, CAD
- **Cálculo preciso**: Conversiones con 6 decimales
- **Manejo de errores**: Gestión robusta de fallos de conexión

## 📋 Requisitos

- Python 3.7 o superior
- Conexión a internet (para conversión de divisas)

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd Wallet-
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:
   ```bash
   python main.py
   ```

## 🎯 Uso

### Primeros Pasos

1. **Registrarse**: Crear una nueva cuenta de usuario
2. **Iniciar sesión**: Acceder con usuario y contraseña
3. **Registrar cuentas**: Agregar cuentas bancarias
4. **Realizar transacciones**: Comenzar a usar el sistema

### Ejemplos de Uso

#### Registro de Usuario
```
=== REGISTRO DE USUARIO ===
Ingrese su nombre completo: Juan Pérez
Ingrese su edad: 25
Ingrese su correo electrónico: juan@email.com
Ingrese su usuario: juanperez
Ingrese una contraseña: MiContraseña123
✅ Registro exitoso. ¡Bienvenido, Juan Pérez!
```

#### Conversión de Divisas
```
=== Conversión COP a USD (Dólar Estadounidense) ===
Ingrese el monto en COP a convertir: 100000
✅ 100,000.00 COP equivale a 25.50 USD
```

#### Gestión de Bolsillos
```
💰 Tus Bolsillos Registrados 💰
1. Vacaciones - Saldo: $500,000.00 COP - Cuenta Origen: Bancolombia
2. Emergencias - Saldo: $200,000.00 COP - Cuenta Origen: Davivienda
```

## 📁 Estructura del Proyecto

```
Wallet-/
├── main.py                      # Punto de entrada principal
├── config.py                    # Configuración centralizada
├── utils.py                     # Funciones utilitarias
├── data.py                      # Manejo de datos y persistencia
├── registro.py                  # Registro de usuarios
├── inicio_sesion.py             # Autenticación
├── utilidades_menu.py           # Lógica de menús
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación
├── app.log                      # Archivo de logs
├── gestion_cuentas/             # Gestión de cuentas bancarias
│   ├── registro_cuentas.py
│   ├── cuentas.json
│   └── cuentas_registradas.json
├── transacciones/               # Sistema de transacciones
│   ├── transacciones.py
│   └── movimientos.json
├── bolsillos/                   # Bolsillos de ahorro
│   ├── bolsillos.py
│   └── bolsillos.json
├── divisas/                     # Conversión de divisas
│   └── divisas.py
└── usuarios/                    # Datos de usuarios
    └── registros.json
```

## 🔒 Seguridad

- **Contraseñas hasheadas**: Uso de SHA-256 para almacenamiento seguro
- **Validación de entrada**: Verificación de todos los datos de usuario
- **Manejo de errores**: Gestión robusta de excepciones
- **Logs de actividad**: Registro de operaciones importantes

## 🛡️ Características de Seguridad

### Validación de Contraseñas
- Mínimo 8 caracteres
- Al menos un número
- Al menos una letra mayúscula
- Al menos una letra minúscula

### Validación de Datos
- Verificación de formato de email
- Validación de edad mínima
- Comprobación de nombres únicos
- Verificación de fondos antes de transacciones

## 🔧 Configuración

El archivo `config.py` contiene todas las configuraciones del sistema:

- **Rutas de archivos**: Ubicaciones de datos JSON
- **Configuración de API**: URLs para conversión de divisas
- **Límites del sistema**: Edad mínima, longitud de contraseñas
- **Opciones de menú**: Configuración de interfaces

## 📊 Persistencia de Datos

El sistema utiliza archivos JSON para almacenar:
- **Usuarios**: Información de registro y autenticación
- **Cuentas**: Datos bancarios y saldos
- **Transacciones**: Historial completo de movimientos
- **Bolsillos**: Estado de ahorros por usuario

## 🐛 Solución de Problemas

### Error de Dependencias
```bash
pip install -r requirements.txt
```

### Error de Conexión (Divisas)
- Verificar conexión a internet
- Revisar firewall/antivirus
- Intentar más tarde

### Error de Archivos
- Verificar permisos de escritura
- Comprobar espacio en disco
- Revisar logs en `app.log`

## 🤝 Contribuciones

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado como parte del programa de formación en desarrollo de software.

## 🙏 Agradecimientos

- API de Exchange Rate para tasas de cambio en tiempo real
- Comunidad de Python por las librerías utilizadas
- Instructores y compañeros del programa de formación

---

**¡Disfruta gestionando tus finanzas con Campers Wallet! 💰**
