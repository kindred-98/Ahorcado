"""
registrar_letra.py
==================
Función para registrar una letra jugada en el estado de la partida.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida


def registrar_letra(estado: EstadoPartida, letra: str) -> EstadoPartida:
    """
    Registra una letra jugada actualizando el estado de la partida.

    Si la letra está en la palabra va a letras_correctas.
    Si no está va a letras_fallidas y suma un fallo.

    Args:
        estado (EstadoPartida): Estado actual de la partida.
        letra  (str):           Letra jugada en minúscula.

    Returns:
        EstadoPartida: Estado mutado con la letra registrada.
    """
    letra_normalizada = letra.lower()

    if letra_normalizada in estado.palabra_secreta:
        estado.letras_correctas.add(letra_normalizada)
    else:
        estado.letras_fallidas.add(letra_normalizada)
        estado.numero_fallos += 1

    return estado