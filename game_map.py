import random
from game_character import player
from game_character import player_level_up
from game_character import player_informations
from game_character import player_backpack
from game_draw_chest_key import draw_chest_key_nothing
from gold_chances_variables import draw
from game_clear_function import clearConsole



def game_map_size():
    while True:
        try:
            game_map_size.map = int(input("Enter a map size in range [2-25]"))
            if game_map_size.map < 2 or game_map_size.map > 25:
                print("Incorrect mape size")
            else:
                break
        except ValueError:
            print("Entered value must be a number")


class GameMoves:
    north = 0
    south = 0

    def west_east_moves(self):
        if player.stamina > 0:
            player_level_up.level_up()
            player.experience += 1
            player.stamina -= 1
            draw_chest_key_nothing(draw)

    def north_moves():
        if player.stamina > 0:
            clearConsole()
            player_level_up.level_up()
            GameMoves.north += 1
            GameMoves.south -= 1
            player.experience += 1
            player.stamina -= 1
            draw_chest_key_nothing(draw)
            GameMoves.coordinates()

    def south_moves():
        if player.stamina > 0:
            clearConsole()
            player_level_up.level_up()
            GameMoves.north -= 1
            GameMoves.south += 1
            player.experience += 1
            player.stamina -= 1
            draw_chest_key_nothing(draw)
            GameMoves.coordinates()

    @classmethod
    def up_moves(cls, move):
        while True:
            if move == "U":
                if player_backpack.coins > player_informations.game_floor * 1000:
                    up_floor = input(
                        f"Do you want unlock up floor for {player_informations.game_floor * 1000} coins.[Y][Q] "
                    )
                    if up_floor == "Y":
                        player_backpack.coins -= player_informations.game_floor * 1000
                        player_informations.game_floor += 1
                        GameMoves.north = 0
                        GameMoves.south = 0
                        break
                    elif up_floor == "Q":
                        break
                    else:
                        print("Entered value is not correct")
                else:
                    print(
                        f"You dont have a coins {player_backpack.coins}/{player_informations.game_floor * 1000} to move on upper floor"
                    )
                    break
            break

    def coordinates():
        print(
            f"NORTH: [ {GameMoves.north} ] || FLOOR:{player_informations.game_floor}:FLOOR || [ {GameMoves.south} ] :SOUTH"
        )


up_move = GameMoves()
moves = GameMoves()

