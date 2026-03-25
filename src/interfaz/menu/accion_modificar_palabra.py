"""
accion_modificar_palabra.py
===========================
Acción del submenú: modificar una palabra existente.
"""

from src.interfaz.pantalla.limpiar_pantalla      import limpiar_pantalla
from src.interfaz.pantalla.mostrar_mensaje       import mostrar_mensaje
from src.interfaz.pantalla.mostrar_error         import mostrar_error
from src.interfaz.menu.pedir_campo_validado      import _pedir_campo_validado
from src.base_datos.insercion.actualizar_palabra import actualizar_palabra
from src.base_datos.insercion.palabra_ya_existe  import palabra_ya_existe
from src.validaciones.palabra.validar_palabra    import validar_palabra
from src.validaciones.palabra.validar_categoria  import validar_categoria
from src.validaciones.palabra.validar_dificultad import validar_dificultad
from src.validaciones.palabra.constantes         import CATEGORIAS_VALIDAS, DIFICULTADES_VALIDAS


def _accion_modificar_palabra() -> None:
    """
    Solicita la palabra a modificar, verifica que existe
    y pide los nuevos valores validando cada campo.
    """
    limpiar_pantalla()
    print("\n  ╔══════════════════════════════════════════════╗")
    print("  ║       ✏️  MODIFICAR PALABRA                  ║")
    print("  ╚══════════════════════════════════════════════╝\n")

    palabra_original = input("  Palabra a modificar > ").strip().lower()

    if not palabra_original:
        mostrar_error("Debes ingresar una palabra.")
        input("\n  Presiona ENTER para continuar...")
        return

    if not palabra_ya_existe(palabra_original):
        mostrar_error(f"La palabra '{palabra_original}' no existe en la base de datos.")
        input("\n  Presiona ENTER para continuar...")
        return

    print(f"\n  Modificando: '{palabra_original.upper()}'\n")

    categorias_texto   = " / ".join(sorted(CATEGORIAS_VALIDAS))
    dificultades_texto = " / ".join(sorted(DIFICULTADES_VALIDAS))

    nueva_palabra = _pedir_campo_validado(
        etiqueta  = "Nueva palabra",
        validador = validar_palabra,
    )
    nueva_categoria = _pedir_campo_validado(
        etiqueta  = f"Nueva categoría ({categorias_texto})",
        validador = validar_categoria,
    )
    nueva_dificultad = _pedir_campo_validado(
        etiqueta  = f"Nueva dificultad ({dificultades_texto})",
        validador = validar_dificultad,
    )

    if actualizar_palabra(palabra_original, nueva_palabra, nueva_categoria, nueva_dificultad):
        mostrar_mensaje(
            f"✅  Palabra actualizada: '{nueva_palabra.upper()}' "
            f"({nueva_categoria} / {nueva_dificultad})"
        )
    else:
        mostrar_error("No se pudo actualizar la palabra. Inténtalo de nuevo.")

    input("\n  Presiona ENTER para continuar...")