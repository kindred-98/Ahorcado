"""
construir_cabecera.py
=====================
Función para construir el recuadro superior con la palabra oculta.
"""

from src.interfaz.pantalla.formatear_letras_usadas import _formatear_letras_usadas


ANCHO_CABECERA:      int = 68
ANCHO_CAMPO_PALABRA: int = 30
ANCHO_CAMPO_LETRAS:  int = 64


def construir_cabecera(palabra_oculta: str, letras_usadas: list[str]) -> str:
    """
    Construye el recuadro superior con la palabra oculta
    y las letras ya intentadas.

    Args:
        palabra_oculta (str):       Cadena con letras reveladas y guiones.
        letras_usadas  (list[str]): Lista de letras ya intentadas.

    Returns:
        str: Bloque de texto con el recuadro formateado.
    """
    letras_formateadas = _formatear_letras_usadas(letras_usadas)

    return (
        f"  ╔{'═' * ANCHO_CABECERA}╗\n"
        f"  ║{'✦   EL AHORCADO MEDIEVAL   ✦':^{ANCHO_CABECERA}}║\n"
        f"  ║{' ' * ANCHO_CABECERA}║\n"
        f"  ║   Palabra :  {palabra_oculta:<{ANCHO_CAMPO_PALABRA}}"
        f"{'':>{ANCHO_CABECERA - ANCHO_CAMPO_PALABRA - 16}}║\n"
        f"  ║   {letras_formateadas:<{ANCHO_CAMPO_LETRAS}}{'':>{ANCHO_CABECERA - ANCHO_CAMPO_LETRAS - 3}}║\n"
        f"  ╚{'═' * ANCHO_CABECERA}╝"
    )