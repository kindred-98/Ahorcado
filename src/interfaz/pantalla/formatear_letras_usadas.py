"""
formatear_letras_usadas.py
==========================
Función privada para formatear la lista de letras usadas.
"""


def _formatear_letras_usadas(letras_usadas: list[str]) -> str:
    """
    Convierte la lista de letras usadas en una cadena legible.

    Args:
        letras_usadas (list[str]): Lista de letras intentadas.

    Returns:
        str: Cadena formateada con las letras en mayúsculas
             o "ninguna" si la lista está vacía.
    """
    if not letras_usadas:
        return "Letras usadas: ninguna"

    letras_en_mayusculas = [letra.upper() for letra in letras_usadas]
    return f"Letras usadas: {', '.join(letras_en_mayusculas)}"