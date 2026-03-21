"""
test_letra_ya_usada.py
======================
Tests para src/juego/estado/letra_ya_usada.py
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.juego.estado.letra_ya_usada       import letra_ya_usada


def test_letra_en_correctas_devuelve_true():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c", "a"})
    assert letra_ya_usada(estado, "c") is True

def test_letra_en_fallidas_devuelve_true():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_fallidas={"x", "z"})
    assert letra_ya_usada(estado, "x") is True

def test_letra_nueva_devuelve_false():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c"}, letras_fallidas={"x"})
    assert letra_ya_usada(estado, "m") is False

def test_mayuscula_detectada_como_usada():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c"})
    assert letra_ya_usada(estado, "C") is True

def test_sin_letras_devuelve_false():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert letra_ya_usada(estado, "c") is False