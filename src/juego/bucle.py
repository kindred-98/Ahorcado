"""
bucle.py
========
Módulo encargado del bucle principal de una partida
del Ahorcado Medieval.

Responsabilidades:
    - Obtener una palabra aleatoria de la base de datos.
    - Coordinar el flujo turno a turno de la partida.
    - Pedir letra al jugador y actualizar el estado.
    - Mostrar la escena actualizada en cada turno.
    - Detectar victoria o derrota y mostrar el resultado.
    - Preguntar si el jugador quiere jugar otra partida.

Importaciones necesarias:
    from src.juego.bucle import iniciar_partida
"""
# después
from src.juego.logica.hay_victoria       import hay_victoria
from src.juego.logica.partida_terminada  import partida_terminada
from src.juego.logica.intentos_restantes import intentos_restantes


from src.juego.estado import (
    EstadoPartida,
    crear_estado_inicial,
    construir_palabra_oculta,
    registrar_letra,
    letra_ya_usada,
    obtener_letras_usadas,
)
from src.base_datos.consultas.obtener_palabra_aleatoria import obtener_palabra_aleatoria
from src.interfaz.pantalla import (
    mostrar_escena,
    mostrar_mensaje,
    mostrar_error,
    limpiar_pantalla,
)
from src.validaciones.letra import validar_letra


# ── Constantes ────────────────────────────────────────────────

RESPUESTA_JUGAR_OTRA: tuple[str, ...] = ("s", "si", "sí")
RESPUESTA_NO_JUGAR:   tuple[str, ...] = ("n", "no")


# ── Función pública principal ─────────────────────────────────

def iniciar_partida(categoria: str | None = None) -> None:
    """
    Punto de entrada del juego. Gestiona el ciclo completo
    de partidas hasta que el jugador decide salir.

    Obtiene una palabra de la base de datos, ejecuta el bucle
    de turnos y al terminar pregunta si desea jugar otra.

    Args:
        categoria (str | None): Categoría de palabras a usar.
                                Si es None se elige de todas.
    """
    while True:
        registro_palabra = _obtener_palabra_o_salir(categoria)
        if registro_palabra is None:
            return

        estado = crear_estado_inicial(registro_palabra)
        _ejecutar_bucle_de_turnos(estado)
        _mostrar_resultado_final(estado)

        if not _preguntar_jugar_otra():
            limpiar_pantalla()
            break


# ── Funciones privadas — flujo de partida ─────────────────────

def _obtener_palabra_o_salir(categoria: str | None) -> dict | None:
    """
    Intenta obtener una palabra aleatoria de la base de datos.
    Si no encuentra ninguna informa al jugador y termina.

    Args:
        categoria (str | None): Filtro de categoría opcional.

    Returns:
        dict | None: Registro de la palabra o None si no hay palabras.
    """
    registro_palabra = obtener_palabra_aleatoria(categoria=categoria)

    if registro_palabra is None:
        mostrar_error(
            "No se encontraron palabras disponibles"
            + (f" en la categoría '{categoria}'." if categoria else ".")
        )
        return None

    return registro_palabra


def _ejecutar_bucle_de_turnos(estado: EstadoPartida) -> None:
    """
    Ejecuta el bucle turno a turno de una partida.

    En cada turno muestra la escena, pide una letra al jugador,
    la valida y actualiza el estado hasta que la partida termina.

    Args:
        estado (EstadoPartida): Estado inicial de la partida.
    """
    while not partida_terminada(estado):
        _mostrar_turno(estado)
        letra = _pedir_letra_valida(estado)
        registrar_letra(estado, letra)


def _mostrar_turno(estado: EstadoPartida) -> None:
    """
    Renderiza la escena completa del turno actual:
    arte ASCII, palabra oculta y letras usadas.

    Args:
        estado (EstadoPartida): Estado actual de la partida.
    """
    mostrar_escena(
        numero_fallos  = estado.numero_fallos,
        palabra_oculta = construir_palabra_oculta(estado),
        letras_usadas  = obtener_letras_usadas(estado),
    )
    mostrar_mensaje(
        f"  Categoría: {estado.categoria}  |  "
        f"Intentos restantes: {intentos_restantes(estado)}"
    )


def _pedir_letra_valida(estado: EstadoPartida) -> str:
    """
    Solicita una letra al jugador en bucle hasta recibir
    una entrada válida y no repetida.

    Args:
        estado (EstadoPartida): Estado actual para comprobar
                                letras ya usadas.

    Returns:
        str: Letra válida en minúscula lista para registrar.
    """
    while True:
        entrada = input("  Ingresa una letra > ").strip().lower()

        error = validar_letra(entrada)
        if error:
            mostrar_error(error)
            continue

        if letra_ya_usada(estado, entrada):
            mostrar_error(f"La letra '{entrada.upper()}' ya fue usada. Intenta con otra.")
            continue

        return entrada


# ── Funciones privadas — resultado ────────────────────────────

def _mostrar_resultado_final(estado: EstadoPartida) -> None:
    """
    Muestra la escena final de la partida con el mensaje
    correspondiente a victoria o derrota.

    Args:
        estado (EstadoPartida): Estado final de la partida.
    """
    mostrar_escena(
        numero_fallos  = estado.numero_fallos,
        palabra_oculta = estado.palabra_secreta,
        letras_usadas  = obtener_letras_usadas(estado),
    )

    if hay_victoria(estado):
        mostrar_mensaje(
            f"  ⚔  ¡Victoria, caballero! La palabra era: "
            f"'{estado.palabra_secreta.upper()}'"
        )
    else:
        mostrar_mensaje(
            f"  💀  La palabra era: '{estado.palabra_secreta.upper()}'"
        )


def _preguntar_jugar_otra() -> bool:
    """
    Pregunta al jugador si desea iniciar otra partida.

    Returns:
        bool: True si el jugador quiere jugar otra partida.
              False si prefiere volver al menú principal.
    """
    while True:
        respuesta = input("\n  ¿Jugar otra partida? (s/n) > ").strip().lower()

        if respuesta in RESPUESTA_JUGAR_OTRA:
            return True
        if respuesta in RESPUESTA_NO_JUGAR:
            return False

        mostrar_error("Responde con 's' para sí o 'n' para no.")