
from game_informations import informations as game_info
from game_informations import pocket as game_eq
from game_informations import main_equipment
from game_add_points import player_stats
from game_merchant import Merchant
from game_moves import Down_Moves
from game_character import player_informations
from campfire_rest import ExploreChoice
from test_game_stage_chest_open import chest
from test_pocket import player_pocket


def main_game_system(move):
    chest.open_chest(move)
    player_pocket.pocket(move)
    player_informations.informations()
    game_eq(move)
    player_stats(move)
    Down_Moves(move)
    main_equipment(move)