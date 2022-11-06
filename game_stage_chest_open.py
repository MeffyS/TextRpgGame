import math
import random

import gold_chances_variables as chance_on_gold
from game_character import player
from game_character import player_informations
from game_character import player_backpack
from game_character import player_level_up


class OpenChest:
    agree = "Y"
    disagree = "Q"

    def drawing_coins(self, coins):
        minimal_coins = (coins - (coins / 10)) * (player_informations.game_floor)
        maximal_coins = (
            coins + random.randint(100, 200)
        ) * player_informations.game_floor

        return random.randint(math.ceil(minimal_coins), math.ceil(maximal_coins))

    @classmethod
    def open_chest(cls, move):
        if move == "CHEST":

            while True:
                explore_chest = input("Do you want open chest? [Y][Q] ").upper()
                if explore_chest == cls.agree:
                    open_chest = OpenChest()
                    open_chest.chest_opening()
                elif explore_chest == cls.disagree:
                    break
                else:
                    print(f"Entered value {explore_chest} is incorrect ")

    def chest_opening(self):
        chest_sort = sorted(
            player_backpack.chests.items(), key=lambda x: x[1], reverse=True
        )
        available_chests = []
        [
            available_chests.extend(
                [chest, count_chest] for chest, count_chest in chest_sort
            )
        ]
        opened_chests = []
        [
            opened_chests.extend([chest_opened, chest_opened_count])
            for chest_opened, chest_opened_count in player_informations.opened_chests.items()
        ]
        if len(player_backpack.chests) > 0:

            while True:
                for color_number, color_value in enumerate(
                    player_backpack.new_chests.items()
                ):
                    print(
                        f"SELECT number [{color_number}] or [{color_value[0]}] to open {color_value[0]} chest. {color_value[0].title()} chest count is {color_value[1]}."
                    )
                chest_color = input(
                    "Enter a color name or number of chest which you want open "
                )
                for color_number, color_value in enumerate(
                    player_backpack.new_chests.items()
                ):
                    if chest_color.isdigit():
                        if int(chest_color) == color_number:

                            player.experience += 1
                            player_backpack.new_chests[color_value[0]] -= 1
                            player_level_up.level_up()

                            inventory_add_coins = self.drawing_coins(
                                chance_on_gold.chance_on_coins[
                                    chance_on_gold.coins_in_chest[f"{color_value[0]}"]
                                ]
                            )
                            player_backpack.coins += inventory_add_coins
                            print(
                                f"To your pocket {inventory_add_coins} coins has been added. You got {player_backpack.coins} coins"
                            )
                            if color_value[0] not in player_informations.opened_chests:
                                player_informations.opened_chests[color_value[0]] = 1
                            elif color_value[0] in player_informations.opened_chests:
                                player_informations.opened_chests[color_value[0]] += 1
                            if player_backpack.new_chests[color_value[0]] == 0:
                                player_backpack.new_chests.pop(color_value[0])
                                break
                            if len(player_backpack.new_chests) == 0:
                                break

                if not chest_color.isdigit():
                    if chest_color in player_backpack.new_chests.keys():

                        player.experience += 1
                        player_backpack.new_chests[chest_color] -= 1
                        player_level_up.level_up()
                        inventory_add_coins = self.drawing_coins(
                            chance_on_gold.chance_on_coins[
                                chance_on_gold.coins_in_chest[f"{color_value[0]}"]
                            ]
                        )
                        player_backpack.coins += inventory_add_coins
                        print(
                            f"To your pocket {inventory_add_coins} coins has been added. You got {player_backpack.coins} coins"
                        )
                        if chest_color not in player_informations.opened_chests:
                            player_informations.opened_chests[chest_color] = 1
                        elif chest_color in player_informations.opened_chests:
                            player_informations.opened_chests[chest_color] += 1
                        if player_backpack.new_chests[chest_color] == 0:
                            player_backpack.new_chests.pop(chest_color)
                        if len(player_backpack.new_chests) == 0:
                            break

                    elif chest_color in ["Q", "q"]:
                        break

                if chest_color == "Q":
                    break




chest = OpenChest()

