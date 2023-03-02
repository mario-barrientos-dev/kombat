import random

from core.process.constants import NARRATION
from core.entities.player_entities import Player


def fight_process(data: dict) -> list:
    """
    Función que procesa una pelea entre dos jugadores según sus datos de entrada. Retorna una lista
    de cadenas de texto que describe la pelea en tiempo real.

    Args:
    - `data (dict)`: Un diccionario que contiene la información de ambos jugadores.

    Returns:
    - `narración (list)`: Una lista de cadenas de texto que describe la pelea en tiempo real.

    Raises:
    - `HTTPException 500`: Si ocurre un error al procesar la pelea.

    `Ejemplo de uso:`
    - `data` = {"player_1": {"name": "Jugador 1", "energy": 5, "hits": ["K", "P", "", "P", "K"], "movements": ["SD", "ASA", "", "DSD", "SA"]}, "player_2": {"name": "Jugador 2", "energy": 5, "hits": ["K", "P", "", "P", "K"], "movements": ["SD", "ASA", "", "DSD", "SA"]}}
    - `narracion` = fight_process(data)

    """
    try:
        player_1 = Player(
            player_number=1,
            **data["player_1"]
        )
        player_2 = Player(
            player_number=2,
            **data["player_2"]
        )

        sum_of_hits_and_movs = [
            sum([len(h) for h in player_1.hits]) + sum(
                [len(m) for m in player_1.movements]),
            sum([len(h) for h in player_2.hits]) + sum(
                [len(m) for m in player_2.movements]),
        ]

        start = 2 if sum_of_hits_and_movs[0] > sum_of_hits_and_movs[
            1] else 1
        if sum_of_hits_and_movs[0] == sum_of_hits_and_movs[1]:
            start = 2 if len(player_1.movements) > len(
                player_2.movements) else 1
            if len(player_1.movements) == len(player_2.movements):
                start = 2 if len(player_1.hits) > len(player_2.hits) else 1
                if len(player_1.hits) == len(player_2.hits):
                    start = 1

        narration = []
        turn = 0
        player = 0
        while player_1.energy > 0 and player_2.energy > 0 and turn < 5:
            p1, p2, action, mov = (
                player_1,
                player_2,
                player_1.hits[turn],
                player_1.movements[turn],
            ) if start == 1 else (
                player_2,
                player_1,
                player_2.hits[turn],
                player_2.movements[turn]
            )
            if action == "K":
                if mov[-2:].find("SD") != -1:
                    narration.append(
                        random.choice(NARRATION["hit"]["remuyuken"]).format(
                            player_1=p1.name,
                            player_2=p2.name
                        ))
                    p2.energy -= 2
                elif mov[-2:].find("SA") != -1:
                    narration.append(
                        random.choice(NARRATION["hit"]["remuyuken"]).format(
                            player_1=p1.name,
                            player_2=p2.name
                        ))
                    p2.energy -= 3
                else:
                    narration.append(
                        random.choice(NARRATION["hit"]["K"]).format(
                            player_1=p1.name,
                            player_2=p2.name
                        ))
                    p2.energy -= 1
            elif action == "P":
                if mov[-3:].find("DSD") != -1:
                    narration.append(
                        random.choice(NARRATION["hit"]["taladoken"]).format(
                            player_1=p1.name,
                            player_2=p2.name
                        ))
                    p2.energy -= 3
                elif mov[-3:].find("ASA") != -1:
                    narration.append(
                        random.choice(NARRATION["hit"]["taladoken"]).format(
                            player_1=p1.name,
                            player_2=p2.name
                        ))
                    p2.energy -= 2

                else:
                    narration.append(
                        random.choice(NARRATION["hit"]["P"]).format(
                            player_1=p1.name,
                            player_2=p2.name
                        ))
                    p2.energy -= 1

            elif action == "":
                narration.append(random.choice(NARRATION["movement"]).format(
                    player=p1.name))
            player += 1
            start = 2 if start == 1 else 1
            if player % 2 == 0:
                turn += 1
        narration.append(random.choice(NARRATION["win"]).format(
            player_1=player_1.name if player_1.energy > 0 else player_2.name,
            player_2=player_2.name if player_2.energy > 0 else player_1.name,
            energy=player_1.energy if player_1.energy > 0 else player_2.energy
        ))
        return narration

    except Exception as e:
        return {
            "status_code": 500,
            "error": str(e)
        }
