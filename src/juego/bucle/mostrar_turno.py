"""
mostrar_turno.py
================
Función privada para renderizar la escena de un turno.
"""

from src.juego.estado.clase_estado_partida      import EstadoPartida
from src.juego.estado.construir_palabra_oculta  import construir_palabra_oculta
from src.juego.estado.obtener_letras_usadas     import obtener_letras_usadas
from src.juego.logica.intentos_restantes        import intentos_restantes
from src.interfaz.pantalla.mostrar_escena       import mostrar_escena
from src.interfaz.pantalla.mostrar_mensaje      import mostrar_mensaje


def _mostrar_turno(estado: EstadoPartida) -> None:
    """
    Renderiza la escena completa del turno actual.

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