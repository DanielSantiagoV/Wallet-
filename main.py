"""
Main entry point for Campers Wallet application.
A CLI-based wallet/banking system with user management, transactions, and currency conversion.
"""

import sys
from colorama import init, Fore, Style
from utils import print_success, print_error, print_info, clear_screen
from utilidades_menu import ejecucion_menu_principal

# Initialize colorama for cross-platform colored output
init()


def display_welcome_banner() -> None:
    """Display the application welcome banner."""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    {Fore.YELLOW}💰 CAMPERS WALLET 💰{Fore.CYAN}                    ║
║                                                                    ║
║  {Fore.GREEN}Un sistema de billetera digital para gestionar tus finanzas{Fore.CYAN}  ║
║                                                                    ║
║  {Fore.WHITE}Características:{Fore.CYAN}                                              ║
║  • Gestión de cuentas bancarias                                  ║
║  • Transacciones (pagos, retiros, depósitos)                    ║
║  • Bolsillos de ahorro                                           ║
║  • Conversión de divisas en tiempo real                          ║
║  • Historial de movimientos                                      ║
║                                                                    ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)


def check_dependencies() -> bool:
    """
    Check if all required dependencies are available.
    
    Returns:
        bool: True if all dependencies are available, False otherwise
    """
    try:
        import colorama
        import requests
        return True
    except ImportError as e:
        print_error(f"Error: Falta la dependencia {e.name}")
        print_info("Ejecute: pip install -r requirements.txt")
        return False


def main() -> None:
    """
    Main application entry point.
    Handles initialization and starts the main menu loop.
    """
    try:
        # Clear screen and display welcome banner
        clear_screen()
        display_welcome_banner()
        
        # Check dependencies
        if not check_dependencies():
            sys.exit(1)
        
        print_info("Iniciando Campers Wallet...")
        print_success("¡Bienvenido al sistema!")
        
        # Start the main menu
        ejecucion_menu_principal()
        
    except KeyboardInterrupt:
        print_info("\nCerrando aplicación...")
        print_success("¡Gracias por usar Campers Wallet!")
        sys.exit(0)
    except Exception as e:
        print_error(f"Error inesperado: {str(e)}")
        print_info("Por favor, contacte al soporte técnico.")
        sys.exit(1)


if __name__ == "__main__":
    main()