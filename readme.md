# Talana Kombat

## Descripción

Este modelo de lenguaje se llama ChatGPT.

## Funcionalidades

### Bienvenidos a la arena!

- Endpoint: /
- Método: GET
- Tags: ["¡Bienvenidos a la arena!"]
Retorna una breve descripción del juego.

### Que comience la lucha!

- Endpoint: /lucha
- Método: POST
- Tags: ["¡Que comience la lucha!"]
Retorna la narración de la pelea entre los dos jugadores.

Los botones que se usan son:

- **(W)Arriba**
- **(S)Abajo**
- **(A)Izquierda**
- **(D)Derecha**
- **(P)Puño**
- **(K)Patada**

Parte atacando el jugador que envió una combinación menor de botones **(movimiento + golpes)**, en caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, si hay empate de nuevo, inicia el player 1 (total el player 2 siempre es del hermano chico)

La secuencia completa del combate de cada jugador se entrega de una vez **(consolidada en un json)**.
Cada personaje tiene 6 Puntos de energía.

- Un personaje muere cuando su energía llega a 0 y de inmediato finaliza la pelea.
- Tony es el player 1, siempre ataca hacia la derecha **(y no cambia de lado)**.
- Arnaldor es el player 2, siempre ataca hacia la izquierda **(y no cambia de lado)**.
- Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es derrotado, los golpes no pueden ser bloqueados, se asume que siempre son efectivos.

## Instalación Local

1. Clona el repositorio.
    `git clone https://github.com/TuUsuario/TuRepositorio.git`
2. Entra a la carpeta.
    `cd TuRepositorio`
3. Instala las dependencias.
    `pip install -r requirements.txt`
4. Ejecuta la aplicación.
    `uvicorn main:app --reload`
5. Abre la aplicación y su documentación.
    `http://localhost:8000/docs` 


## Requerimientos
- `fastapi==0.70.0`
- `pydantic==1.8.2`
- `starlette==0.14.2`
- `uvicorn==0.20.0`

## Estructura de carpetas
[.
├── api
│   ├── routers
│   │   └── kombat_route.py
│   └── serializers
│       └── player_serializer.py
├── core
│   ├── entities
│   │   └── player_entities.py
│   └── process
│       ├── constants.py
│       └── kombat_game.py
├── main.py
├── Dockerfile
├── requirements.txt
└── .dockerignore]