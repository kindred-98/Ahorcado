"""
preguntar_jugar_otra.py
=======================
Función privada para preguntar si el jugador quiere otra partida.
"""

from src.interfaz.pantalla.mostrar_error import mostrar_error


RESPUESTA_JUGAR_OTRA: tuple[str, ...] = ("s", "si", "sí")
RESPUESTA_NO_JUGAR:   tuple[str, ...] = ("n", "no")


def _preguntar_jugar_otra() -> bool:
    """
    Pregunta al jugador si desea iniciar otra partida.

    Returns:
        bool: True si quiere jugar otra. False si prefiere salir.
    """
    while True:
        respuesta = input("\n  ¿Jugar otra partida? (s/n) > ").strip().lower()

        if respuesta in RESPUESTA_JUGAR_OTRA:
            return True
        if respuesta in RESPUESTA_NO_JUGAR:
            return False

        mostrar_error("Responde con 's' para sí o 'n' para no.")