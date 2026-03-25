"""
ejecutar_bucle_de_turnos.py
===========================
Función privada que ejecuta el bucle turno a turno.
"""

from src.juego.estado.clase_estado_partida      import EstadoPartida
from src.juego.estado.registrar_letra           import registrar_letra
from src.juego.logica.partida_terminada         import partida_terminada
from src.juego.bucle.mostrar_turno              import _mostrar_turno
from src.juego.bucle.pedir_letra_valida         import _pedir_letra_valida, INTENTO_PALABRA_COMPLETA
from src.interfaz.pantalla.mostrar_error        import mostrar_error
from src.interfaz.pantalla.mostrar_escena       import mostrar_escena
from src.juego.estado.construir_palabra_oculta  import construir_palabra_oculta
from src.juego.estado.obtener_letras_usadas     import obtener_letras_usadas


def _ejecutar_bucle_de_turnos(estado: EstadoPartida) -> None:
    """
    Ejecuta el bucle turno a turno hasta que la partida termina.

    Gestiona tanto letras individuales como intentos de
    adivinar la palabra completa.

    Args:
        estado (EstadoPartida): Estado inicial de la partida.
    """
    while not partida_terminada(estado):
        _mostrar_turno(estado)
        entrada = _pedir_letra_valida(estado)

        if entrada.startswith(f"{INTENTO_PALABRA_COMPLETA}:"):
            palabra_intentada = entrada.split(":", 1)[1]
            _procesar_intento_palabra(estado, palabra_intentada)
        else:
            registrar_letra(estado, entrada)


def _procesar_intento_palabra(estado: EstadoPartida, palabra_intentada: str) -> None:
    """
    Procesa un intento de adivinar la palabra completa.

    Si acierta revela todas las letras y la partida termina
    en victoria. Si falla suma un fallo y muestra el error.

    Args:
        estado           (EstadoPartida): Estado actual de la partida.
        palabra_intentada (str):          Palabra introducida por el jugador.
    """
    if palabra_intentada == estado.palabra_secreta:
        estado.letras_correctas = set(estado.palabra_secreta)
    else:
        estado.numero_fallos += 1
        mostrar_escena(
            numero_fallos  = estado.numero_fallos,
            palabra_oculta = construir_palabra_oculta(estado),
            letras_usadas  = obtener_letras_usadas(estado),
        )
        mostrar_error(
            f"'{palabra_intentada.upper()}' no es la palabra correcta. "
            f"Pierdes un intento."
        )