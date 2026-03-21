"""
test_obtener_palabra_aleatoria.py
=================================
Tests para src/base_datos/consultas/obtener_palabra_aleatoria.py
"""

from src.base_datos.consultas.obtener_palabra_aleatoria import obtener_palabra_aleatoria


def test_devuelve_dict(bd_prueba):
    assert isinstance(obtener_palabra_aleatoria(), dict)

def test_tiene_claves_esperadas(bd_prueba):
    resultado = obtener_palabra_aleatoria()
    assert "palabra"    in resultado
    assert "categoria"  in resultado
    assert "dificultad" in resultado

def test_filtra_por_categoria(bd_prueba):
    resultado = obtener_palabra_aleatoria(categoria="animales")
    assert resultado["categoria"] == "animales"

def test_categoria_inexistente_devuelve_none(bd_prueba):
    assert obtener_palabra_aleatoria(categoria="comida") is None

def test_bd_vacia_devuelve_none(bd_prueba):
    bd_prueba.execute("DELETE FROM palabras")
    bd_prueba.commit()
    assert obtener_palabra_aleatoria() is None

def test_filtra_por_dificultad(bd_prueba):
    resultado = obtener_palabra_aleatoria(dificultad="facil")
    assert resultado["dificultad"] == "facil"

def test_filtros_combinados(bd_prueba):
    resultado = obtener_palabra_aleatoria(categoria="animales", dificultad="facil")
    if resultado:
        assert resultado["categoria"]  == "animales"
        assert resultado["dificultad"] == "facil"