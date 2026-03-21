"""
test_partida_terminada.py
=========================
Tests para src/juego/logica/partida_terminada.py
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.juego.logica.partida_terminada     import partida_terminada
from src.interfaz.dibujo                    import MAXIMO_FALLOS


def test_sin_condicion_no_termina():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert partida_terminada(estado) is False

def test_victoria_termina_partida():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas=set("castillo"))
    assert partida_terminada(estado) is True

def test_derrota_termina_partida():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           numero_fallos=MAXIMO_FALLOS)
    assert partida_terminada(estado) is True

def test_victoria_con_fallos_termina():
    estado = EstadoPartida(palabra_secreta="rey", categoria="personajes", dificultad="facil",
                           letras_correctas=set("rey"), numero_fallos=3)
    assert partida_terminada(estado) is True