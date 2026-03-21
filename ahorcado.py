"""
ahorcado.py
===========
Punto de entrada principal del Ahorcado Medieval.

Este archivo únicamente arranca la aplicación.
Toda la lógica está distribuida en los módulos de src/.

Uso:
    python ahorcado.py
"""



from src.base_datos.inicializar.inicializar_base_datos import inicializar_base_datos
from src.interfaz.menu.ejecutar_menu_principal import ejecutar_menu_principal


def main() -> None:
    """
    Función principal. Inicializa la base de datos y
    lanza el menú principal.
    """
    inicializar_base_datos()
    ejecutar_menu_principal()


if __name__ == "__main__":
    main()