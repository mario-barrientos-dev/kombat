# Talana Kombat

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

## Instalación Docker

Para ejecutar este Dockerfile y ver la aplicación funcionar, sigue estos pasos:

1. Asegúrate de tener Docker instalado en tu máquina. Si no lo tienes, descárgalo e instálalo desde la página oficial de Docker.

2. Descarga los archivos de la aplicación, incluyendo el Dockerfile, y colócalos en una carpeta.

3. Abre una terminal o línea de comandos en la carpeta donde se encuentran los archivos de la aplicación.

4. Ejecuta el siguiente comando para construir la imagen de Docker a partir del Dockerfile:
   
   `docker build -t talana-kombat .` 

    Esto creará una nueva imagen de Docker con el nombre "mi-aplicacion" y las dependencias necesarias instaladas.

5. Una vez que se haya construido la imagen, puedes ejecutar la aplicación con el siguiente comando:

    `docker run -p 8000:8000 talana-kombat`

    Esto iniciará un contenedor de Docker y expondrá el puerto 8000 de la aplicación en el puerto 8000 de tu máquina host. Puedes acceder a la aplicación abriendo un navegador web y visitando la dirección [http://localhost:8000]. 

6. Si deseas detener la aplicación, puedes presionar Ctrl+C en la terminal donde se está ejecutando el contenedor. 
    También puedes detener el contenedor con el siguiente comando:

    `docker stop <nombre_del_contenedor_o_ID>`

    Asegúrate de reemplazar <nombre_del_contenedor_o_ID> con el nombre o ID del contenedor que deseas detener.

Con estos pasos, podrás ejecutar este Dockerfile y ver la aplicación funcionar en tu máquina. Si necesitas personalizar la aplicación o la imagen de Docker, asegúrate de editar los archivos correspondientes y volver a construir la imagen con el comando **docker build**.


## Instalación Local

1. Clona el repositorio.
    `https://github.com/mario-barrientos-dev/talana-kombat.git`
2. Entra a la carpeta.
    `cd talana-kombat`
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
`.
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
└── .dockerignore`
