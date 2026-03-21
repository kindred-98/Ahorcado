"""
test_registrar_letra.py
=======================
Tests para src/juego/estado/registrar_letra.py
"""

from src.juego.estado.clase_estado_partida import EstadoPartida
from src.juego.estado.registrar_letra      import registrar_letra


def test_letra_correcta_va_a_correctas():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    registrar_letra(estado, "c")
    assert "c" in estado.letras_correctas

def test_letra_correcta_no_suma_fallo():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    registrar_letra(estado, "c")
    assert estado.numero_fallos == 0

def test_letra_fallida_va_a_fallidas():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    registrar_letra(estado, "x")
    assert "x" in estado.letras_fallidas

def test_letra_fallida_suma_un_fallo():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    registrar_letra(estado, "x")
    assert estado.numero_fallos == 1

def test_misma_letra_correcta_dos_veces_no_duplica():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    registrar_letra(estado, "c")
    registrar_letra(estado, "c")
    assert len(estado.letras_correctas) == 1

def test_normaliza_mayuscula():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    registrar_letra(estado, "C")
    assert "c" in estado.letras_correctas

def test_devuelve_estado_partida():
    estado = EstadoPartida(palabra_secreta="castillo", categoria="lugares", dificultad="medio")
    resultado = registrar_letra(estado, "c")
    assert isinstance(resultado, EstadoPartida)