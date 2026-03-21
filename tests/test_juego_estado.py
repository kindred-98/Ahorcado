"""
test_juego_estado.py
====================
Tests unitarios para src/juego/estado.py
"""

import pytest
from src.juego.estado import (
    EstadoPartida,
    crear_estado_inicial,
    construir_palabra_oculta,
    registrar_letra,
    letra_ya_usada,
    obtener_letras_usadas,
)


# ── Tests crear_estado_inicial ────────────────────────────────

def test_crear_estado_inicial_palabra(estado_inicial):
    assert estado_inicial.palabra_secreta == "castillo"

def test_crear_estado_inicial_categoria(estado_inicial):
    assert estado_inicial.categoria == "lugares"

def test_crear_estado_inicial_dificultad(estado_inicial):
    assert estado_inicial.dificultad == "medio"

def test_crear_estado_inicial_sin_letras_correctas(estado_inicial):
    assert len(estado_inicial.letras_correctas) == 0

def test_crear_estado_inicial_sin_letras_fallidas(estado_inicial):
    assert len(estado_inicial.letras_fallidas) == 0

def test_crear_estado_inicial_cero_fallos(estado_inicial):
    assert estado_inicial.numero_fallos == 0

def test_crear_estado_desde_registro():
    registro = {"palabra": "espada", "categoria": "armas", "dificultad": "facil"}
    estado = crear_estado_inicial(registro)
    assert estado.palabra_secreta == "espada"
    assert estado.categoria == "armas"
    assert estado.dificultad == "facil"


# ── Tests construir_palabra_oculta ────────────────────────────

def test_palabra_oculta_sin_letras(estado_inicial):
    resultado = construir_palabra_oculta(estado_inicial)
    assert resultado == "_ _ _ _ _ _ _ _"

def test_palabra_oculta_con_una_letra(estado_inicial):
    estado_inicial.letras_correctas = {"c"}
    resultado = construir_palabra_oculta(estado_inicial)
    assert resultado == "c _ _ _ _ _ _ _"

def test_palabra_oculta_letras_repetidas(estado_inicial):
    # castillo tiene dos 'l' — ambas deben revelarse con una sola letra
    estado_inicial.letras_correctas = {"l"}
    resultado = construir_palabra_oculta(estado_inicial)
    assert resultado == "_ _ _ _ _ l l _"

def test_palabra_oculta_completa(estado_inicial):
    estado_inicial.letras_correctas = set("castillo")
    resultado = construir_palabra_oculta(estado_inicial)
    assert resultado == "c a s t i l l o"

def test_palabra_oculta_es_string(estado_inicial):
    assert isinstance(construir_palabra_oculta(estado_inicial), str)


# ── Tests registrar_letra ─────────────────────────────────────

def test_registrar_letra_correcta_va_a_correctas(estado_inicial):
    registrar_letra(estado_inicial, "c")
    assert "c" in estado_inicial.letras_correctas

def test_registrar_letra_correcta_no_suma_fallo(estado_inicial):
    registrar_letra(estado_inicial, "c")
    assert estado_inicial.numero_fallos == 0

def test_registrar_letra_fallida_va_a_fallidas(estado_inicial):
    registrar_letra(estado_inicial, "x")
    assert "x" in estado_inicial.letras_fallidas

def test_registrar_letra_fallida_suma_un_fallo(estado_inicial):
    registrar_letra(estado_inicial, "x")
    assert estado_inicial.numero_fallos == 1

def test_registrar_misma_letra_correcta_dos_veces(estado_inicial):
    registrar_letra(estado_inicial, "c")
    registrar_letra(estado_inicial, "c")
    # set no duplica, sigue siendo 1 elemento
    assert len(estado_inicial.letras_correctas) == 1
    assert estado_inicial.numero_fallos == 0

def test_registrar_misma_letra_fallida_dos_veces(estado_inicial):
    registrar_letra(estado_inicial, "x")
    registrar_letra(estado_inicial, "x")
    assert len(estado_inicial.letras_fallidas) == 1
    # pero suma fallo dos veces porque no hay protección aquí
    # esa responsabilidad es de bucle.py con letra_ya_usada()
    assert estado_inicial.numero_fallos == 2

def test_registrar_letra_devuelve_estado(estado_inicial):
    resultado = registrar_letra(estado_inicial, "c")
    assert isinstance(resultado, EstadoPartida)

def test_registrar_letra_normaliza_mayuscula(estado_inicial):
    registrar_letra(estado_inicial, "C")
    assert "c" in estado_inicial.letras_correctas


# ── Tests letra_ya_usada ──────────────────────────────────────

def test_letra_ya_usada_en_correctas(estado_con_letras):
    assert letra_ya_usada(estado_con_letras, "c") is True

def test_letra_ya_usada_en_fallidas(estado_con_letras):
    assert letra_ya_usada(estado_con_letras, "x") is True

def test_letra_no_usada_devuelve_false(estado_con_letras):
    assert letra_ya_usada(estado_con_letras, "m") is False

def test_letra_ya_usada_mayuscula(estado_con_letras):
    assert letra_ya_usada(estado_con_letras, "C") is True


# ── Tests obtener_letras_usadas ───────────────────────────────

def test_letras_usadas_sin_letras(estado_inicial):
    assert obtener_letras_usadas(estado_inicial) == []

def test_letras_usadas_combina_correctas_y_fallidas(estado_con_letras):
    letras = obtener_letras_usadas(estado_con_letras)
    assert "c" in letras
    assert "a" in letras
    assert "x" in letras
    assert "z" in letras

def test_letras_usadas_ordenadas_alfabeticamente(estado_con_letras):
    letras = obtener_letras_usadas(estado_con_letras)
    assert letras == sorted(letras)

def test_letras_usadas_devuelve_lista(estado_inicial):
    assert isinstance(obtener_letras_usadas(estado_inicial), list)