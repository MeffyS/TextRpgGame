
from game_informations import pocket as game_eq
from game_informations import main_equipment
from game_add_points import player_attributes
from game_map import up_move
from game_character import player_informations
from game_stage_chest_open import chest
from test_pocket import player_pocket

from game_map import moves
from game_character import player
from campfire_rest import explore
from player_menu import character_menu


def main_game_system(move):
    chest.open_chest(move)
    player_pocket.pocket(move)
    player_informations.informations(move)
    game_eq(move)
    player_attributes(move)
    up_move.up_moves(move)
    main_equipment(move)


def game_stystem(self):
    moves.west_east_moves()
    if player.stamina <= 0:
        explore.explore_menu()


