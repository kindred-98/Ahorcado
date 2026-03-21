# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
## FASE 9 — Refactorización modular (cierre)
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Fase final de la refactorización. Se completan los tres módulos restantes:
`interfaz/pantalla/`, `juego/bucle/` e `interfaz/menu/`. Con esto el proyecto
tiene un archivo por función/clase en toda la base de código.

---

## INTERACCIÓN 1 — Refactorización de interfaz/pantalla/

### 🔵 S — Situación

`pantalla.py` tenía 5 funciones públicas y 2 privadas. Era el módulo más
crítico de `interfaz/` porque `menu.py`, `bucle.py` y `test_cobertura_completa.py`
dependen directamente de él.

### 🔴 P — Problema

Al convertirlo en carpeta todos los módulos que importaban funciones de
`pantalla` perdían sus imports. También afectaba a `test_cobertura_completa.py`
que importaba `mostrar_escena`.

### 🟠 E — Exploración

**Prompt enviado:**

> *"listo"*

### 🟢 C — Cambios

`src/interfaz/pantalla.py` → `src/interfaz/pantalla/`:

| Archivo nuevo | Función/Clase | Tipo |
|---|---|---|
| `limpiar_pantalla.py` | `limpiar_pantalla()` | pública |
| `formatear_letras_usadas.py` | `_formatear_letras_usadas()` | privada |
| `construir_etiqueta_fallos.py` | `_construir_etiqueta_fallos()` | privada |
| `construir_cabecera.py` | `construir_cabecera()` | pública |
| `mostrar_mensaje.py` | `mostrar_mensaje()` | pública |
| `mostrar_error.py` | `mostrar_error()` | pública |
| `mostrar_escena.py` | `mostrar_escena()` | pública |

Tests refactorizados en `tests/interfaz/pantalla/`:

| Archivo nuevo | Tests |
|---|---|
| `test_construir_cabecera.py` | 6 tests |
| `test_mostrar_escena.py` | 4 tests |
| `test_mostrar_mensaje.py` | 2 tests |
| `test_mostrar_error.py` | 3 tests |
| `test_formatear_letras_usadas.py` | 4 tests |
| `test_construir_etiqueta_fallos.py` | 4 tests |

**Imports actualizados:**

| Archivo | Import corregido |
|---|---|
| `menu.py` | imports individuales de `limpiar_pantalla`, `mostrar_mensaje`, `mostrar_error` |
| `bucle.py` | imports individuales de `mostrar_escena`, `mostrar_mensaje`, `mostrar_error`, `limpiar_pantalla` |
| `test_cobertura_completa.py` | `from src.interfaz.pantalla.mostrar_escena import mostrar_escena` |

### 🔵 A — Acuerdo

✅ 7 archivos de código + 6 de tests.  
✅ `test_interfaz_pantalla.py` original borrado.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `interfaz/pantalla/` refactorizado.

---

## INTERACCIÓN 2 — Refactorización de juego/bucle/

### 🔵 S — Situación

`bucle.py` era el módulo más complejo del proyecto: orquestaba la BD,
el estado, la lógica, las validaciones y la interfaz. Tenía 1 función
pública y 6 privadas.

### 🔴 P — Problema

Al separarlo en archivos, cada función privada necesitaba importar de
múltiples módulos ya refactorizados con sus nuevas rutas explícitas.

### 🟠 E — Exploración

**Prompt enviado:**

> *"listo"*

### 🟢 C — Cambios

`src/juego/bucle.py` → `src/juego/bucle/`:

| Archivo nuevo | Función/Clase | Tipo |
|---|---|---|
| `obtener_palabra_o_salir.py` | `_obtener_palabra_o_salir()` | privada |
| `mostrar_turno.py` | `_mostrar_turno()` | privada |
| `pedir_letra_valida.py` | `_pedir_letra_valida()` | privada |
| `ejecutar_bucle_de_turnos.py` | `_ejecutar_bucle_de_turnos()` | privada |
| `mostrar_resultado_final.py` | `_mostrar_resultado_final()` | privada |
| `preguntar_jugar_otra.py` | `_preguntar_jugar_otra()` | privada |
| `iniciar_partida.py` | `iniciar_partida()` | pública |

No se crearon tests nuevos — `bucle` usa `input()` y queda fuera del
scope de tests unitarios definido en la Fase 6.

**Imports actualizados:**

| Archivo | Import corregido |
|---|---|
| `menu.py` | `from src.juego.bucle.iniciar_partida import iniciar_partida` |

### 🔵 A — Acuerdo

✅ 7 archivos de código.  
✅ Sin tests nuevos (usa `input()`).

### 🟢 R — Resultado

Todos los tests pasan. Módulo `juego/bucle/` refactorizado.

---

## INTERACCIÓN 3 — Refactorización de interfaz/menu/

### 🔵 S — Situación

`menu.py` era el último módulo en refactorizarse. Tenía 3 funciones
públicas, 7 privadas y 4 constantes. Era el módulo con más dependencias
del proyecto porque conecta todos los demás.

### 🔴 P — Problema

Al separarlo en archivos, el punto de entrada `ahorcado.py` perdía su
import de `ejecutar_menu_principal`.

### 🟠 E — Exploración

**Prompt enviado:**

> *"listo"*

### 🟢 C — Cambios

`src/interfaz/menu.py` → `src/interfaz/menu/`:

| Archivo nuevo | Función/Clase | Tipo |
|---|---|---|
| `constantes_menu.py` | `OPCION_JUGAR`, `OPCION_AÑADIR_PALABRA`, `OPCION_VER_PALABRAS`, `OPCION_SALIR`, `OPCIONES_VALIDAS` | constantes |
| `construir_menu.py` | `_construir_menu()` | privada |
| `mostrar_menu_principal.py` | `mostrar_menu_principal()` | pública |
| `pedir_opcion_menu.py` | `pedir_opcion_menu()` | pública |
| `pedir_campo_validado.py` | `_pedir_campo_validado()` | privada |
| `pedir_categoria_opcional.py` | `_pedir_categoria_opcional()` | privada |
| `accion_jugar.py` | `_accion_jugar()` | privada |
| `accion_añadir_palabra.py` | `_accion_añadir_palabra()` | privada |
| `accion_ver_palabras.py` | `_accion_ver_palabras()` | privada |
| `accion_salir.py` | `_accion_salir()` | privada |
| `ejecutar_menu_principal.py` | `ejecutar_menu_principal()` | pública |

No se crearon tests nuevos — `menu` usa `input()` igual que `bucle`.

**Imports actualizados:**

| Archivo | Import corregido |
|---|---|
| `ahorcado.py` | `from src.interfaz.menu.ejecutar_menu_principal import ejecutar_menu_principal` |

### 🔵 A — Acuerdo

✅ 11 archivos de código.  
✅ Sin tests nuevos (usa `input()`).

### 🟢 R — Resultado

Todos los tests pasan. Módulo `interfaz/menu/` refactorizado.
**Refactorización completa del proyecto.**

---

## Catálogo de archivos refactorizados — Fase 9

### `src/interfaz/pantalla/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `limpiar_pantalla.py` | `limpiar_pantalla()` | pública |
| `formatear_letras_usadas.py` | `_formatear_letras_usadas()` | privada |
| `construir_etiqueta_fallos.py` | `_construir_etiqueta_fallos()` | privada |
| `construir_cabecera.py` | `construir_cabecera()` | pública |
| `mostrar_mensaje.py` | `mostrar_mensaje()` | pública |
| `mostrar_error.py` | `mostrar_error()` | pública |
| `mostrar_escena.py` | `mostrar_escena()` | pública |

---

### `src/juego/bucle/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `obtener_palabra_o_salir.py` | `_obtener_palabra_o_salir()` | privada |
| `mostrar_turno.py` | `_mostrar_turno()` | privada |
| `pedir_letra_valida.py` | `_pedir_letra_valida()` | privada |
| `ejecutar_bucle_de_turnos.py` | `_ejecutar_bucle_de_turnos()` | privada |
| `mostrar_resultado_final.py` | `_mostrar_resultado_final()` | privada |
| `preguntar_jugar_otra.py` | `_preguntar_jugar_otra()` | privada |
| `iniciar_partida.py` | `iniciar_partida()` | pública |

---

### `src/interfaz/menu/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `constantes_menu.py` | `OPCION_JUGAR`, `OPCION_AÑADIR_PALABRA`, `OPCION_VER_PALABRAS`, `OPCION_SALIR`, `OPCIONES_VALIDAS` | constantes |
| `construir_menu.py` | `_construir_menu()` | privada |
| `mostrar_menu_principal.py` | `mostrar_menu_principal()` | pública |
| `pedir_opcion_menu.py` | `pedir_opcion_menu()` | pública |
| `pedir_campo_validado.py` | `_pedir_campo_validado()` | privada |
| `pedir_categoria_opcional.py` | `_pedir_categoria_opcional()` | privada |
| `accion_jugar.py` | `_accion_jugar()` | privada |
| `accion_añadir_palabra.py` | `_accion_añadir_palabra()` | privada |
| `accion_ver_palabras.py` | `_accion_ver_palabras()` | privada |
| `accion_salir.py` | `_accion_salir()` | privada |
| `ejecutar_menu_principal.py` | `ejecutar_menu_principal()` | pública |

---

## Estado final del proyecto

```
src/
├── validaciones/
│   ├── letra/         — 3 archivos
│   └── palabra/       — 5 archivos
├── juego/
│   ├── estado/        — 6 archivos
│   ├── logica/        — 5 archivos
│   └── bucle/         — 7 archivos
├── base_datos/
│   ├── conexion/      — 2 archivos
│   ├── inicializar/   — 4 archivos
│   ├── consultas/     — 4 archivos
│   └── insercion/     — 3 archivos
└── interfaz/
    ├── dibujo/        — 2 archivos
    ├── pantalla/      — 7 archivos
    └── menu/          — 11 archivos
```

**Total: 59 archivos de código fuente.**

---

## Resumen de decisiones — Fase 9

| Elemento | Decisión |
|---|---|
| Tests para `bucle/` y `menu/` | ❌ Usan `input()`, fuera de scope |
| Tests para `pantalla/` | ✅ 6 archivos de test creados |
| Archivos antiguos borrados | ✅ `pantalla.py`, `bucle.py`, `menu.py` |
| Imports en `ahorcado.py` | ✅ Actualizado al último import |
| Refactorización completa | ✅ Un archivo por función/clase en todo el proyecto |