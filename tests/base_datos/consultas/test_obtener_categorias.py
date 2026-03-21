"""
test_obtener_categorias.py
==========================
Tests para src/base_datos/consultas/obtener_categorias.py
"""

from src.base_datos.consultas.obtener_categorias import obtener_categorias


def test_devuelve_lista(bd_prueba):
    assert isinstance(obtener_categorias(), list)

def test_tiene_claves_categoria_y_total(bd_prueba):
    for categoria in obtener_categorias():
        assert "categoria" in categoria
        assert "total"     in categoria

def test_total_es_entero(bd_prueba):
    for categoria in obtener_categorias():
        assert isinstance(categoria["total"], int)

def test_bd_vacia_devuelve_lista_vacia(bd_prueba):
    bd_prueba.execute("DELETE FROM palabras")
    bd_prueba.commit()
    assert obtener_categorias() == []