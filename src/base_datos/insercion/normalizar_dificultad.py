"""
normalizar_dificultad.py
========================
Función privada para validar y normalizar el valor de dificultad.
"""

from src.validaciones.palabra.constantes import DIFICULTADES_VALIDAS


def _normalizar_dificultad(dificultad: str) -> str | None:
    """
    Valida y normaliza el valor de dificultad recibido.

    Args:
        dificultad (str): Valor de dificultad a normalizar.

    Returns:
        str | None: Valor normalizado si es válido, None si no lo es.
    """
    valor_normalizado = dificultad.lower().strip()

    if valor_normalizado not in DIFICULTADES_VALIDAS:
        return None

    return valor_normalizado