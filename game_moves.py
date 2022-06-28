import random

from game_informations import GameAttributes, direction_move
from game_character import player
from game_character import player_level_up
from game_draw_chest_key import draw_chest_key_nothing as game_draw
import gold_chances_variables
from game_clear_function import clearConsole

draw = random.choices(
    gold_chances_variables.chance_key, gold_chances_variables.chance_value)[0]


def North_Moves():

    if player.getStamina() > 0:
        clearConsole()
        player_level_up.level_up()

        print(f'{100*"="}'.center(100))
        GameAttributes.N = GameAttributes.N + 1
        GameAttributes.S = GameAttributes.S - 1
        GameAttributes.Moves = GameAttributes.Moves + 1
        player.experience = player.experience + 1
        player.stamina = player.getStamina() - 1
        game_draw(draw)
        direction_move()
    elif player.getStamina() <= 0:
        player.stamina = 0
        print("Your character is exhausted, you can't move.")


def South_Moves():

    if player.getStamina() > 0:
        clearConsole()
        player_level_up.level_up()

        print(f'{100*"="}'.center(100))
        GameAttributes.N = GameAttributes.N - 1
        GameAttributes.S = GameAttributes.S + 1
        GameAttributes.Moves = GameAttributes.Moves + 1
        player.experience = player.experience + 1
        player.stamina = player.getStamina() - 1
        game_draw(draw)
        direction_move()
    elif player.getStamina() <= 0:
        player.stamina = 0
        print("Your character is exhausted, you can't move.")


def Down_Moves(move):

    if move == "U":
        print(
            f"Cost to unlock next up floor: {GameAttributes.Floor * 1000} coins")
        if GameAttributes.Coins >= GameAttributes.Floor * 1000:
            do_u_want_unlock = input(
                f"Do you want unlock next up floor? Y/N. Cost to unlock next up floor: {GameAttributes.Floor * 1000} coins ").upper()
            if do_u_want_unlock == 'T':
                GameAttributes.Coins = GameAttributes.Coins - GameAttributes.Floor * 1000
                GameAttributes.Floor = GameAttributes.Floor + 1
                GameAttributes.N = 0
                GameAttributes.S = 0
            else:
                pass
