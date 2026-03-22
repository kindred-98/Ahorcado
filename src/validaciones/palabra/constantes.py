"""
constantes.py
=============
Constantes de validación para palabras de la base de datos.
"""

LONGITUD_MINIMA_PALABRA: int = 3
LONGITUD_MAXIMA_PALABRA: int = 30

CATEGORIAS_VALIDAS: frozenset[str] = frozenset({
    "animales",
    "armas",
    "lugares",
    "personajes",
    "otros",
})

DIFICULTADES_VALIDAS: frozenset[str] = frozenset({
    "facil",
    "medio",
    "dificil",
    "legendario",
})

CARACTERES_VALIDOS_PALABRA: frozenset[str] = frozenset(
    "abcdefghijklmnñopqrstuvwxyzáéíóúü"
)