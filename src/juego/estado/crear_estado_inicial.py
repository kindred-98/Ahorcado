"""
crear_estado_inicial.py
=======================
Función para crear un estado de partida desde un registro de la BD.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida


def crear_estado_inicial(registro_palabra: dict) -> EstadoPartida:
    """
    Crea un estado de partida nuevo desde un registro de la BD.

    Args:
        registro_palabra (dict): Diccionario con 'palabra', 'categoria'
                                 y 'dificultad'.

    Returns:
        EstadoPartida: Estado inicial con sets vacíos y cero fallos.
    """
    return EstadoPartida(
        palabra_secreta = registro_palabra["palabra"],
        categoria       = registro_palabra["categoria"],
        dificultad      = registro_palabra["dificultad"],
    )