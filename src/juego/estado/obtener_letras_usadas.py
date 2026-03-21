"""
obtener_letras_usadas.py
========================
Función para obtener todas las letras jugadas ordenadas.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida


def obtener_letras_usadas(estado: EstadoPartida) -> list[str]:
    """
    Devuelve todas las letras jugadas ordenadas alfabéticamente.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        list[str]: Lista ordenada de letras ya jugadas.
    """
    return sorted(estado.letras_correctas | estado.letras_fallidas)