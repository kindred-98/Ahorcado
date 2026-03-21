"""
partida_terminada.py
====================
Función para comprobar si la partida ha terminado.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.juego.logica.hay_victoria          import hay_victoria
from src.juego.logica.hay_derrota           import hay_derrota


def partida_terminada(estado: EstadoPartida) -> bool:
    """
    Comprueba si la partida terminó por victoria o derrota.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        bool: True si la partida terminó. False si continúa.
    """
    return hay_victoria(estado) or hay_derrota(estado)