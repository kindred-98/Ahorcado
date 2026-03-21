"""
logica.py
=========
Módulo encargado de las reglas del juego del Ahorcado Medieval.

Responsabilidades:
    - Detectar si el jugador ha ganado la partida.
    - Detectar si el jugador ha perdido la partida.
    - Determinar si una letra pertenece a la palabra secreta.

Importaciones necesarias:
    from src.juego.logica import hay_victoria, hay_derrota, letra_en_palabra
    from src.juego.estado import EstadoPartida
    from src.interfaz.dibujo import MAXIMO_FALLOS
"""

from src.juego.estado import EstadoPartida
from src.interfaz.dibujo import MAXIMO_FALLOS


# ── Funciones públicas ────────────────────────────────────────

def hay_victoria(estado: EstadoPartida) -> bool:
    """
    Comprueba si el jugador ha ganado la partida.

    La victoria se produce cuando todas las letras únicas
    de la palabra secreta han sido adivinadas.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        bool: True si todas las letras han sido reveladas.
              False si aún quedan letras por adivinar.
    """
    letras_unicas_de_la_palabra = set(estado.palabra_secreta)
    return letras_unicas_de_la_palabra.issubset(estado.letras_correctas)


def hay_derrota(estado: EstadoPartida) -> bool:
    """
    Comprueba si el jugador ha perdido la partida.

    La derrota se produce cuando el número de fallos
    acumulados alcanza el máximo permitido.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        bool: True si se alcanzó el límite de fallos.
              False si aún quedan intentos disponibles.
    """
    return estado.numero_fallos >= MAXIMO_FALLOS


def letra_en_palabra(letra: str, palabra_secreta: str) -> bool:
    """
    Comprueba si una letra pertenece a la palabra secreta.

    La comparación se realiza en minúsculas para evitar
    problemas de capitalización.

    Args:
        letra          (str): Letra a comprobar.
        palabra_secreta(str): Palabra secreta de la partida.

    Returns:
        bool: True si la letra está en la palabra.
              False si no está.
    """
    return letra.lower() in palabra_secreta.lower()


def intentos_restantes(estado: EstadoPartida) -> int:
    """
    Calcula el número de intentos que le quedan al jugador.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        int: Número de intentos restantes antes de perder.
    """
    return MAXIMO_FALLOS - estado.numero_fallos


def partida_terminada(estado: EstadoPartida) -> bool:
    """
    Comprueba si la partida ha terminado por cualquier motivo,
    ya sea victoria o derrota.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

    Returns:
        bool: True si la partida terminó. False si continúa.
    """
    return hay_victoria(estado) or hay_derrota(estado)