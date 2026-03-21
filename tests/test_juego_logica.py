"""
test_juego_logica.py
====================
Tests unitarios para src/juego/logica.py
"""

from src.juego.estado import EstadoPartida
from src.juego.logica import (
    hay_victoria,
    hay_derrota,
    letra_en_palabra,
    intentos_restantes,
    partida_terminada,
)
from src.interfaz.dibujo import MAXIMO_FALLOS


# ── Tests hay_victoria ────────────────────────────────────────

def test_hay_victoria_todas_las_letras_adivinadas(estado_inicial):
    estado_inicial.letras_correctas = set("castillo")
    assert hay_victoria(estado_inicial) is True

def test_hay_victoria_false_sin_letras(estado_inicial):
    assert hay_victoria(estado_inicial) is False

def test_hay_victoria_false_letras_parciales(estado_inicial):
    estado_inicial.letras_correctas = {"c", "a"}
    assert hay_victoria(estado_inicial) is False

def test_hay_victoria_letras_repetidas_basta_una_vez():
    # "llorar" tiene dos 'l' — basta con tener 'l' una vez en el set
    estado = EstadoPartida(
        palabra_secreta  = "llorar",
        categoria        = "test",
        dificultad       = "facil",
        letras_correctas = set("llorar"),
    )
    assert hay_victoria(estado) is True


# ── Tests hay_derrota ─────────────────────────────────────────

def test_hay_derrota_false_con_cero_fallos(estado_inicial):
    assert hay_derrota(estado_inicial) is False

def test_hay_derrota_false_con_cinco_fallos(estado_inicial):
    estado_inicial.numero_fallos = MAXIMO_FALLOS - 1
    assert hay_derrota(estado_inicial) is False

def test_hay_derrota_true_con_seis_fallos(estado_inicial):
    estado_inicial.numero_fallos = MAXIMO_FALLOS
    assert hay_derrota(estado_inicial) is True

def test_hay_derrota_true_supera_maximo(estado_inicial):
    estado_inicial.numero_fallos = MAXIMO_FALLOS + 1
    assert hay_derrota(estado_inicial) is True


# ── Tests letra_en_palabra ────────────────────────────────────

def test_letra_en_palabra_true():
    assert letra_en_palabra("c", "castillo") is True

def test_letra_en_palabra_false():
    assert letra_en_palabra("x", "castillo") is False

def test_letra_en_palabra_mayuscula():
    assert letra_en_palabra("C", "castillo") is True

def test_letra_en_palabra_tilde():
    assert letra_en_palabra("é", "caballero") is False

def test_letra_en_palabra_repetida():
    # 'l' aparece dos veces en castillo
    assert letra_en_palabra("l", "castillo") is True


# ── Tests intentos_restantes ──────────────────────────────────

def test_intentos_restantes_cero_fallos(estado_inicial):
    assert intentos_restantes(estado_inicial) == MAXIMO_FALLOS

def test_intentos_restantes_tres_fallos(estado_inicial):
    estado_inicial.numero_fallos = 3
    assert intentos_restantes(estado_inicial) == 3

def test_intentos_restantes_derrota(estado_inicial):
    estado_inicial.numero_fallos = MAXIMO_FALLOS
    assert intentos_restantes(estado_inicial) == 0

def test_intentos_restantes_devuelve_entero(estado_inicial):
    assert isinstance(intentos_restantes(estado_inicial), int)


# ── Tests partida_terminada ───────────────────────────────────

def test_partida_no_terminada(estado_inicial):
    assert partida_terminada(estado_inicial) is False

def test_partida_terminada_por_victoria(estado_inicial):
    estado_inicial.letras_correctas = set("castillo")
    assert partida_terminada(estado_inicial) is True

def test_partida_terminada_por_derrota(estado_inicial):
    estado_inicial.numero_fallos = MAXIMO_FALLOS
    assert partida_terminada(estado_inicial) is True

def test_partida_terminada_victoria_con_fallos(estado_inicial):
    # puede ganar aunque tenga fallos
    estado_inicial.letras_correctas = set("castillo")
    estado_inicial.numero_fallos    = 3
    assert partida_terminada(estado_inicial) is True