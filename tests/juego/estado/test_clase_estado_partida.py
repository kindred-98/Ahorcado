"""
test_clase_estado_partida.py
============================
Tests para src/juego/estado/clase_estado_partida.py
"""

from src.juego.estado.clase_estado_partida import EstadoPartida


def test_estado_tiene_palabra_secreta():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert estado.palabra_secreta == "castillo"

def test_estado_tiene_categoria():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert estado.categoria == "lugares"

def test_estado_tiene_dificultad():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert estado.dificultad == "medio"

def test_estado_letras_correctas_vacio_por_defecto():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert estado.letras_correctas == set()

def test_estado_letras_fallidas_vacio_por_defecto():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert estado.letras_fallidas == set()

def test_estado_numero_fallos_cero_por_defecto():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    assert estado.numero_fallos == 0

def test_estados_no_comparten_sets():
    estado1 = EstadoPartida(palabra_secreta="rey", categoria="personajes", dificultad="facil")
    estado2 = EstadoPartida(palabra_secreta="lobo", categoria="animales", dificultad="facil")
    estado1.letras_correctas.add("r")
    assert "r" not in estado2.letras_correctas