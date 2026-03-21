# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA — Método SPECAR
## FASE 5 — Validaciones
> Módulo 2 · Estrategias de Generación de Código con IA · Dicampus

---

## Introducción

Este documento recoge el proceso de asistencia con IA para implementar
los módulos `letra.py` y `palabra.py` de la carpeta `src/validaciones/`.
Estos dos módulos se encargan de validar toda entrada del usuario antes
de procesarla, tanto durante el juego como al añadir nuevas palabras
a la base de datos.

---

## INTERACCIÓN 1 — Implementación de letra.py y palabra.py

### 🔵 S — Situación

Con `juego/bucle.py` implementado se detectó que importaba `validar_letra`
de `src.validaciones.letra` que aún no existía. Además, las acciones de
añadir palabras en `menu.py` necesitarán validar la palabra, categoría
y dificultad antes de insertarlas en la BD.

### 🔴 P — Problema

Sin validaciones el juego acepta cualquier entrada del usuario: números,
símbolos, cadenas vacías o letras repetidas. Esto puede romper la lógica
del juego o insertar datos corruptos en la base de datos.

### 🟠 E — Exploración

**Prompt enviado:**

> *"si dame las validaciones"*

La IA propuso generar los dos archivos a la vez ya que son independientes
entre sí y tienen el mismo patrón: reciben una cadena, devuelven `None`
si es válida o un mensaje de error descriptivo si no lo es.

### 🟢 C — Cambios

**En `letra.py`:**
- `ALFABETO_ESPAÑOL` definido como `frozenset` para búsquedas O(1).
- La función devuelve `None` si es válida o un `str` con el error,
  en vez de lanzar excepciones, para que `bucle.py` pueda mostrar
  el mensaje directamente al jugador.
- `_normalizar_caracter()` añadida como utilidad privada para eliminar
  tildes en comparaciones cuando sea necesario.

**En `palabra.py`:**
- `CATEGORIAS_VALIDAS` y `DIFICULTADES_VALIDAS` definidas como `frozenset`
  para que sean inmutables y con búsquedas eficientes.
- `LONGITUD_MINIMA_PALABRA = 3` y `LONGITUD_MAXIMA_PALABRA = 30` como
  constantes nombradas para facilitar cambios futuros.
- `_buscar_caracter_invalido()` extraída como función privada para no
  mezclar la lógica de búsqueda con la función principal.
- Mensajes de error descriptivos que incluyen el carácter inválido
  encontrado y la lista de opciones válidas.

### 🔵 A — Acuerdo

✅ Patrón de retorno `str | None` en todas las funciones de validación.  
✅ `frozenset` para conjuntos de valores válidos (inmutable y eficiente).  
✅ Constantes nombradas para longitudes mínima y máxima.  
✅ Mensajes de error descriptivos con el valor inválido incluido.  
✅ Funciones privadas para lógica interna de cada módulo.  

### 🟢 R — Resultado

Dos archivos generados y verificados:

- `src/validaciones/letra.py`
- `src/validaciones/palabra.py`

---

## Catálogo de funciones — Fase 5

### `src/validaciones/letra.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `validar_letra()` | pública | Valida que la entrada sea una sola letra del alfabeto español |
| `_normalizar_caracter()` | privada | Elimina tildes de un carácter para comparaciones internas |

---

### `src/validaciones/palabra.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `validar_palabra()` | pública | Valida longitud mínima, máxima y que solo contenga letras |
| `validar_categoria()` | pública | Verifica que la categoría sea una de las 4 permitidas |
| `validar_dificultad()` | pública | Verifica que la dificultad sea `facil`, `medio` o `dificil` |
| `_buscar_caracter_invalido()` | privada | Devuelve el primer carácter inválido encontrado en la palabra |

---

## Resumen de decisiones — Fase 5

| Elemento | Propuesto | Decisión |
|---|---|---|
| Retorno de validaciones | Excepción o booleano | ✅ `str \| None` — mensaje directo o sin error |
| Conjuntos de valores válidos | Lista o tuple | ✅ `frozenset` (inmutable y O(1)) |
| Longitudes | Hardcodeadas | ✅ Constantes nombradas `LONGITUD_MINIMA_PALABRA` y `LONGITUD_MAXIMA_PALABRA` |
| Mensajes de error | Genéricos | ✅ Descriptivos con el valor inválido incluido |
| Lógica de búsqueda | Inline en la función | ✅ Extraída a función privada `_buscar_caracter_invalido()` |