"""
letra.py
========
Módulo encargado de validar la letra ingresada por el jugador
durante una partida del Ahorcado Medieval.

Responsabilidades:
    - Verificar que la entrada sea exactamente una letra.
    - Verificar que pertenezca al alfabeto español.
    - Devolver un mensaje de error descriptivo o None si es válida.

Importaciones necesarias:
    from src.validaciones.letra import validar_letra
"""

import unicodedata


# ── Constantes ────────────────────────────────────────────────

ALFABETO_ESPAÑOL: frozenset[str] = frozenset(
    "abcdefghijklmnñopqrstuvwxyzáéíóúü"
)


# ── Función pública ───────────────────────────────────────────

def validar_letra(entrada: str) -> str | None:
    """
    Valida que la entrada del jugador sea una letra válida
    del alfabeto español.

    La entrada se normaliza a minúsculas antes de validar.
    No verifica si la letra ya fue usada, esa responsabilidad
    pertenece a bucle.py.

    Args:
        entrada (str): Texto ingresado por el jugador.

    Returns:
        str | None: Mensaje de error si la entrada no es válida.
                    None si la entrada es correcta.

    Ejemplos:
        validar_letra("a")   → None
        validar_letra("ñ")   → None
        validar_letra("")    → "Debes ingresar una letra."
        validar_letra("ab")  → "Ingresa solo una letra, no varias."
        validar_letra("3")   → "El carácter '3' no es una letra válida."
    """
    if not entrada:
        return "Debes ingresar una letra."

    if len(entrada) > 1:
        return "Ingresa solo una letra, no varias."

    letra_normalizada = entrada.lower()

    if letra_normalizada not in ALFABETO_ESPAÑOL:
        return f"El carácter '{entrada}' no es una letra válida."

    return None


# ── Funciones privadas ────────────────────────────────────────

def _normalizar_caracter(caracter: str) -> str:
    """
    Normaliza un carácter eliminando tildes para comparaciones
    cuando sea necesario.

    Por ejemplo: 'á' → 'a', 'é' → 'e'.

    Args:
        caracter (str): Carácter a normalizar.

    Returns:
        str: Carácter sin tilde en minúscula.
    """
    return unicodedata.normalize("NFD", caracter)\
        .encode("ascii", "ignore")\
        .decode("utf-8")\
        .lower()