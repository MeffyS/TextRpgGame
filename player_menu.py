from enum import Enum
from game_character import (
    player_backpack,
    player_equipment,
    player_informations,
    player_statistic,
)
from game_add_points import player_attributes
from game_stage_chest_open import chest
from campfire_rest import explore
from test_change_eq import change_eq
from test_pocket import player_pocket


class CharacterMenuChoice(Enum):
    character_information = [1, "Character Informations"]
    character_statistic = [2, "Character Statistics"]
    character_backpack = [3, "Character Backpack"]
    character_chest = [4, "Character Chests"]
    character_equipment = [5, "Character Equipment"]
    character_inventory = [6, "Character Inventory"]
    character_pocket = [7, "Character Pocket"]
    character_menu_exit = [8, "Menu Exit"]


class CharacterMenu:
    def player_menu(self, menu):
        if menu == "menu":
            print("PLAYER MENU")
            while True:
                for option in CharacterMenuChoice:
                    print(f"{option.value[0]} {option.value[1]}")
                enter_option = input("Enter option")
                if int(enter_option) == CharacterMenuChoice.character_information.value[0]:
                    print(CharacterMenuChoice.character_information.value[1])
                    player_informations.informations()
                elif int(enter_option) == CharacterMenuChoice.character_statistic.value[0]:
                    player_attributes("STATISTIC")
                elif int(enter_option) == CharacterMenuChoice.character_backpack.value[0]:
                    print(f"Coins: {player_backpack.coins:,} ")
                    print(f"City Items: {player_backpack.quest_items}")
                    print(f"Quest Items: {player_backpack.quest_items}")
                    print(f"Blacksmith Items: {player_backpack.blacksmith_items}")
                    print(f"Dungeon Items: {player_backpack.dungeon_items}")
                elif int(enter_option) == CharacterMenuChoice.character_chest.value[0]:
                    chest.chest_opening()
                elif int(enter_option) == CharacterMenuChoice.character_equipment.value[0]:
                    change_eq.player_change_eq_options()
                elif int(enter_option) == CharacterMenuChoice.character_inventory.value[0]:
                    for item in player_backpack.inventory:
                        for name, attribute in item.items():
                            print(name, attribute)
                elif int(enter_option) == CharacterMenuChoice.character_pocket.value[0]:
                    player_pocket.pocket('POCKET')
                elif int(enter_option) == CharacterMenuChoice.character_menu_exit.value[0]:
                    break



                

character_menu = CharacterMenu()
