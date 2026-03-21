"""
test_hay_victoria.py
====================
Tests para src/juego/logica/hay_victoria.py
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.juego.logica.hay_victoria          import hay_victoria


def test_victoria_todas_las_letras_adivinadas():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas=set("castillo"))
    assert hay_victoria(estado) is True

def test_sin_letras_no_hay_victoria():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert hay_victoria(estado) is False

def test_letras_parciales_no_hay_victoria():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c", "a"})
    assert hay_victoria(estado) is False

def test_victoria_con_letras_repetidas():
    estado = EstadoPartida(palabra_secreta="llorar", categoria="test", dificultad="facil",
                           letras_correctas=set("llorar"))
    assert hay_victoria(estado) is True

def test_victoria_con_fallos_acumulados():
    estado = EstadoPartida(palabra_secreta="rey", categoria="personajes", dificultad="facil",
                           letras_correctas=set("rey"), numero_fallos=3)
    assert hay_victoria(estado) is True