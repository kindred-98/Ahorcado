"""
hay_derrota.py
==============
Función para detectar si el jugador ha perdido la partida.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS


def hay_derrota(estado: EstadoPartida) -> bool:
    """
    Comprueba si el número de fallos alcanzó el máximo permitido.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        bool: True si el jugador perdió. False si no.
    """
    return estado.numero_fallos >= MAXIMO_FALLOS