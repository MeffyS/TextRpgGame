from enum import Enum, auto

from game_character import player
from game_clear_function import clearConsole


player_items = ["Armor", "Boots"]
player_level = 21
buy_slot = 10


tested_dict = {}


class SpecialChestSlot(Enum):
    COIN_SLOT = ["0", "Coins Slot", 10000, True]
    BLACKSMITH_SLOT = ["1", "Blacksmith Slot", 50000, True]
    QUEST_SLOT = ["2", "Quest Slot", 30000, True]
    DUNGEON_SLOT = ["3", "Monster Slot", 30000, True]
    POTION_SLOT = ["4", "Potion Slot", 5000, True]
    GEM_SLOT = ["5", "Gem Slot", 100000, True]
    CITY_SLOT = ["6", "City Slot", 10000, True]


class CityChestOption(Enum):
    SLOT = ["0", "Buy Slot"]
    SPECIAL_SLOT = ["1", "Buy Special Slot"]
    PUT_IN_ITEM = ["2", "Put In Item"]
    TAKE_OUT_ITEM = ["3", "Take Out Item"]


class CityChest:
    bool_counter = 0
    free_chest_slot = 5
    bought_chest_slot = 0
    special_slot = {}

    count_chest_slot = free_chest_slot + bought_chest_slot + player.level

    def chest():
        while True:
            for option in CityChestOption:
                print(f"[{option.value[0]}] [{option.value[1]}]")
            chest_option = input("Enter value")
            if chest_option == CityChestOption.SLOT.value[0]:
                CityChest.buy_slot()
            elif chest_option == CityChestOption.SPECIAL_SLOT.value[0]:
                CityChest.buy_special_slot()
            elif chest_option == CityChestOption.PUT_IN_ITEM.value[0]:
                pass

    @classmethod
    def buy_slot(cls):
        print(f"SLOTS: [{cls.count_chest_slot}]")
        print(f"Cost per next slot is {round(player_level*250)}")
        print(player_level)
        # # while True:

    @classmethod
    def buy_special_slot(cls):

        while True:
            for slot in SpecialChestSlot:
                if slot.value[3] is True:
                    print(f"[{slot.value[0]}][{slot.value[1]}] COST:[{slot.value[2]}]")
                else:
                    print(f"[{slot.value[0]}][{slot.value[1]}] COST:[PURCHASED]")

            buy_slot = input(
                "Enter slot value which you want to buy or [Q] to Quit "
            ).upper()
            for slot in SpecialChestSlot:
                if buy_slot == slot.value[0]:
                    if slot.value[3] is True:
                        cls.bool_counter += 1
                        slot.value[3] = False
                        cls.special_slot[slot.value[1]] = []
            if buy_slot == "Q":
                break
            if buy_slot != slot.value[0] and buy_slot not in [
                slot.value[0] for slot in SpecialChestSlot
            ]:
                print("PLEASE ENTER CORRECT NUMBER")

    # def add_item_to_store():
    #     for item_number, item in enumerate(player_items):
    #         print(f"[{item_number}] {item}")

    #     player_chest = [[slot] for slot in range(0, 6 + player_level + buy_slot)]
    #     while True:
    #         if len(player_items) > 0:
    #             choose_item = int(
    #                 input("Please choose number item which you want hide in chest ")
    #             )
    #             if int(choose_item) < len(player_items):
    #                 for _, chest_place in enumerate(player_chest):
    #                     print(chest_place, end='' )
    #                 while True:
    #                     enter_place = input(f" <-- Choose slot on item: ")
    #                     if int(enter_place) < len(player_chest):
    #                         if len(player_chest[int(enter_place)]) < 2:
    #                             player_chest[int(enter_place)].append(
    #                                 player_items[choose_item]
    #                             )
    #                             del player_items[choose_item]
    #                             print(player_items)
    #                             print(player_chest)
    #                             break
    #                         else:
    #                             print("This slot is taken, try choose other")
    #             else:
    #                 break
    #         else:
    #             break


a = CityChest
a.chest()
