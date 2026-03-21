"""
conftest.py
===========
Fixtures compartidos para todos los tests del Ahorcado Medieval.

Este archivo es detectado automáticamente por pytest y sus fixtures
quedan disponibles en todos los archivos de test sin necesidad
de importarlos explícitamente.

Fixtures disponibles:
    bd_prueba       — conexión SQLite en memoria con tabla y datos de prueba
    estado_inicial  — EstadoPartida limpio sin letras jugadas
    estado_con_letras — EstadoPartida con letras ya jugadas
"""

import sqlite3
import pytest

from src.juego.estado.clase_estado_partida import EstadoPartida


# ── Datos de prueba ───────────────────────────────────────────

PALABRAS_DE_PRUEBA: list[tuple[str, str, str]] = [
    ("dragon",    "animales",   "dificil"),
    ("lobo",      "animales",   "facil"),
    ("espada",    "armas",      "facil"),
    ("ballesta",  "armas",      "medio"),
    ("castillo",  "lugares",    "medio"),
    ("caballero", "personajes", "medio"),
]

PALABRA_DE_PRUEBA:   str = "castillo"
CATEGORIA_PRUEBA:    str = "lugares"
DIFICULTAD_PRUEBA:   str = "medio"


# ── Fixtures de base de datos ─────────────────────────────────

@pytest.fixture
def bd_prueba(tmp_path, monkeypatch):
    """
    Crea una base de datos SQLite de prueba en un directorio
    temporal con la tabla 'palabras' poblada con datos de prueba.

    Usa `monkeypatch` para redirigir `RUTA_BASE_DATOS` de
    `conexion.py` al archivo temporal, de forma que todos los
    módulos de `base_datos/` usen la BD de prueba durante el test.

    Args:
        tmp_path   : Directorio temporal provisto por pytest.
        monkeypatch: Fixture de pytest para parchear atributos.

    Yields:
        sqlite3.Connection: Conexión activa a la BD de prueba.
    """
    ruta_bd_temporal = tmp_path / "prueba.db"

    import src.base_datos.conexion.ruta_base_datos as modulo_ruta
    import src.base_datos.conexion.obtener_conexion as modulo_conexion
    monkeypatch.setattr(modulo_ruta,    "RUTA_BASE_DATOS", str(ruta_bd_temporal))
    monkeypatch.setattr(modulo_conexion, "RUTA_BASE_DATOS", str(ruta_bd_temporal))

    conexion = sqlite3.connect(str(ruta_bd_temporal))
    conexion.row_factory = sqlite3.Row

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS palabras (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra    TEXT    NOT NULL UNIQUE,
            categoria  TEXT    NOT NULL,
            dificultad TEXT    NOT NULL
        )
    """)

    conexion.executemany("""
        INSERT OR IGNORE INTO palabras (palabra, categoria, dificultad)
        VALUES (?, ?, ?)
    """, PALABRAS_DE_PRUEBA)

    conexion.commit()

    yield conexion

    conexion.close()


# ── Fixtures de estado de partida ─────────────────────────────

@pytest.fixture
def estado_inicial() -> EstadoPartida:
    """
    Crea un EstadoPartida limpio con la palabra 'castillo',
    sin letras jugadas y con cero fallos.

    Returns:
        EstadoPartida: Estado inicial de prueba.
    """
    return EstadoPartida(
        palabra_secreta = PALABRA_DE_PRUEBA,
        categoria       = CATEGORIA_PRUEBA,
        dificultad      = DIFICULTAD_PRUEBA,
    )


@pytest.fixture
def estado_con_letras() -> EstadoPartida:
    """
    Crea un EstadoPartida con la palabra 'castillo' y algunas
    letras ya jugadas: 'c' y 'a' correctas, 'x' y 'z' fallidas.

    Returns:
        EstadoPartida: Estado con letras jugadas y 2 fallos.
    """
    return EstadoPartida(
        palabra_secreta  = PALABRA_DE_PRUEBA,
        categoria        = CATEGORIA_PRUEBA,
        dificultad       = DIFICULTAD_PRUEBA,
        letras_correctas = {"c", "a"},
        letras_fallidas  = {"x", "z"},
        numero_fallos    = 2,
    )