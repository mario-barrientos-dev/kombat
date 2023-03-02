from typing import List


class Player:
    def __init__(self, player_number: int, movements: List[str], hits: List[str]) -> None:
        """
        Constructor de la clase Player, que representa a un jugador de la pelea.

        Args:
        - player_number (int): Número que identifica al jugador.
        - movements (List[str]): Lista de movimientos que puede realizar el jugador.
        - hits (List[str]): Lista de golpes que puede realizar el jugador.

        Returns: None.
        """
        self.name = "Tonyn" if player_number == 1 else "Arnaldor"
        self.energy = 6
        self.movements = movements
        self.hits = hits

    def to_json(self) -> dict:
        """
        Método que convierte la instancia de la clase Player en un diccionario JSON.

        Args: None.

        Returns:
        - dict: Diccionario JSON que representa la instancia de la clase Player.
        """
        return {
            "name": self.name,
            "energy": self.energy,
            "movements": self.movements,
            "hits": self.hits
        }
