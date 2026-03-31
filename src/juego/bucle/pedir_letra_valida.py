"""
pedir_letra_valida.py
=====================
Función privada para pedir una letra o palabra completa al jugador.
"""

from src.juego.estado.clase_estado_partida      import EstadoPartida
from src.juego.estado.letra_ya_usada            import letra_ya_usada
from src.juego.estado.construir_palabra_oculta  import construir_palabra_oculta
from src.juego.estado.obtener_letras_usadas     import obtener_letras_usadas
from src.validaciones.letra.validar_letra       import validar_letra
from src.interfaz.pantalla.mostrar_escena       import mostrar_escena
from src.interfaz.pantalla.mostrar_error        import mostrar_error


# Centinela para indicar que el jugador intentó adivinar la palabra completa
INTENTO_PALABRA_COMPLETA: str = "__PALABRA__"


def _pedir_letra_valida(estado: EstadoPartida) -> str:
    """
    Solicita una letra o palabra completa al jugador en bucle
    hasta recibir una entrada válida.

    Si el jugador escribe más de una letra se interpreta como
    intento de adivinar la palabra completa. Se devuelve el
    centinela INTENTO_PALABRA_COMPLETA junto con la entrada
    para que el bucle lo gestione.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        str: Letra válida en minúscula, o la palabra completa
             intentada como 'INTENTO_PALABRA_COMPLETA:palabra'.
    """
    while True:
        entrada = input("  Ingresa una letra o la palabra > ").strip().lower()

        if not entrada:
            _redibujar_con_error(estado, "Debes ingresar algo.")
            continue

        # Intento de palabra completa
        if len(entrada) > 1:
            return f"{INTENTO_PALABRA_COMPLETA}:{entrada}"

        # Validación de letra individual
        error = validar_letra(entrada)
        if error:
            _redibujar_con_error(estado, error)
            continue

        if letra_ya_usada(estado, entrada):
            _redibujar_con_error(
                estado,
                f"La letra '{entrada.upper()}' ya fue usada. Intenta con otra."
            )
            continue

        return entrada


def _redibujar_con_error(estado: EstadoPartida, mensaje_error: str) -> None:
    """
    Limpia la pantalla, redibuja la escena actual y muestra
    el mensaje de error. Evita que el texto se acumule.

    Args:
        estado        (EstadoPartida): Estado actual de la partida.
        mensaje_error (str):           Mensaje de error a mostrar.
    """
    mostrar_escena(
        numero_fallos  = estado.numero_fallos,
        palabra_oculta = construir_palabra_oculta(estado),
        letras_usadas  = obtener_letras_usadas(estado),
    )
    mostrar_error(mensaje_error)