"""
test_obtener_letras_usadas.py
=============================
Tests para src/juego/estado/obtener_letras_usadas.py
"""

from src.juego.estado.clase_estado_partida  import EstadoPartida
from src.juego.estado.obtener_letras_usadas import obtener_letras_usadas


def test_sin_letras_devuelve_lista_vacia():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert obtener_letras_usadas(estado) == []

def test_combina_correctas_y_fallidas():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c", "a"}, letras_fallidas={"x", "z"})
    letras = obtener_letras_usadas(estado)
    assert "c" in letras
    assert "a" in letras
    assert "x" in letras
    assert "z" in letras

def test_devuelve_lista_ordenada():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c", "a"}, letras_fallidas={"x", "z"})
    letras = obtener_letras_usadas(estado)
    assert letras == sorted(letras)

def test_devuelve_lista():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert isinstance(obtener_letras_usadas(estado), list)

def test_sin_duplicados():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio",
                           letras_correctas={"c"}, letras_fallidas={"x"})
    letras = obtener_letras_usadas(estado)
    assert len(letras) == len(set(letras))