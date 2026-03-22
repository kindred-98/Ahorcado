"""
palabras_iniciales.py
=====================
Constante con las palabras iniciales de la base de datos.
"""

PALABRAS_INICIALES: list[tuple[str, str, str]] = [
    # (palabra, categoria, dificultad)

    # Animales
    ("dragon",      "animales",   "dificil"),
    ("lobo",        "animales",   "facil"),
    ("cuervo",      "animales",   "medio"),
    ("jabali",      "animales",   "medio"),
    ("serpiente",   "animales",   "dificil"),

    # Armas
    ("espada",      "armas",      "facil"),
    ("lanza",       "armas",      "facil"),
    ("escudo",      "armas",      "medio"),
    ("ballesta",    "armas",      "medio"),
    ("mandoble",    "armas",      "dificil"),

    # Lugares
    ("castillo",    "lugares",    "medio"),
    ("mazmorra",    "lugares",    "dificil"),
    ("aldea",       "lugares",    "facil"),
    ("fortaleza",   "lugares",    "dificil"),
    ("taberna",     "lugares",    "medio"),

    # Personajes
    ("caballero",   "personajes", "medio"),
    ("rey",         "personajes", "facil"),
    ("hechicero",   "personajes", "dificil"),
    ("arquero",     "personajes", "medio"),
    ("herrero",     "personajes", "dificil"),
    
    # Otros — legendario
    ("excalibur",   "otros",      "legendario"),
    ("merlín",      "otros",      "legendario"),
    ("grial",       "otros",      "legendario"),
]