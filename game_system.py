from test_change_eq import change_eq
from game_map import moves
from game_character import player
from campfire_rest import explore


def game_stystem():
    
    moves.west_east_moves()
    change_eq.main_equipment()
    if player.stamina <= 0:
        explore.explore_menu()

