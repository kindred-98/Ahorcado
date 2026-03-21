# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
## FASE 8 — Refactorización modular (continuación)
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Continuación de la Fase 7. Se completa la refactorización de los módulos
`base_datos/` e `interfaz/dibujo/`, incluyendo la corrección de todos los
imports rotos detectados por pytest en cada paso.

---

## INTERACCIÓN 1 — Refactorización de base_datos/inicializar/

### 🔵 S — Situación

`inicializar.py` tenía la función pública, dos privadas y las 20 palabras
iniciales todo junto. Era el cuarto módulo de `base_datos/` en refactorizarse.

### 🔴 P — Problema

Al convertirlo en carpeta, `ahorcado.py` y `test_cobertura_completa.py`
perdieron el import de `inicializar_base_datos`.

### 🟠 E — Exploración

**Prompt enviado:**

> *"listo"*

### 🟢 C — Cambios

`src/base_datos/inicializar.py` → `src/base_datos/inicializar/`:

| Archivo nuevo | Contenido |
|---|---|
| `palabras_iniciales.py` | Constante `PALABRAS_INICIALES` con las 20 palabras |
| `crear_tabla_palabras.py` | Función privada `_crear_tabla_palabras()` |
| `poblar_palabras_iniciales.py` | Función privada `_poblar_palabras_iniciales()` |
| `inicializar_base_datos.py` | Función pública `inicializar_base_datos()` |

Tests refactorizados en `tests/base_datos/inicializar/`:

| Archivo nuevo | Contenido |
|---|---|
| `test_inicializar_base_datos.py` | 4 tests |

**Imports actualizados:**

| Archivo | Import corregido |
|---|---|
| `ahorcado.py` | `from src.base_datos.inicializar.inicializar_base_datos import inicializar_base_datos` |
| `test_cobertura_completa.py` | mismo import + monkeypatch actualizado a ruta específica |

### 🔵 A — Acuerdo

✅ 4 archivos de código + 1 de tests.  
✅ `test_base_datos_inicializar.py` original borrado.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `base_datos/inicializar/` refactorizado.

---

## INTERACCIÓN 2 — Refactorización de base_datos/consultas/

### 🔵 S — Situación

`consultas.py` tenía 3 funciones públicas y 1 privada. Era el quinto módulo
de `base_datos/` en refactorizarse.

### 🔴 P — Problema

Al convertirlo en carpeta, `menu.py`, `bucle.py` y `test_cobertura_completa.py`
perdieron sus imports. Los monkeypatches de los tests también necesitaban
apuntar a la ruta específica de cada función.

### 🟠 E — Exploración

**Prompt enviado:**

> *"listo"*

### 🟢 C — Cambios

`src/base_datos/consultas.py` → `src/base_datos/consultas/`:

| Archivo nuevo | Contenido |
|---|---|
| `construir_consulta_aleatoria.py` | Función privada `_construir_consulta_aleatoria()` |
| `obtener_palabra_aleatoria.py` | Función pública `obtener_palabra_aleatoria()` |
| `obtener_todas_las_palabras.py` | Función pública `obtener_todas_las_palabras()` |
| `obtener_categorias.py` | Función pública `obtener_categorias()` |

Tests refactorizados en `tests/base_datos/consultas/`:

| Archivo nuevo | Contenido |
|---|---|
| `test_obtener_palabra_aleatoria.py` | 7 tests |
| `test_obtener_todas_las_palabras.py` | 5 tests |
| `test_obtener_categorias.py` | 4 tests |

**Monkeypatches actualizados en `test_cobertura_completa.py`:**

| Test | Ruta anterior | Ruta corregida |
|---|---|---|
| `test_obtener_palabra_aleatoria_error_bd` | `src.base_datos.consultas.obtener_conexion` | `src.base_datos.consultas.obtener_palabra_aleatoria.obtener_conexion` |
| `test_obtener_todas_error_bd` | `src.base_datos.consultas.obtener_conexion` | `src.base_datos.consultas.obtener_todas_las_palabras.obtener_conexion` |
| `test_obtener_categorias_error_bd` | `src.base_datos.consultas.obtener_conexion` | `src.base_datos.consultas.obtener_categorias.obtener_conexion` |

### 🔵 A — Acuerdo

✅ 4 archivos de código + 3 de tests.  
✅ `test_base_datos_consultas.py` original borrado.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `base_datos/consultas/` refactorizado.

---

## INTERACCIÓN 3 — Refactorización de base_datos/insercion/

### 🔵 S — Situación

`insercion.py` tenía 2 funciones públicas y 1 privada. Se refactorizó en
paralelo con `consultas/` porque `test_cobertura_completa.py` ya asumía
la nueva estructura al actualizar sus imports.

### 🔴 P — Problema

`test_cobertura_completa.py` ya tenía imports de la nueva ruta pero
`insercion.py` todavía era un archivo, causando `ModuleNotFoundError`.

### 🟠 E — Exploración

**Prompt enviado:**

> *"ya tengo todo para la opcion b"*

### 🟢 C — Cambios

`src/base_datos/insercion.py` → `src/base_datos/insercion/`:

| Archivo nuevo | Contenido |
|---|---|
| `normalizar_dificultad.py` | Función privada `_normalizar_dificultad()` |
| `insertar_palabra.py` | Función pública `insertar_palabra()` |
| `palabra_ya_existe.py` | Función pública `palabra_ya_existe()` |

Tests refactorizados en `tests/base_datos/insercion/`:

| Archivo nuevo | Contenido |
|---|---|
| `test_insertar_palabra.py` | 7 tests |
| `test_palabra_ya_existe.py` | 5 tests |

**Monkeypatches actualizados:**

| Test | Ruta corregida |
|---|---|
| `test_insertar_palabra_error_bd` | `src.base_datos.insercion.insertar_palabra.obtener_conexion` |
| `test_palabra_ya_existe_error_bd` | `src.base_datos.insercion.palabra_ya_existe.obtener_conexion` |

### 🔵 A — Acuerdo

✅ 3 archivos de código + 2 de tests.  
✅ `test_base_datos_insercion.py` original borrado.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `base_datos/insercion/` refactorizado.

---

## INTERACCIÓN 4 — Refactorización de interfaz/dibujo/

### 🔵 S — Situación

`dibujo.py` tenía 2 constantes: `MAXIMO_FALLOS` y `ESTADOS`. Era el módulo
más simple de `interfaz/` pero el más crítico porque `MAXIMO_FALLOS` es
importado por `logica/`, `pantalla/` y los tests.

### 🔴 P — Problema

Al separar `MAXIMO_FALLOS` en su propio archivo, todos los módulos que lo
importaban desde `src.interfaz.dibujo` dejaron de funcionar. Afectó a
`hay_derrota.py`, `intentos_restantes.py`, `pantalla.py` y 3 archivos de tests.

### 🟠 E — Exploración

**Prompt enviado (con dibujo.py personalizado):**

El alumno subió su versión de `dibujo.py` con mensajes propios en la rama
del árbol en cada estado. La IA los mantuvo exactamente igual.

### 🟢 C — Cambios

`src/interfaz/dibujo.py` → `src/interfaz/dibujo/`:

| Archivo nuevo | Contenido |
|---|---|
| `maximo_fallos.py` | Constante `MAXIMO_FALLOS = 6` |
| `estados.py` | Constante `ESTADOS` con los 7 estados ASCII personalizados |

No hay tests para este módulo — solo constantes sin lógica.

**Imports actualizados:**

| Archivo | Import corregido |
|---|---|
| `pantalla.py` | `from src.interfaz.dibujo.estados import ESTADOS` + `from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS` |
| `hay_derrota.py` | `from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS` |
| `intentos_restantes.py` | `from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS` |
| `test_hay_derrota.py` | `from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS` |
| `test_intentos_restantes.py` | `from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS` |
| `test_partida_terminada.py` | `from src.interfaz.dibujo.maximo_fallos import MAXIMO_FALLOS` |

### 🔵 A — Acuerdo

✅ 2 archivos de código.  
✅ Mensajes personalizados del alumno en la rama conservados exactamente.  
✅ Sin tests para constantes puras.

### 🟢 R — Resultado

Todos los tests pasan. Módulo `interfaz/dibujo/` refactorizado.

---

## Catálogo de archivos refactorizados — Fase 8

### `src/base_datos/inicializar/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `palabras_iniciales.py` | `PALABRAS_INICIALES` | constante |
| `crear_tabla_palabras.py` | `_crear_tabla_palabras()` | privada |
| `poblar_palabras_iniciales.py` | `_poblar_palabras_iniciales()` | privada |
| `inicializar_base_datos.py` | `inicializar_base_datos()` | pública |

---

### `src/base_datos/consultas/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `construir_consulta_aleatoria.py` | `_construir_consulta_aleatoria()` | privada |
| `obtener_palabra_aleatoria.py` | `obtener_palabra_aleatoria()` | pública |
| `obtener_todas_las_palabras.py` | `obtener_todas_las_palabras()` | pública |
| `obtener_categorias.py` | `obtener_categorias()` | pública |

---

### `src/base_datos/insercion/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `normalizar_dificultad.py` | `_normalizar_dificultad()` | privada |
| `insertar_palabra.py` | `insertar_palabra()` | pública |
| `palabra_ya_existe.py` | `palabra_ya_existe()` | pública |

---

### `src/interfaz/dibujo/`

| Archivo | Función/Clase | Tipo |
|---|---|---|
| `maximo_fallos.py` | `MAXIMO_FALLOS` | constante |
| `estados.py` | `ESTADOS` | constante |

---

## Pendiente de refactorizar

| Módulo | Estado |
|---|---|
| `src/interfaz/pantalla/` | ⏳ Próximo |
| `src/juego/bucle/` | ⏳ Próximo |
| `src/interfaz/menu/` | ⏳ Próximo |

---

## Resumen de decisiones — Fase 8

| Elemento | Decisión |
|---|---|
| Mensajes personalizados en `dibujo.py` | ✅ Conservados exactamente |
| Monkeypatches tras refactorizar | ✅ Actualizados a ruta específica por función |
| Tests sin lógica (`dibujo/`) | ✅ No se crean tests para constantes puras |
| Orden de refactorización | ✅ Se mantuvo de adentro hacia afuera |
| `insercion/` adelantado | ✅ Se refactorizó antes de `pantalla/` por dependencia de imports |