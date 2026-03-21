"""
validar_dificultad.py
=====================
Función pública para validar la dificultad de una palabra.
"""

from src.validaciones.palabra.constantes import DIFICULTADES_VALIDAS


def validar_dificultad(dificultad: str) -> str | None:
    """
    Valida que la dificultad sea facil, medio o dificil.

    Args:
        dificultad (str): Dificultad a validar.

    Returns:
        str | None: Mensaje de error o None si es válida.
    """
    dificultad_normalizada = dificultad.strip().lower()

    if not dificultad_normalizada:
        return "La dificultad no puede estar vacía."

    if dificultad_normalizada not in DIFICULTADES_VALIDAS:
        opciones = ", ".join(sorted(DIFICULTADES_VALIDAS))
        return f"Dificultad no válida. Elige entre: {opciones}."

    return None