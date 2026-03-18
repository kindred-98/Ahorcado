# ⚔️ El Ahorcado Medieval

> Juego clásico del ahorcado para terminal, ambientado en la época medieval,
> con base de datos SQLite y arte ASCII nocturno.

---

## 📖 Descripción

**El Ahorcado Medieval** es un juego de terminal desarrollado en Python 3.12+
donde el jugador debe adivinar una palabra oculta letra por letra antes de agotar
sus 6 intentos. La palabra se obtiene de una base de datos SQLite que puede
consultarse y ampliarse en cualquier momento.

La escena visual está ambientada en una noche medieval: un árbol con hojas del
que cuelga una figura, que cae al suelo si se agotan los intentos.

---

## 🎮 Características

- Arte ASCII medieval con 7 estados progresivos (0-6 fallos)
- Base de datos SQLite con palabras por categoría y dificultad
- Filtrado de palabras por categoría antes de jugar
- Añadir nuevas palabras desde el propio juego
- Validación robusta de entradas
- Menú principal interactivo

---

## 🗂️ Estructura del proyecto

```
ahorcado/
│
├── README.md               # Este archivo
├── .gitignore              # Archivos ignorados por Git
├── requirements.txt        # Dependencias del proyecto
│
├── src/
│   ├── ahorcado.py         # Lógica principal del juego
│   ├── base_datos.py       # Conexión y operaciones SQLite
│   ├── validaciones.py     # Validación de entradas del usuario
│   └── dibujo.py           # Arte ASCII del ahorcado (7 estados)
│
├── data/
│   └── palabras.db         # Base de datos SQLite (generada automáticamente)
│
└── docs/
    └── asistencia_ia.md    # Documentación del proceso con IA (método SPECAR)
```

---

## 🚀 Instalación y uso

### Requisitos

- Python 3.12 o superior
- No requiere dependencias externas (`sqlite3` viene incluido con Python)

### Clonar el repositorio

```bash
git clone https://github.com/kindred-98/Ahorcado.git
cd ahorcado-medieval
```

### Ejecutar el juego

```bash
python src/ahorcado.py
```

---

## 🕹️ Cómo jugar

1. Ejecuta el juego con el comando anterior.
2. En el menú principal elige **Jugar**.
3. Selecciona una categoría de palabras (opcional).
4. Adivina letras una por una antes de agotar los 6 intentos.
5. Si fallas 6 veces, la cuerda se rompe y la figura cae. ¡Suerte, caballero!

---

## 🗄️ Base de datos

La base de datos `data/palabras.db` se crea automáticamente al iniciar el juego
por primera vez. Contiene una tabla `palabras` con los campos:

| Campo       | Tipo    | Descripción                        |
|-------------|---------|------------------------------------|
| id          | INTEGER | Clave primaria autoincremental     |
| palabra     | TEXT    | La palabra en minúsculas           |
| categoria   | TEXT    | Categoría temática                 |
| dificultad  | TEXT    | Nivel: facil / medio / dificil     |

---

## 📚 Tecnologías

| Tecnología | Uso                        |
|------------|----------------------------|
| Python 3.12+ | Lenguaje principal        |
| sqlite3    | Base de datos embebida     |
| Git        | Control de versiones       |

---

## 📝 Documentación IA

El proceso de desarrollo asistido por IA está documentado en
[`docs/asistencia_ia.md`](docs/asistencia_ia.md) siguiendo el método **SPECAR**.

---

## 👤 Autor

Desarrollado como ejercicio práctico del **Estrategias de Generación de Código con IA** · Dicampus