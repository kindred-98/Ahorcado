"""
construir_palabra_oculta.py
===========================
Función para construir la representación visual de la palabra oculta.
"""

from src.juego.estado.clase_estado_partida import EstadoPartida


def construir_palabra_oculta(estado: EstadoPartida) -> str:
    """
    Construye la representación visual de la palabra oculta,
    revelando letras acertadas y ocultando el resto con guiones.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        str: Letras reveladas separadas por espacios. Las no
             adivinadas se muestran como guión bajo.
    """
    return " ".join(
        letra if letra in estado.letras_correctas else "_"
        for letra in estado.palabra_secreta
    )