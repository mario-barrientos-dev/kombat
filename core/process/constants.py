NARRATION = {
    # Narración de movimientos generales
    "movement": [
        "{player} avanza",
        "{player} se mueve",
    ],
    # Narración de golpes y movimientos especiales
    "hit": {
        "K": [
            "{player_1} lanza una patada a {player_2}",
            "{player_1} avanza y lanza una patada a {player_2}",
            "{player_1} conecta una patada a {player_2}",
            "{player_1} lanza una patada golpeando a {player_2}",
        ],
        "P": [
            "{player_1} lanza un golpe a {player_2}",
            "{player_1} avanza y lanza un golpe a {player_2}",
            "{player_1} conecta un golpe a {player_2}",
            "{player_1} le da un puño golpeando a {player_2}",
        ],
        "taladoken": [
            "{player_1} conecta un Taladoken a {player_2}",
        ],
        "remuyuken": [
            "{player_1} conecta un Remuyuken a {player_2}",
        ],
    },
    # Narración de victoria
    "win": [
        "{player_1} gana la pelea y aun le queda {energy} de energía",
    ]
}

"""
La variable NARRATION es un diccionario que contiene las diferentes narraciones utilizadas en el proceso de pelea.\n
Estas narraciones se dividen en tres categorías: movimientos generales, golpes y victorias.\n

Los movimientos generales incluyen frases que describen los movimientos de los jugadores durante la pelea,\n
mientras que los golpes y movimientos especiales incluyen frases específicas para cada tipo de golpe. Estas frases \n
están organizadas por tipo de golpe y contienen placeholders para los nombres de los jugadores.

Finalmente, la categoría de victorias incluye frases para narrar el momento en que un jugador gana la pelea. Cada narración\n
también incluye un placeholder para la energía restante del jugador ganador después de la pelea.
"""