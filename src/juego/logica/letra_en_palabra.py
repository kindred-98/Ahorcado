"""
letra_en_palabra.py
===================
Función para comprobar si una letra pertenece a la palabra secreta.
"""


def letra_en_palabra(letra: str, palabra_secreta: str) -> bool:
    """
    Comprueba si una letra pertenece a la palabra secreta.

    Args:
        letra           (str): Letra a comprobar.
        palabra_secreta (str): Palabra secreta de la partida.

    Returns:
        bool: True si la letra está en la palabra. False si no.
    """
    return letra.lower() in palabra_secreta.lower()