from game_informations import informations as game_info
from game_informations import pocket as game_eq
from game_informations import main_equipment
from game_add_points import player_stats
from game_merchant import Merchant
from game_moves import Down_Moves
from game_character import player_informations
from campfire_rest import ExploreChoice


def main_game_system(move):
    player_informations.informations()
    game_eq(move)
    player_stats(move)
    Down_Moves(move)
    main_equipment(move)