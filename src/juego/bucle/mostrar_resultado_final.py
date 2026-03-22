"""
mostrar_resultado_final.py
==========================
Función privada para mostrar el resultado final de la partida.
"""

from src.juego.estado.clase_estado_partida   import EstadoPartida
from src.juego.estado.obtener_letras_usadas  import obtener_letras_usadas
from src.juego.logica.hay_victoria           import hay_victoria
from src.interfaz.pantalla.mostrar_escena    import mostrar_escena
from src.interfaz.pantalla.mostrar_mensaje   import mostrar_mensaje
from src.interfaz.pantalla.mostrar_victoria  import mostrar_victoria


def _mostrar_resultado_final(estado: EstadoPartida) -> None:
    """
    Muestra el resultado final de la partida.
    Si el jugador ganó lanza la animación de victoria.
    Si perdió muestra la escena final con la palabra revelada.

    Args:
        estado (EstadoPartida): Estado final de la partida.
    """
    if hay_victoria(estado):
        mostrar_victoria(estado.palabra_secreta)
    else:
        mostrar_escena(
            numero_fallos  = estado.numero_fallos,
            palabra_oculta = estado.palabra_secreta,
            letras_usadas  = obtener_letras_usadas(estado),
        )
        mostrar_mensaje(
            f"  💀  La palabra era: '{estado.palabra_secreta.upper()}'"
        )