"""
pedir_letra_valida.py
=====================
Función privada para pedir una letra válida al jugador.
"""

from src.juego.estado.clase_estado_partida  import EstadoPartida
from src.juego.estado.letra_ya_usada        import letra_ya_usada
from src.validaciones.letra.validar_letra   import validar_letra
from src.interfaz.pantalla.mostrar_error    import mostrar_error


def _pedir_letra_valida(estado: EstadoPartida) -> str:
    """
    Solicita una letra al jugador en bucle hasta recibir
    una entrada válida y no repetida.

    Args:
        estado (EstadoPartida): Estado actual de la partida.

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