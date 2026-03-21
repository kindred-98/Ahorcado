"""
pedir_categoria_opcional.py
===========================
Función privada para mostrar categorías y pedir elección.
"""

from src.base_datos.consultas.obtener_categorias import obtener_categorias
from src.interfaz.pantalla.mostrar_error         import mostrar_error


def _pedir_categoria_opcional() -> str | None:
    """
    Muestra las categorías disponibles y permite al jugador
    elegir una o jugar con todas.

    Returns:
        str | None: Nombre de la categoría elegida o None
                    si el jugador prefiere cualquier categoría.
    """
    categorias = obtener_categorias()

    if not categorias:
        return None

    print("\n  ── Categorías disponibles ──\n")
    print("  0)  Cualquier categoría")
    for indice, registro in enumerate(categorias, start=1):
        print(
            f"  {indice})  {registro['categoria'].capitalize()}"
            f"  ({registro['total']} palabras)"
        )

    opciones_validas = ["0"] + [str(i) for i in range(1, len(categorias) + 1)]

    while True:
        eleccion = input("\n  Elige una categoría > ").strip()
        if eleccion in opciones_validas:
            break
        mostrar_error(f"Elige un número entre 0 y {len(categorias)}.")

    if eleccion == "0":
        return None

    return categorias[int(eleccion) - 1]["categoria"]