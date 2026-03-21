"""
mostrar_escena.py
=================
Función para renderizar la escena completa en la terminal.
"""

from src.interfaz.dibujo.estados               import ESTADOS
from src.interfaz.dibujo.maximo_fallos          import MAXIMO_FALLOS
from src.interfaz.pantalla.limpiar_pantalla      import limpiar_pantalla
from src.interfaz.pantalla.construir_cabecera    import construir_cabecera
from src.interfaz.pantalla.construir_etiqueta_fallos import _construir_etiqueta_fallos


def mostrar_escena(
    numero_fallos:  int,
    palabra_oculta: str,
    letras_usadas:  list[str],
) -> None:
    """
    Limpia la pantalla y renderiza la escena completa:
    cabecera con estado del juego + arte ASCII del estado actual.

    Args:
        numero_fallos  (int):       Número de fallos acumulados (0-6).
        palabra_oculta (str):       Palabra con letras reveladas y guiones.
        letras_usadas  (list[str]): Lista de letras ya intentadas.

    Raises:
        ValueError: Si numero_fallos está fuera del rango 0-MAXIMO_FALLOS.
    """
    if not 0 <= numero_fallos <= MAXIMO_FALLOS:
        raise ValueError(
            f"numero_fallos debe estar entre 0 y {MAXIMO_FALLOS}, "
            f"se recibió: {numero_fallos}"
        )

    limpiar_pantalla()
    print(construir_cabecera(palabra_oculta, letras_usadas))
    print(_construir_etiqueta_fallos(numero_fallos))
    print(ESTADOS[numero_fallos])