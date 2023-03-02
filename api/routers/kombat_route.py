from starlette.responses import JSONResponse
from fastapi import APIRouter
from api.serializers.player_serializer import FightSerializer
from core.process.kombat_game import fight_process

router = APIRouter()

@router.get("/", tags=["¡Bienvenidos a la arena!"])
async def root():
    """
        `Buenvenidos a Talana Kombat` pulsa try out para ver de que va este juego.
    """
    return JSONResponse(
        content={
            "descripcion ": "Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.",
        }
    )
@router.get("/contacto", tags=["Información de contacto"])
async def root():
    """
        Obtiene la informacion de `creación`, `versión`, y mis datos de contacto.
        """
    return JSONResponse(
        content={
            "autor": "Mario Barrientos",
            "correo": "mariobarrientos0303@gmail.com",
            "linkedin": "https://www.linkedin.com/in/mariobarrientos-developer-python/",
            "github": "https://github.com/mario-barrientos-dev/",
            "documentacion": '"Url local o remota"/docs"',
        }
    )

@router.post("/lucha", tags=["¡Que comience la lucha!"]
)
async def comment_fight(q: FightSerializer):
    """
        Los botones que se usan son 
        `(W)Arriba`, `(S)Abajo`, `(A)Izquierda`, `(D)Derecha`, 
        `(P)Puño`, `(K)Patada` .
        
        Parte atacando el jugador que envió una combinación menor de botones `(movimiento + golpes)`, 
        en caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, 
        si hay empate de nuevo, inicia el player 1 (total el player 2 siempre es del hermano chico) 

        La secuencia completa del combate de cada jugador se entrega de una vez `(consolidada en un json) `
        Cada personaje tiene 6 Puntos de energía 

        • `Un personaje muere` cuando su energía llega a 0 y de inmediato finaliza la pelea\n
        • `Tony es el player 1`, siempre ataca hacia la derecha (y no cambia de lado)\n
        • `Arnaldor es el player 2`, siempre ataca hacia la izquierda (y no cambia de lado)\n
        • `Los personajes se atacan uno a la vez estilo JRPG`, por turnos hasta que uno es 
        derrotado, los golpes no pueden ser bloqueados, se asume que siempre son efectivos. 
    """
    try:
        res = fight_process(q.dict())
        return JSONResponse(
            content={
                "status_code": 200,
                "narration": res,
            }
        )
    except Exception as e:
        return JSONResponse(
            content={
                "status_code": 500,
                "error": str(e),
            }
        )
