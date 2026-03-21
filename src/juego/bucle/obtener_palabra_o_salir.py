"""
obtener_palabra_o_salir.py
==========================
Función privada para obtener una palabra de la BD o salir.
"""

from src.base_datos.consultas.obtener_palabra_aleatoria import obtener_palabra_aleatoria
from src.interfaz.pantalla.mostrar_error                import mostrar_error


def _obtener_palabra_o_salir(categoria: str | None) -> dict | None:
    """
    Intenta obtener una palabra aleatoria de la base de datos.
    Si no encuentra ninguna informa al jugador y devuelve None.

    Args:
        categoria (str | None): Filtro de categoría opcional.

    Returns:
        dict | None: Registro de la palabra o None si no hay palabras.
    """
    registro_palabra = obtener_palabra_aleatoria(categoria=categoria)

    if registro_palabra is None:
        mostrar_error(
            "No se encontraron palabras disponibles"
            + (f" en la categoría '{categoria}'." if categoria else ".")
        )
        return None

    return registro_palabra