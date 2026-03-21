"""
intentos_restantes.py
=====================
Función para calcular los intentos restantes del jugador.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS


def intentos_restantes(estado: EstadoPartida) -> int:
    """
    Calcula los intentos que le quedan al jugador.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        int: Número de intentos restantes.
    """
    return MAXIMO_FALLOS - estado.numero_fallos