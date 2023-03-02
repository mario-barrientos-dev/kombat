from enum import Enum
from typing import List

from pydantic import BaseModel, Field, validator
from fastapi import APIRouter

router = APIRouter()

class Movements(str, Enum):
    W = "W"
    A = "A"
    D = "D"
    S = "S"


class Hits(str, Enum):
    K = "K"
    P = "P"


class PlayerSerializer(BaseModel):
    movements: List[str] = Field(
        ...,
        title="Movimientos",
        description="Lista de movimientos que ejecuta un usuario",
        alias="movimientos",
        max_items=5,
        max_length=5
    )
    hits: List[str] = Field(
        ...,
        title="Hits",
        description="Lista de golpes que ejecuta un usuario",
        alias="golpes",
        max_items=5,
        max_length=1
    )

    @validator("movements")
    def validate_movements(cls, v: List[str]) -> List[str]:
        """
        Valida que los movimientos sean válidos.
        """
        if not all(movement in Movements.__members__ for movements in v for movement in movements):
            raise ValueError("Los movimientos no son válidos")
        return v

    @validator("hits")
    def validate_hits(cls, v: List[str]) -> List[str]:
        """
        Valida que los golpes sean válidos.
        """
        if not all(hit in Hits.__members__ for hits in v for hit in hits):
            raise ValueError("Los golpes no son válidos")
        return v


class FightSerializer(BaseModel):
    player_1: PlayerSerializer = Field(
        ...,
        title="Player 1",
        description="Información de los movimientos y golpes ejecutados por el player 1",
        alias="player1",
        example={
            "movimientos": ["D", "DSD", "S", "DSD", "SD"],
            "golpes": ["K", "P", "", "K", "P"]
        },
    )
    player_2: PlayerSerializer = Field(
        ...,
        title="Player 2",
        description="Información de los movimientos y golpes ejecutados por el player 2",
        alias="player2",
        example={
            "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
            "golpes": ["K", "", "K", "P", "P"]
        },
    )
