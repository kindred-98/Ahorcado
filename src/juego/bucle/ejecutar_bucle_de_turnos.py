"""
ejecutar_bucle_de_turnos.py
===========================
Función privada que ejecuta el bucle turno a turno.
"""

from src.juego.estado.clase_estado_partida  import EstadoPartida
from src.juego.estado.registrar_letra       import registrar_letra
from src.juego.logica.partida_terminada     import partida_terminada
from src.juego.bucle.mostrar_turno          import _mostrar_turno
from src.juego.bucle.pedir_letra_valida     import _pedir_letra_valida


def _ejecutar_bucle_de_turnos(estado: EstadoPartida) -> None:
    """
    Ejecuta el bucle turno a turno hasta que la partida termina.

    Args:
        estado (EstadoPartida): Estado inicial de la partida.
    """
    while not partida_terminada(estado):
        _mostrar_turno(estado)
        letra = _pedir_letra_valida(estado)
        registrar_letra(estado, letra)