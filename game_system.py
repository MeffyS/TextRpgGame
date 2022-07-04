from game_informations import informations as game_info
from game_informations import pocket as game_eq
from game_informations import main_equipment
from opcja_otwierania_skrzyni import chest_opening as game_chest_open
from game_add_points import player_stats
from game_merchant import Merchant
from game_moves import Down_Moves
from game_character import player_informations


def main_game_system(move):
    player_informations.informations()
    game_eq(move)
    game_chest_open(move)
    player_stats(move)
    Down_Moves(move)
    main_equipment(move)