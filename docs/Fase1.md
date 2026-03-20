# ⚔️ EL AHORCADO MEDIEVAL
## Documentación de Asistencia IA Dicampus — Método SPECAR

---

## Introducción

Este documento recoge el proceso completo de asistencia con IA para desarrollar
el **Ahorcado Medieval**, desde la idea inicial hasta la arquitectura modular
del proyecto. Se documenta cada interacción siguiendo el método SPECAR:
**Situación, Problema, Exploración, Cambios, Acuerdo y Resultado.**

---

## FASE 1 — Arte ASCII

---

### INTERACCIÓN 1 — Propuesta inicial del arte ASCII

#### 🔵 S — Situación

El ejercicio del Módulo 2 propone un Juego del Ahorcado con arte ASCII estándar
(7 estados, horca clásica). El profesor da libertad para personalizar la
implementación visual. Se dispone del PDF de referencia y una imagen de ejemplo
de una app comercial del juego.

#### 🔴 P — Problema

El arte ASCII genérico no aporta valor diferencial al repositorio de GitHub.
Se necesita una propuesta visual más original que demuestre creatividad dentro
del marco técnico del ejercicio (CLI con Python).

#### 🟠 E — Exploración

**Prompt enviado:**

> *"Quiero un juego en interfaz que salga un árbol y de él guinde una persona
> y que al 6 intento fallado el mecate de donde cuelga sea cortado con un
> disparo de otra persona para al fondo de la imagen."*

**La IA propuso dos caminos:**

- **CLI con arte ASCII** — encaja con el Commit 5 del enunciado.
- **Interfaz gráfica (tkinter / HTML)** — más detalle pero se aleja del ejercicio.

La IA recomendó quedarse en CLI con ASCII.

#### 🟢 C — Cambios

Se pidió personalización sobre la propuesta base:

- Árbol con hojas en vez de horca clásica.
- Figura detallada, no palitos simples.
- Personaje secundario con espada a la derecha.
- Ambiente medieval.
- Escena nocturna con luna y estrellas.

#### 🔵 A — Acuerdo

✅ CLI con ASCII  
✅ Árbol con hojas  
✅ Figura medieval detallada  
✅ Espadachín a la derecha  
✅ Noche con luna y estrellas  
✅ Estado 6 con efecto de corte  

#### 🟢 R — Resultado

Se generó el primer `prueba_ahorcado.py` con los 7 estados y modo de navegación
interactivo (número 0-6, opción `todos` y `salir`). Funcional pero el layout
no correspondía al boceto que se tenía en mente.

---

### INTERACCIÓN 2 — Reposicionamiento de la escena

#### 🔵 S — Situación

Se compartió un boceto dibujado a mano (imagen PNG) mostrando la distribución
deseada. El primer resultado tenía el árbol y la figura mal posicionados.

#### 🔴 P — Problema

- El colgado no estaba en el centro exacto.
- El espadachín aparecía desde el estado 0 en vez del fallo 1.
- El suelo no diferenciaba hierba de tierra.

#### 🟠 E — Exploración

**Prompt enviado:**

> *"El espadachín aparece en el primer fallo. quiero una luna y quiero hierba.
> donde está el ahorcado y tierra donde está el espadachín. Colgado en el
> centro exacto y no tan grande, mediano. Espadachín igual mediano."*

La IA resumió el nuevo layout antes de reescribir para confirmar comprensión.

#### 🟢 C — Cambios

- Árbol a la izquierda con rama larga hacia el centro.
- Figura colgada en el centro exacto, tamaño mediano.
- Espadachín aparece solo a partir del estado 1.
- Suelo con `/\/\` (hierba) bajo el colgado y `. . .` (tierra) bajo el espadachín.

#### 🔵 A — Acuerdo

✅ Reescritura completa de los 7 estados con el nuevo layout.

#### 🟢 R — Resultado

Segunda versión generada. Layout mejorado respecto al boceto. Verificado sin
errores de sintaxis ni warnings.

---

### INTERACCIÓN 3 — Eliminar el espadachín

#### 🔵 S — Situación

Con la segunda versión lista se revisó la escena. Dos personajes resultaban
visualmente cargados y complicaban el ASCII.

#### 🔴 P — Problema

El espadachín añadía complejidad innecesaria. La narrativa más impactante era
que la cuerda se rompiera sola en el 6to fallo.

#### 🟠 E — Exploración

**Prompt enviado:**

> *"MEJOR QUITEMOS AL ESPADACHÍN, HAGÁMOSLO SOLO CON LA PERSONA Y QUE CAIGA
> EN EL 6 FALLO."*

La IA confirmó el nuevo plan antes de proceder.

#### 🟢 C — Cambios

- Eliminación completa del espadachín de todos los estados.
- Estado 6 rediseñado: cuerda rota `~`, efecto `* SNAP! *` con estrellas `✦`.
- Figura en pose de caída libre.

#### 🔵 A — Acuerdo

✅ Reescritura manteniendo árbol, hierba, estrellas y cabecera.  
❌ Espadachín eliminado definitivamente.

#### 🟢 R — Resultado

Tercera versión más limpia y dramática. Sin warnings, sintaxis verificada.

---

### INTERACCIÓN 4 — Eliminar la luna

#### 🔵 S — Situación

La luna ASCII ocupaba 4 líneas en el lado derecho de cada estado, compitiendo
visualmente con el árbol y la figura.

#### 🔴 P — Problema

La luna con `( ' )` y `.' ~~~ '.` quedaba torpe visualmente. El cielo solo
con estrellas es más elegante.

#### 🟠 E — Exploración

**Prompt enviado:**

> *"QUITEMOS LA LUNA."*

La IA identificó que el bloque se repetía en los 6 primeros estados y procedió
a reemplazarlos con `str_replace` individual.

#### 🟢 C — Cambios

- Eliminación del bloque de luna de los 7 estados.
- Líneas reemplazadas por estrellas `✦` y puntos dispersos.
- Se corrigieron warnings de escape convirtiéndolas a raw strings `r"""`.

#### 🔵 A — Acuerdo

✅ Reemplazo quirúrgico estado por estado.  
❌ Luna eliminada definitivamente.

#### 🟢 R — Resultado

Versión final del archivo `prueba_ahorcado.py` aprobada: sin luna, sin
espadachín, sin warnings.

---

### INTERACCIÓN 5 — Árbol más grande y figura separada del tronco

#### 🔵 S — Situación

Al integrar el arte en la arquitectura modular, se revisó visualmente la escena
y no convencía el tamaño del árbol ni la posición de la figura.

#### 🔴 P — Problema

- El árbol era demasiado pequeño para la escena.
- La cabeza de la figura aparecía pegada al tronco del árbol.

#### 🟠 E — Exploración

**Prompt enviado (con boceto anotado):**

> *"Quiero que el árbol sea más grande y que la cabeza no salga pegada al cepe."*

Se compartió una captura del estado 1 con anotaciones en amarillo marcando
dónde debía ir la figura.

#### 🟢 C — Cambios

- Árbol mucho más alto, ocupa casi toda la altura izquierda.
- Rama rediseñada con doble línea para dar volumen.
- Cuerda más larga para separar la figura del tronco.
- Estado 6: mensaje cambiado a `⚔ Muerte por ahorcamiento . . . ⚔`.
- Figura cayendo con pose desparramada (brazos y piernas abiertos).

#### 🔵 A — Acuerdo

✅ Árbol más alto y ancho.  
✅ Cuerda larga, figura centrada y separada.  
✅ Mensaje `Muerte por ahorcamiento`.  
✅ El alumno indicó que realizó cambios propios en el dibujo que no alteran la lógica.

#### 🟢 R — Resultado

Archivo `dibujo.py` generado como módulo independiente en `src/interfaz/`.
Sintaxis verificada, 7 estados confirmados.

---

## FASE 2 — Arquitectura y modularización

---

### INTERACCIÓN 6 — Definición de la arquitectura modular

#### 🔵 S — Situación

El `main.py` original tenía todo junto: estados ASCII, cabecera, limpiar
pantalla, bucle de prueba y menú. El ejercicio iba creciendo y se necesitaba
una estructura profesional antes de continuar.

#### 🔴 P — Problema

Un solo archivo con todas las responsabilidades mezcladas no es mantenible,
no permite commits incrementales limpios y no demuestra buenas prácticas
para el repositorio de GitHub.

#### 🟠 E — Exploración

**Prompt enviado:**

> *"Quiero cambiar todo mi main y mi base de datos y que todo lo que me des
> sea en español, funciones variables todo todo y con buena nomenclatura
> descriptiva. Quiero separar las cosas del main, quiero hacer carpetas y
> archivo para cada función."*

**La IA propuso esta arquitectura:**

```
src/
├── base_datos/
│   ├── __init__.py
│   ├── conexion.py
│   ├── inicializar.py
│   ├── consultas.py
│   └── insercion.py
├── interfaz/
│   ├── __init__.py
│   ├── dibujo.py
│   ├── menu.py
│   └── pantalla.py
├── juego/
│   ├── __init__.py
│   ├── bucle.py
│   ├── estado.py
│   └── logica.py
├── validaciones/
│   ├── __init__.py
│   ├── letra.py
│   └── palabra.py
└── __init__.py
```

#### 🟢 C — Cambios

Se preguntó si los `__init__.py` debían exportar funciones o usar importaciones
explícitas siempre.

**Prompt enviado:**

> *"Explícitas."*

#### 🔵 A — Acuerdo

✅ Arquitectura modular con una responsabilidad por archivo.  
✅ Todo en español: funciones, variables, constantes, docstrings.  
✅ Nomenclatura descriptiva (sin abreviaciones).  
✅ Importaciones siempre explícitas.  
✅ `__init__.py` vacíos, sin reexportaciones.  
❌ `setup_proyecto.py` propuesto por la IA y rechazado por innecesario.

#### 🟢 R — Resultado

Arquitectura creada manualmente en el proyecto. Todos los archivos vacíos
listos para rellenar módulo por módulo.

---

### INTERACCIÓN 7 — Separación del main en módulos

#### 🔵 S — Situación

Con la arquitectura vacía lista, se procedió a dividir el contenido del
`main.py` existente en sus módulos correspondientes.

#### 🔴 P — Problema

El `main.py` contenía en un solo archivo: los 7 estados ASCII, la cabecera,
la función de limpiar pantalla, `mostrar_estado()` y el bucle de prueba.

#### 🟠 E — Exploración

**Distribución acordada antes de generar:**

| Contenido del main.py | Destino |
|---|---|
| Los 7 estados ASCII + `MAXIMO_FALLOS` | `interfaz/dibujo.py` |
| `CABECERA`, `limpiar_pantalla()`, `mostrar_estado()` | `interfaz/pantalla.py` |
| Bucle de prueba / menú | `interfaz/menu.py` |
| `main()` | `ahorcado.py` |

#### 🟢 C — Cambios

Respecto al `main.py` original se añadió:

- `MAXIMO_FALLOS = 6` como constante nombrada.
- Tipado completo en todas las funciones.
- Docstrings en español en cada función.
- `mostrar_mensaje()` y `mostrar_error()` como funciones independientes.
- Funciones privadas con prefijo `_` para uso interno del módulo.
- `ValueError` en `mostrar_escena()` si `numero_fallos` está fuera de rango.
- `TODO` comments en las acciones del menú pendientes de implementar.

#### 🔵 A — Acuerdo

✅ Todo aceptado.  
✅ El alumno confirmó que realizó cambios propios en `dibujo.py` que no
   alteran la lógica del resto de módulos.

#### 🟢 R — Resultado

Cuatro archivos generados, verificados y listos:

- `src/interfaz/dibujo.py`
- `src/interfaz/pantalla.py`
- `src/interfaz/menu.py`
- `ahorcado.py`

---

## Catálogo de funciones generadas

### `src/interfaz/dibujo.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `ESTADOS` | `list[str]` | Lista con los 7 estados ASCII de la escena medieval |
| `MAXIMO_FALLOS` | `int` | Constante con el máximo de fallos permitidos (6) |

---

### `src/interfaz/pantalla.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `limpiar_pantalla()` | pública | Limpia la terminal (Windows y Unix) |
| `construir_cabecera()` | pública | Construye el recuadro con palabra oculta y letras usadas |
| `mostrar_escena()` | pública | Renderiza cabecera + estado ASCII completo |
| `mostrar_mensaje()` | pública | Imprime un mensaje informativo |
| `mostrar_error()` | pública | Imprime un mensaje de advertencia con `⚠` |
| `_formatear_letras_usadas()` | privada | Convierte lista de letras en cadena legible |
| `_construir_etiqueta_fallos()` | privada | Construye la línea de estado con fallos actuales |

---

### `src/interfaz/menu.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `ejecutar_menu_principal()` | pública | Bucle completo del menú hasta que el jugador sale |
| `mostrar_menu_principal()` | pública | Renderiza las opciones del menú en pantalla |
| `pedir_opcion_menu()` | pública | Captura y valida la opción elegida por el jugador |
| `_accion_jugar()` | privada | Acción: iniciar partida (pendiente de `juego/bucle.py`) |
| `_accion_añadir_palabra()` | privada | Acción: añadir palabra (pendiente de `base_datos/insercion.py`) |
| `_accion_ver_palabras()` | privada | Acción: listar palabras (pendiente de `base_datos/consultas.py`) |
| `_accion_salir()` | privada | Acción: despedida y cierre del programa |
| `_construir_menu()` | privada | Construye el bloque visual del menú |

---

### `ahorcado.py`

| Nombre | Tipo | Descripción |
|---|---|---|
| `main()` | pública | Punto de entrada: inicializa BD y lanza el menú |

---

### `src/base_datos/` *(versión previa, pendiente de separar en módulos)*

| Nombre | Tipo | Descripción |
|---|---|---|
| `_obtener_conexion()` | privada | Abre y devuelve la conexión SQLite |
| `inicializar_base_datos()` | pública | Crea la tabla y puebla las palabras iniciales |
| `obtener_palabra_aleatoria()` | pública | Devuelve una palabra aleatoria con filtros opcionales |
| `obtener_todas_las_palabras()` | pública | Lista todas las palabras ordenadas por categoría |
| `obtener_categorias()` | pública | Lista categorías únicas con conteo de palabras |
| `insertar_palabra()` | pública | Inserta una nueva palabra en la BD |

> ⚠️ Este módulo será separado en `conexion.py`, `inicializar.py`,
> `consultas.py` e `insercion.py` en el siguiente commit.

---

## Resumen de decisiones

| Elemento | Propuesto | Decisión |
|---|---|---|
| Plataforma | CLI o interfaz gráfica | ✅ CLI con ASCII |
| Árbol | Horca clásica | ✅ Árbol con hojas grande |
| Figura | Palitos simples | ✅ Figura medieval detallada |
| Espadachín | Con disparo al estado 6 | ❌ Eliminado |
| Estado 6 | Corte por espadachín | ✅ Cuerda rota sola + SNAP! |
| Mensaje estado 6 | HAS SIDO DERROTADO | ✅ Muerte por ahorcamiento |
| Luna | Luna grande ASCII | ❌ Eliminada |
| Suelo | Línea uniforme | ✅ Hierba + tierra diferenciada |
| Nomenclatura | Sin especificar | ✅ Todo en español descriptivo |
| Importaciones | Libres | ✅ Siempre explícitas |
| `__init__.py` | Con reexportaciones | ❌ Vacíos |
| `setup_proyecto.py` | Propuesto por la IA | ❌ Rechazado por innecesario |
| Arquitectura | Todo en un archivo | ✅ Un archivo por responsabilidad |

---

## Archivos generados hasta ahora

| Archivo | Ruta | Estado |
|---|---|---|
| `dibujo.py` | `src/interfaz/dibujo.py` | ✅ Listo |
| `pantalla.py` | `src/interfaz/pantalla.py` | ✅ Listo |
| `menu.py` | `src/interfaz/menu.py` | ✅ Listo |
| `ahorcado.py` | `ahorcado.py` | ✅ Listo |
| `base_datos.py` | `src/base_datos/` | 🔄 Pendiente de separar |
| `conexion.py` | `src/base_datos/conexion.py` | ⏳ Próximo |
| `inicializar.py` | `src/base_datos/inicializar.py` | ⏳ Próximo |
| `consultas.py` | `src/base_datos/consultas.py` | ⏳ Próximo |
| `insercion.py` | `src/base_datos/insercion.py` | ⏳ Próximo |
| `estado.py` | `src/juego/estado.py` | ⏳ Pendiente |
| `logica.py` | `src/juego/logica.py` | ⏳ Pendiente |
| `bucle.py` | `src/juego/bucle.py` | ⏳ Pendiente |
| `letra.py` | `src/validaciones/letra.py` | ⏳ Pendiente |
| `palabra.py` | `src/validaciones/palabra.py` | ⏳ Pendiente |