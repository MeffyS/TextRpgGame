from enum import Enum, auto

from game_character import player
from game_clear_function import clearConsole



tested_dict = {}


class SpecialChestSlot(Enum):
    COIN_SLOT = ["0", "Coins Slot", 10000, True]
    BLACKSMITH_SLOT = ["1", "Blacksmith Slot", 50000, True]
    QUEST_SLOT = ["2", "Quest Slot", 30000, True]
    DUNGEON_SLOT = ["3", "Monster Slot", 30000, True]
    POTION_SLOT = ["4", "Potion Slot", 5000, True]
    GEM_SLOT = ["5", "Gem Slot", 100000, True]
    CITY_SLOT = ["6", "City Slot", 10000, True]


# for x in SpecialChestSlot:
#     print(x.value[0])


class CityChestOption(Enum):
    SLOT = [0, "Buy Slot"]
    SPECIAL_SLOT = [1, "Buy Slot"]
    PUT_IN_ITEM = [2, "Put In Item"]
    TAKE_OUT_ITEM = [3, "Take Out Item"]


class CityChest:
    free_chest_slot = 5
    bought_chest_slot = 0
    special_slot = {}

    count_chest_slot = free_chest_slot + bought_chest_slot + player.level

    def buy_special_slot():
        print("--------------------------------")
        for slot in SpecialChestSlot.__members__.values():
            print(slot.value[1], slot.value[3])
        print("--------------------------------")
        while True:
            buy_slot = input("Enter slot value which you want to buy")

            for slot in SpecialChestSlot.__members__.values():
                if buy_slot == slot.value[0]:
                    if slot.value[3] is True:
                        slot.value[3] = False

                    for slot1 in SpecialChestSlot.__members__.values():
                        if slot1.value[3] is True:
                            print(slot1.value[0], slot1.value[1])
                        else:
                            print(slot1.value[0], slot1.value[1], "PURCHASED")


CityChest.buy_special_slot()
