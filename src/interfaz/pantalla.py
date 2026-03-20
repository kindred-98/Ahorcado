"""
pantalla.py
===========
Módulo encargado de renderizar la interfaz visual del
Ahorcado Medieval en la terminal.

Responsabilidades:
    - Limpiar la pantalla entre turnos.
    - Construir y mostrar la cabecera con la palabra oculta
      y las letras ya usadas.
    - Componer la escena completa: cabecera + estado ASCII.

Importaciones necesarias:
    from src.interfaz.dibujo import ESTADOS, MAXIMO_FALLOS
"""

import os
from src.interfaz.dibujo import ESTADOS, MAXIMO_FALLOS


# ── Constantes visuales ───────────────────────────────────────
ANCHO_CABECERA:       int = 68
ANCHO_CAMPO_PALABRA:  int = 30
ANCHO_CAMPO_LETRAS:   int = 64


# ── Funciones públicas ────────────────────────────────────────

def limpiar_pantalla() -> None:
    """
    Limpia la terminal de forma compatible con Windows y Unix.

    Usa 'cls' en Windows y 'clear' en Linux/macOS.
    """
    os.system("cls" if os.name == "nt" else "clear")


def construir_cabecera(palabra_oculta: str, letras_usadas: list[str]) -> str:
    """
    Construye el recuadro superior con la palabra oculta
    y las letras ya intentadas.

    Args:
        palabra_oculta (str): Cadena con letras reveladas y guiones.
                              Ejemplo: "c _ s t _ _ _ o"
        letras_usadas  (list[str]): Lista de letras ya intentadas.
                              Ejemplo: ["a", "c", "e"]

    Returns:
        str: Bloque de texto con el recuadro formateado listo
             para imprimir.
    """
    letras_formateadas = _formatear_letras_usadas(letras_usadas)

    cabecera = (
        f"  ╔{'═' * ANCHO_CABECERA}╗\n"
        f"  ║{'✦   EL AHORCADO MEDIEVAL   ✦':^{ANCHO_CABECERA}}║\n"
        f"  ║{' ' * ANCHO_CABECERA}║\n"
        f"  ║   Palabra :  {palabra_oculta:<{ANCHO_CAMPO_PALABRA}}"
        f"{'':>{ANCHO_CABECERA - ANCHO_CAMPO_PALABRA - 16}}║\n"
        f"  ║   {letras_formateadas:<{ANCHO_CAMPO_LETRAS}}{'':>{ANCHO_CABECERA - ANCHO_CAMPO_LETRAS - 3}}║\n"
        f"  ╚{'═' * ANCHO_CABECERA}╝"
    )
    return cabecera


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


def mostrar_mensaje(mensaje: str) -> None:
    """
    Imprime un mensaje simple centrado en la terminal.

    Args:
        mensaje (str): Texto a mostrar.
    """
    print(f"\n  {mensaje}\n")


def mostrar_error(mensaje_error: str) -> None:
    """
    Imprime un mensaje de error con formato de advertencia.

    Args:
        mensaje_error (str): Descripción del error ocurrido.
    """
    print(f"\n  ⚠  {mensaje_error}\n")


# ── Funciones privadas ────────────────────────────────────────

def _formatear_letras_usadas(letras_usadas: list[str]) -> str:
    """
    Convierte la lista de letras usadas en una cadena legible.

    Args:
        letras_usadas (list[str]): Lista de letras intentadas.

    Returns:
        str: Cadena formateada. Ejemplo: "Letras usadas: A, C, E"
             o "Letras usadas: ninguna" si la lista está vacía.
    """
    if not letras_usadas:
        return "Letras usadas: ninguna"

    letras_en_mayusculas = [letra.upper() for letra in letras_usadas]
    return f"Letras usadas: {', '.join(letras_en_mayusculas)}"


def _construir_etiqueta_fallos(numero_fallos: int) -> str:
    """
    Construye la línea de estado que muestra los fallos actuales.

    Args:
        numero_fallos (int): Número de fallos acumulados.

    Returns:
        str: Línea formateada con los fallos actuales.
             Ejemplo: "  ── Fallos: 2/6 ──"
    """
    if numero_fallos == 0:
        descripcion = "Sin fallos aún"
    elif numero_fallos == MAXIMO_FALLOS:
        descripcion = "¡Sin más intentos!"
    else:
        descripcion = f"Fallos: {numero_fallos}/{MAXIMO_FALLOS}"

    return f"\n  ── {descripcion} ──\n"