"""
iniciar_partida.py
==================
Función pública — punto de entrada del juego.
"""

from src.juego.estado.crear_estado_inicial      import crear_estado_inicial
from src.juego.bucle.obtener_palabra_o_salir    import _obtener_palabra_o_salir
from src.juego.bucle.ejecutar_bucle_de_turnos   import _ejecutar_bucle_de_turnos
from src.juego.bucle.mostrar_resultado_final    import _mostrar_resultado_final
from src.juego.bucle.preguntar_jugar_otra       import _preguntar_jugar_otra
from src.interfaz.pantalla.limpiar_pantalla     import limpiar_pantalla


def iniciar_partida(categoria: str | None = None) -> None:
    """
    Punto de entrada del juego. Gestiona el ciclo completo
    de partidas hasta que el jugador decide salir.

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