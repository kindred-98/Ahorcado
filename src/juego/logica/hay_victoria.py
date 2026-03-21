"""
hay_victoria.py
===============
Función para detectar si el jugador ha ganado la partida.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida


def hay_victoria(estado: EstadoPartida) -> bool:
    """
    Comprueba si todas las letras únicas de la palabra
    han sido adivinadas.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        bool: True si el jugador ganó. False si no.
    """
    return set(estado.palabra_secreta).issubset(estado.letras_correctas)