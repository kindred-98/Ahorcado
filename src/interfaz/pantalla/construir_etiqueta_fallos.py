"""
construir_etiqueta_fallos.py
============================
Función privada para construir la etiqueta de fallos actuales.
"""

from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS


def _construir_etiqueta_fallos(numero_fallos: int) -> str:
    """
    Construye la línea de estado con los fallos actuales.

    Args:
        numero_fallos (int): Número de fallos acumulados.

    Returns:
        str: Línea formateada con el estado de fallos.
    """
    if numero_fallos == 0:
        descripcion = "Sin fallos aún"
    elif numero_fallos == MAXIMO_FALLOS:
        descripcion = "¡Sin más intentos!"
    else:
        descripcion = f"Fallos: {numero_fallos}/{MAXIMO_FALLOS}"

    return f"\n  ── {descripcion} ──\n"