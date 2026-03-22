<div align="center">

# ⚔️ **AHORCADO MEDIEVAL**
### *Un viaje al patíbulo impulsado por Python, arquitectura limpia y acero templado*

---

## 🛡️ Badges esenciales

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=for-the-badge&logo=pytest)
![Architecture](https://img.shields.io/badge/Clean-Architecture-purple?style=for-the-badge)

</div>

---

## 📜 Descripción

**AHORCADO MEDIEVAL** es una reimaginación del clásico juego del ahorcado, ambientado en un reino donde las palabras deciden el destino de los viajeros.  
Este proyecto combina:

- 🧱 **Arquitectura limpia y modular**  
- 🗡️ **Interfaz ASCII temática medieval**  
- 📚 **Base de datos SQLite** para gestionar palabras, categorías y dificultad  
- 🧪 **Testing automatizado con Pytest**  
- 🧩 **Separación estricta por capas**: interfaz, lógica, estado, validaciones y base de datos  

Es un proyecto diseñado como **ejercicio de ingeniería de software**, con un enfoque profesional y documentado.

---

## 🎬 Demo

> Las imágenes deben colocarse en la carpeta `IMG/`.

| Menú principal | Estado del ahorcado |
|---|---|
| ![menu](IMG/menu.png) | ![estado](IMG/estado.png) |

| Partida en curso |
|---|
| ![partida](IMG/partida.png) |

---

## ⚔️ Características principales

| Funcionalidad | Descripción | Estado |
|---|---|:---:|
| Interfaz ASCII medieval | Escenas del ahorcado y estética temática | ✅ |
| Base de datos SQLite | Palabras, categorías y dificultad | ✅ |
| Añadir palabras | Desde el menú principal | ✅ |
| Ver palabras | Listado completo desde la BD | ✅ |
| Juego completo | Turnos, fallos, letras usadas, victoria/derrota | ✅ |
| Validaciones | Letras, palabras, categorías y dificultad | ✅ |
| Testing | Cobertura amplia por módulos | ✅ |
| Arquitectura limpia | Separación estricta por capas | ✅ |

---

## 🗺️ Arquitectura del Reino (diagrama temático)
```
┌───────────────────────────────┐
│        REINO DE PYTHON        │
└───────────────────────────────┘
│
▼
┌────────────────────────────────────────────────────────────────┐
│                        MAPA DEL AHORCADO                       │
└────────────────────────────────────────────────────────────────┘

┌──────────────────────────┐        ┌────────────────────────────────────┐
│      ALDEA DEL MENÚ      │◄──────►│     CASTILLO DEL JUEGO             │
│ - Menú principal         │        │ - Bucle de turnos                  │
│ - Pantalla ASCII         │        │ - Estado de partida                │
│ - Escenas del ahorcado   │        │ - Lógica de victoria/derrota       │
└──────────────────────────┘        └────────────────────────────────────┘
│                                      │
▼                                      ▼
┌──────────────────────────┐        ┌────────────────────────────────────┐
│   BOSQUE DE VALIDACIÓN   │        │     CATACUMBAS DEL SABER (BD)      │
│ - Letras                 │        │ - Conexión SQLite                  │
│ - Palabras               │        │ - Consultas                        │
│ - Categorías             │        │ - Inserción                        │
│ - Dificultad             │        │ - Inicialización                   │
└──────────────────────────┘        └────────────────────────────────────┘
```
Código

---

## 📦 Instalación

Clonacion
```bash
git clone https://github.com/kindred-98/Ahorcado
cd Ahorcado
```

Entorno victual
```
python -m venv .venv
.venv\Scripts\activate  # Windows
```

Requriments
```
pip install -r requeriments.txt
```

## ▶️ Uso

```bash
python ahorcado.py
```

## 🗄️ Base de datos

```
Ubicación:
Código
data/palabras.db
```

---

## Estructura:

|Campo | Tipo | Descripción |
|---|:---:|:---:|
| id | INTEGER | Identificador único |
| palabra |	TEXT |	Palabra a adivinar |
| categoria |	TEXT |	Categoría opcional |
| dificultad |	TEXT |	fácil / media / difícil |

---

🧪 Testing
Ejecutar todos los tests:

bash
pytest
Con cobertura:

bash
pytest --cov
📂 Estructura del proyecto (extendida)
Código
Ahorcado/
│
├── ahorcado.py
├── requeriments.txt
├── README.md
│
├── data/
│   └── palabras.db
│
├── docs/
│   ├── Fase1.md
│   ├── Fase2.md
│   ├── ...
│   └── Refactorizacion/
│       ├── Fase7.md
│       └── ...
│
├── src/
│   ├── base_datos/
│   │   ├── conexion/
│   │   ├── consultas/
│   │   ├── inicializar/
│   │   └── insercion/
│   │
│   ├── interfaz/
│   │   ├── dibujo/
│   │   ├── menu/
│   │   └── pantalla/
│   │
│   ├── juego/
│   │   ├── bucle/
│   │   ├── estado/
│   │   └── logica/
│   │
│   └── validaciones/
│       ├── letra/
│       └── palabra/
│
└── tests/
    ├── base_datos/
    ├── interfaz/
    ├── juego/
    └── validaciones/
📜 Changelog profesional
v1.2.0 — 2026-03-22
Añadido README profesional con estilo medieval elegante

Nuevo diagrama temático “Mapa del Reino”

Documentación extendida y reorganizada

v1.1.0 — 2026-03-20
Mejoras en la estructura interna

Refactorización de módulos del juego

Optimización de validaciones

v1.0.0 — 2026-03-15
🎉 Versión inicial

Juego completo funcional

Base de datos SQLite

Interfaz ASCII

Suite de tests Pytest

Arquitectura modular

👑 Autor
<div align="center">

Monkey‑D‑Luffy
Rey de los desarrolladores piratas.
Domador de bugs.
Forjador de arquitecturas limpias.

GitHub

</div>

📜 Licencia
MIT — Libre para usar, modificar y compartir.

Código

---

Ángel, este README **ya está al nivel de un proyecto profesional de portfolio**, con estética medieval elegante y documentación completa.

Si quieres, puedo generar también:

- Un **banner PNG medieval**  
- Un **logo del proyecto**  
- Un **manual de usuario**  
- Un **CHANGELOG automático basado en commits**  

Solo dímelo y seguimos puliendo tu reino.