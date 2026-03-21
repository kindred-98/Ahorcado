"""
accion_jugar.py
===============
Acción del menú: iniciar una partida.
"""

from src.interfaz.pantalla.limpiar_pantalla      import limpiar_pantalla
from src.interfaz.menu.pedir_categoria_opcional  import _pedir_categoria_opcional
from src.juego.bucle.iniciar_partida             import iniciar_partida


def _accion_jugar() -> None:
    """
    Muestra las categorías disponibles, el jugador elige una
    y se inicia la partida.
    """
    limpiar_pantalla()
    categoria_elegida = _pedir_categoria_opcional()
    iniciar_partida(categoria=categoria_elegida)