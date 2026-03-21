"""
letra_ya_usada.py
=================
Función para comprobar si una letra ya fue jugada.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida


def letra_ya_usada(estado: EstadoPartida, letra: str) -> bool:
    """
    Comprueba si una letra ya fue jugada anteriormente.

    Args:
        estado (EstadoPartida): Estado actual de la partida.
        letra  (str):           Letra a comprobar.

    Returns:
        bool: True si ya fue usada. False si es nueva.
    """
    letra_normalizada = letra.lower()
    return (
        letra_normalizada in estado.letras_correctas
        or letra_normalizada in estado.letras_fallidas
    )