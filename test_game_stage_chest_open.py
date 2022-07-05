import math
import random

from game_character import player_informations
from game_character import player_backpack
from game_character import player_level_up
import gold_chances_variables as chance_on_gold

class OpenChest:

    def drawing_coins(self,coins):
        minimal_coins = (coins - (coins/10)) * (player_informations.game_floor)
        maximal_coins = (coins + random.randint(100,200)) * player_informations.game_floor

        return random.randint(math.ceil(minimal_coins), math.ceil(maximal_coins))
     
    def chest_opening(self):
        chest_sort = sorted(player_backpack.chests.items(),key=lambda x: x[1], reverse=True)
        available_chests = []
        [available_chests.extend([chest, count_chest] for chest, count_chest in chest_sort)]
        opened_chests = []
        [opened_chests.extend([chest_opened,chest_opened_count]) for chest_opened, chest_opened_count in player_informations.opened_chests.items() ]
        if len(player_backpack.chests) > 0:
            while True:
                print(f'CHESTS: {player_backpack.chests}')
                print(f'OPENED CHESTS: {player_informations.opened_chests}')
                chest_color = input("Enter a color chest which you want open ")
                
                if chest_color in player_backpack.chests:
                    player_level_up.level_up()
                    player_backpack.chests[chest_color] -= 1
                    inventory_add_coins  = self.drawing_coins(
                        chance_on_gold.chance_on_coins[chance_on_gold.coins_in_chest[f'{chest_color}']]
                    )
                    player_backpack.coins += inventory_add_coins
                    print(f'To your pocket {inventory_add_coins} coins has been added. You got {player_backpack.coins} coins')
                    if chest_color not in player_informations.opened_chests:
                        player_informations.opened_chests[chest_color] = 1
                    elif chest_color in player_informations.opened_chests:
                        player_informations.opened_chests[chest_color] += 1
                    if player_backpack.chests[chest_color] == 0:
                        player_backpack.chests.pop(chest_color)
                    if len(player_backpack.chests) == 0:
                        break
                elif chest_color == "Q":
                    break
                else:
                    print(f"You dont have {chest_color!r} chest")
        else:
            print('You dont have chests top open')
            print(f"Opened Chests: {opened_chests}")

