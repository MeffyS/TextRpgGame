from game_informations import GameAttributes
import random
import math
from enum import Enum
import gold_chances_variables
from game_character import player
from game_character import player_level_up
from game_clear_function import clearConsole
from test_game_stage_chest_open import OpenChest


def draw_coins_count(value):
    minimal_coins_count = (value - 0.9) * (GameAttributes.Floor)
    maximal_coins_count = (value + 100) * (GameAttributes.Floor)
    return random.randint(math.ceil(minimal_coins_count), math.ceil(maximal_coins_count))


def chests_opening():

    while len(GameAttributes.player_chests) >= 0:
        chests_sort = sorted( GameAttributes.player_chests.items(), key=lambda x: x[1], reverse=True)
        chests_count = []
        [chests_count.extend([chest,count]) for chest, count in chests_sort]
            
        opened_count = []
        [opened_count.extend([chest, count]) for chest, count in GameAttributes.opened_chests.items()]
        if len(GameAttributes.player_chests) > 0:
            # clearConsole()    
            print(100*'=')
            print(f'Chests: {chests_count}')
            print(100*'=')
            print(f'Opened Chests: {opened_count}')
            print(100*'=')
            
            chest_color = input(
                "Enter a chest color to open it. Click [Q] to leave ")
            
            if chest_color == "Q":
                # clearConsole()
                break

            elif chest_color not in GameAttributes.player_chests:
                print(f"You dont have {chest_color} chest")

            else:
                player_level_up.level_up()
                GameAttributes.player_chests[chest_color] -= 1
                add_coins = draw_coins_count(
                    gold_chances_variables.chance_on_coins[gold_chances_variables.coins_in_chest[f'{chest_color}']])
                GameAttributes.Coins += add_coins
                print(f'{add_coins} coins has been added to ur pocket')
                player.experience = player.experience + \
                    (math.ceil(add_coins * 0.2))
                

                # print('To you purse has beed added', add_coins, 'Coins')

                if chest_color not in GameAttributes.opened_chests:
                    GameAttributes.opened_chests[chest_color] = 1

                elif chest_color in GameAttributes.opened_chests:
                    GameAttributes.opened_chests[chest_color] = GameAttributes.opened_chests[chest_color] + 1

                if GameAttributes.player_chests[chest_color] == 0:
                    GameAttributes.player_chests.pop(chest_color)
        elif len(GameAttributes.player_chests) == 0:
            print(100*'=')
            print(f'You have a 0 chest to open')
            print(100*'=')
            print(f'Opened Chests: {opened_count}')
            print(100*'=')
            break