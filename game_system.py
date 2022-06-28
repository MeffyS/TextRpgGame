from game_informations import informations as game_info
from game_informations import pocket as game_eq
from game_informations import main_equipment
from opcja_otwierania_skrzyni import chest_opening as game_chest_open
from game_add_points import player_stats
from game_shop import merchant
from game_moves import Down_Moves


def main_game_system(move):
    game_info(move)
    game_eq(move)
    game_chest_open(move)
    player_stats(move)
    merchant(move)
    Down_Moves(move)
    main_equipment(move)