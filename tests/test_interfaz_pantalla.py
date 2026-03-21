"""
test_interfaz_pantalla.py
=========================
Tests para src/interfaz/pantalla.py
"""

from src.interfaz.pantalla import (
    construir_cabecera,
    mostrar_mensaje,
    mostrar_error,
)
from src.interfaz.dibujo import MAXIMO_FALLOS


# Accedemos a las funciones privadas directamente para testearlas
from src.interfaz.pantalla import (
    _formatear_letras_usadas,
    _construir_etiqueta_fallos,
)


# ── Tests construir_cabecera ──────────────────────────────────

def test_cabecera_contiene_titulo():
    cabecera = construir_cabecera("_ _ _ _ _ _ _ _", [])
    assert "AHORCADO MEDIEVAL" in cabecera

def test_cabecera_contiene_palabra_oculta():
    cabecera = construir_cabecera("c _ s t _ _ _ o", [])
    assert "c _ s t _ _ _ o" in cabecera

def test_cabecera_sin_letras_muestra_ninguna():
    cabecera = construir_cabecera("_ _ _ _ _ _ _ _", [])
    assert "ninguna" in cabecera

def test_cabecera_con_letras_las_muestra():
    cabecera = construir_cabecera("_ _ _ _ _ _ _ _", ["a", "c"])
    assert "A" in cabecera
    assert "C" in cabecera

def test_cabecera_devuelve_string():
    resultado = construir_cabecera("_ _ _", [])
    assert isinstance(resultado, str)

def test_cabecera_tiene_bordes():
    cabecera = construir_cabecera("_ _ _", [])
    assert "╔" in cabecera
    assert "╚" in cabecera


# ── Tests _formatear_letras_usadas ────────────────────────────

def test_formatear_letras_vacia_devuelve_ninguna():
    assert _formatear_letras_usadas([]) == "Letras usadas: ninguna"

def test_formatear_letras_en_mayusculas():
    resultado = _formatear_letras_usadas(["a", "b"])
    assert "A" in resultado
    assert "B" in resultado

def test_formatear_letras_separadas_por_coma():
    resultado = _formatear_letras_usadas(["a", "b"])
    assert "," in resultado

def test_formatear_letras_devuelve_string():
    assert isinstance(_formatear_letras_usadas(["a"]), str)


# ── Tests _construir_etiqueta_fallos ──────────────────────────

def test_etiqueta_cero_fallos():
    resultado = _construir_etiqueta_fallos(0)
    assert "Sin fallos" in resultado

def test_etiqueta_fallos_maximos():
    resultado = _construir_etiqueta_fallos(MAXIMO_FALLOS)
    assert "intentos" in resultado.lower()

def test_etiqueta_fallos_intermedios():
    resultado = _construir_etiqueta_fallos(3)
    assert "3" in resultado
    assert str(MAXIMO_FALLOS) in resultado

def test_etiqueta_devuelve_string():
    assert isinstance(_construir_etiqueta_fallos(0), str)


# ── Tests mostrar_mensaje y mostrar_error (smoke tests) ───────

def test_mostrar_mensaje_no_lanza_excepcion(capsys):
    mostrar_mensaje("Hola caballero")
    salida = capsys.readouterr().out
    assert "Hola caballero" in salida

def test_mostrar_error_incluye_simbolo(capsys):
    mostrar_error("Error de prueba")
    salida = capsys.readouterr().out
    assert "⚠" in salida
    assert "Error de prueba" in salida