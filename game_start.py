from enum import Enum
from test_game_informations import game_informations
from game_moves import game_start
import sys


class GameOptions(Enum):
    Start = ["1", "start"]
    About = ["2", "about"]
    Leave = ["3", "leave"]


for option in GameOptions:
    print(f"Click {option.value[0]} to [{option.name}]")

while True:
    choose_option = input("Start[1], About[2], Leave[3] ")
    if choose_option == GameOptions.Start.value[0] and GameOptions.Start.value[1]:
        game_start.game_moves(choose_option)

    elif choose_option == GameOptions.About.value[0] and GameOptions.About.value[1]:
        game_informations()
    elif choose_option == GameOptions.Leave.value[0] and GameOptions.Leave.value[1]:
        sys.exit()
