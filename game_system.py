from game_add_points import player_attributes
from game_map import up_move
from test_change_eq import change_eq
from game_stage_chest_open import chest
from test_pocket import player_pocket
from test_change_eq import change_eq

from game_map import moves
from game_character import player
from campfire_rest import explore


def main_game_system(move):
    chest.open_chest(move)
    player_pocket.pocket(move)
    player_attributes(move)
    up_move.up_moves(move)
    change_eq.main_equipment(move)


def game_stystem():
    
    moves.west_east_moves()
    change_eq.main_equipment()
    if player.stamina <= 0:
        explore.explore_menu()

