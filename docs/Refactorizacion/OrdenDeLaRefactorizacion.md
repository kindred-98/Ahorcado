El orden que seguire es de adentro hacia afuera, empezando por los módulos sin dependencias internas y terminando por los que dependen de todo lo demás.

El orden:

1. validaciones/    ← sin dependencias internas
2. juego/estado/    ← solo dataclasses, sin imports internos
3. juego/logica/    ← depende de estado e interfaz
4. base_datos/conexion/   ← base de todo base_datos
5. base_datos/inicializar/ ← depende de conexion
6. base_datos/consultas/  ← depende de conexion
7. base_datos/insercion/  ← depende de conexion
8. interfaz/dibujo/       ← solo constantes
9. interfaz/pantalla/     ← depende de dibujo
10. juego/bucle/          ← depende de casi todo
11. interfaz/menu/        ← depende de casi todo

El ahorcado.py no lo tocare toca, es el punto de entrada y ya es un archivo mínimo.

Después de cada módulo corremos:

```
pytest tests/ -v
```

Para verificar que nada se rompe antes de seguir con el siguiente.



Tiene todo el sentido, consistencia en todo el proyecto. Si el código se organiza un archivo por función, los tests igual.

tests/
├── __init__.py
├── conftest.py
├── validaciones/
│   ├── __init__.py
│   ├── letra/
│   │   ├── __init__.py
│   │   ├── test_validar_letra.py
│   │   └── test_normalizar_caracter.py
│   └── palabra/
│       ├── __init__.py
│       ├── test_validar_palabra.py
│       ├── test_validar_categoria.py
│       └── test_validar_dificultad.py
├── juego/
│   ├── __init__.py
│   ├── estado/
│   │   ├── __init__.py
│   │   ├── test_crear_estado_inicial.py
│   │   ├── test_construir_palabra_oculta.py
│   │   ├── test_registrar_letra.py
│   │   ├── test_letra_ya_usada.py
│   │   └── test_obtener_letras_usadas.py
│   └── logica/
│       ├── __init__.py
│       ├── test_hay_victoria.py
│       ├── test_hay_derrota.py
│       ├── test_letra_en_palabra.py
│       ├── test_intentos_restantes.py
│       └── test_partida_terminada.py
├── base_datos/
│   ├── __init__.py
│   ├── test_conexion.py
│   ├── inicializar/
│   │   └── ...
│   ├── consultas/
│   │   └── ...
│   └── insercion/
│       └── ...
└── interfaz/
    ├── __init__.py
    └── pantalla/
        └── ...