"""
test_hay_derrota.py
===================
Tests para src/juego/logica/hay_derrota.py
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.juego.logica.hay_derrota           import hay_derrota
from src.interfaz.dibujo                    import MAXIMO_FALLOS


def test_cero_fallos_no_hay_derrota():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert hay_derrota(estado) is False

def test_cinco_fallos_no_hay_derrota():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           numero_fallos=MAXIMO_FALLOS - 1)
    assert hay_derrota(estado) is False

def test_seis_fallos_hay_derrota():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           numero_fallos=MAXIMO_FALLOS)
    assert hay_derrota(estado) is True

def test_supera_maximo_hay_derrota():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           numero_fallos=MAXIMO_FALLOS + 1)
    assert hay_derrota(estado) is True