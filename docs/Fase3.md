# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA Dicampus — Método SPECAR

## FASE 3 — Base de datos modular

---

### INTERACCIÓN 8 — Separación de base_datos en módulos

#### 🔵 S — Situación

El archivo `base_datos.py` original tenía todas las operaciones juntas:
conexión, creación de tabla, consultas e inserciones.

#### 🔴 P — Problema

Seguía el mismo problema de la fase anterior: múltiples responsabilidades
en un solo archivo. La conexión, la inicialización, las consultas y las
inserciones son responsabilidades distintas que deben vivir separadas.

#### 🟠 E — Exploración

**Prompt enviado:**

> *"Claro sigamos, comenzemos."*

La IA propuso separar en 4 archivos siguiendo el principio de responsabilidad
única, en este orden de implementación porque `conexion.py` es la base de todos:

| Archivo | Responsabilidad |
|---|---|
| `conexion.py` | Solo abrir la conexión SQLite |
| `inicializar.py` | Crear tabla y poblar palabras |
| `consultas.py` | Todas las operaciones SELECT |
| `insercion.py` | Todas las operaciones INSERT |

Durante la implementación se debatió si usar **tuplas o diccionarios** para
`PALABRAS_INICIALES`. La IA explicó que las tuplas son la opción correcta
porque `executemany()` las acepta nativamente, los datos son fijos y son
más ligeras en memoria. Los diccionarios se reservan para los resultados
de las consultas.

#### 🟢 C — Cambios

- `_construir_consulta_aleatoria()` extraída como función privada en
  `consultas.py` para no mezclar construcción SQL con ejecución.
- `palabra_ya_existe()` añadida en `insercion.py` para verificar
  duplicados antes de insertar desde la interfaz.
- `_normalizar_dificultad()` añadida como validación interna en `insercion.py`.

#### 🔵 A — Acuerdo

✅ Cuatro archivos con responsabilidad única.  
✅ Tuplas para datos fijos de inicialización.  
✅ Diccionarios para resultados de consultas (`dict(fila)`).  
✅ Funciones privadas para lógica interna de cada módulo.  

#### 🟢 R — Resultado

Cuatro archivos generados y verificados:

- `src/base_datos/conexion.py`
- `src/base_datos/inicializar.py`
- `src/base_datos/consultas.py`
- `src/base_datos/insercion.py`

---

### INTERACCIÓN 9 — Corrección de imports (ModuleNotFoundError)

#### 🔵 S — Situación

Al ejecutar `python ahorcado.py` desde la raíz del proyecto apareció el error:

```
ModuleNotFoundError: No module named 'base_datos'
```

#### 🔴 P — Problema

`ahorcado.py` está en la raíz y los módulos dentro de `src/`. Los imports
internos usaban rutas sin prefijo como `from base_datos.conexion` que Python
no puede resolver cuando el punto de entrada está fuera de `src/`.

#### 🟠 E — Exploración

La IA propuso dos soluciones:

- Corregir todos los imports añadiendo el prefijo `src.`
- Usar `python -m ahorcado`

Se intentó `python -m ahorcado` pero el error persistía porque los imports
internos entre módulos de `src/` tampoco tenían el prefijo `src.`.

#### 🟢 C — Cambios

Se corrigieron los imports en todos los archivos afectados:

| Archivo | Import anterior | Import corregido |
|---|---|---|
| `ahorcado.py` | `from base_datos.inicializar` | `from src.base_datos.inicializar` |
| `ahorcado.py` | `from interfaz.menu` | `from src.interfaz.menu` |
| `inicializar.py` | `from base_datos.conexion` | `from src.base_datos.conexion` |
| `consultas.py` | `from base_datos.conexion` | `from src.base_datos.conexion` |
| `insercion.py` | `from base_datos.conexion` | `from src.base_datos.conexion` |
| `pantalla.py` | `from interfaz.dibujo` | `from src.interfaz.dibujo` |
| `menu.py` | `from interfaz.pantalla` | `from src.interfaz.pantalla` |

#### 🔵 A — Acuerdo

✅ Prefijo `src.` en todos los imports del proyecto.  
✅ `__init__.py` vacíos en todas las carpetas de `src/`.  
✅ Ejecución con `python ahorcado.py` desde la raíz.

#### 🟢 R — Resultado

El proyecto arranca correctamente. Menú principal funcional. Las opciones
de jugar, añadir palabra y ver palabras muestran placeholders `TODO` hasta
que se implemente `juego/`.

---

## Catálogo de funciones generadas

---

### `src/base_datos/conexion.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `obtener_conexion()` | pública | Abre y devuelve la conexión SQLite con `row_factory` configurado |

---

### `src/base_datos/inicializar.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `inicializar_base_datos()` | pública | Crea la tabla y puebla las 20 palabras iniciales |
| `_crear_tabla_palabras()` | privada | Ejecuta el `CREATE TABLE IF NOT EXISTS` |
| `_poblar_palabras_iniciales()` | privada | Ejecuta el `INSERT OR IGNORE` de las palabras iniciales |

---

### `src/base_datos/consultas.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `obtener_palabra_aleatoria()` | pública | Devuelve una palabra aleatoria con filtros opcionales |
| `obtener_todas_las_palabras()` | pública | Lista todas las palabras ordenadas por categoría |
| `obtener_categorias()` | pública | Lista categorías únicas con conteo de palabras |
| `_construir_consulta_aleatoria()` | privada | Construye el SQL dinámico con filtros opcionales |

---

### `src/base_datos/insercion.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `insertar_palabra()` | pública | Inserta una palabra nueva normalizando a minúsculas |
| `palabra_ya_existe()` | pública | Comprueba si una palabra ya existe en la BD |
| `_normalizar_dificultad()` | privada | Valida y normaliza el valor de dificultad |

---

### `src/juego/` *(pendiente de implementar — Fase 4)*

| Nombre | Módulo | Descripción |
|---|---|---|
| `EstadoPartida` | `estado.py` | Dataclass con la palabra, fallos y letras usadas |
| `construir_palabra_oculta()` | `estado.py` | Genera la cadena con guiones y letras reveladas |
| `verificar_letra()` | `logica.py` | Comprueba si la letra está en la palabra |
| `hay_victoria()` | `logica.py` | Detecta si todas las letras han sido adivinadas |
| `hay_derrota()` | `logica.py` | Detecta si se alcanzó el máximo de fallos |
| `iniciar_partida()` | `bucle.py` | Bucle principal de una partida completa |

> ⚠️ Estos módulos se implementarán en la siguiente fase.

---


## Resumen de decisiones

| Elemento | Propuesto | Decisión |
|---|---|---|
| Datos iniciales BD | Diccionarios | ✅ Tuplas (nativas de `executemany`) |
| Resultados de consultas | Sin especificar | ✅ Diccionarios (`dict(fila)`) |

---

## Estado de archivos

| Archivo | Ruta | Estado |
|---|---|---|
| `dibujo.py` | `src/interfaz/dibujo.py` | ✅ Listo |
| `pantalla.py` | `src/interfaz/pantalla.py` | ✅ Listo |
| `menu.py` | `src/interfaz/menu.py` | ✅ Listo |
| `ahorcado.py` | `ahorcado.py` | ✅ Listo |
| `conexion.py` | `src/base_datos/conexion.py` | ✅ Listo |
| `inicializar.py` | `src/base_datos/inicializar.py` | ✅ Listo |
| `consultas.py` | `src/base_datos/consultas.py` | ✅ Listo |
| `insercion.py` | `src/base_datos/insercion.py` | ✅ Listo |
| `estado.py` | `src/juego/estado.py` | ⏳ Próximo |
| `logica.py` | `src/juego/logica.py` | ⏳ Próximo |
| `bucle.py` | `src/juego/bucle.py` | ⏳ Próximo |
| `letra.py` | `src/validaciones/letra.py` | ⏳ Próximo |
| `palabra.py` | `src/validaciones/palabra.py` | ⏳ Próximo |


