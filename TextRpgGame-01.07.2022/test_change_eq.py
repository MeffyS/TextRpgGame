from enum import Enum, auto
from game_character import player_backpack
from game_character import player_equipment


class ChangeEqOptions(Enum):
    INVENTORY = auto()
    EQUIPMENT = auto()
    CHANGE = auto()
    QUIT = "Q"


class PlayerChangeEquipment:

    item_name_list = [
        item_name
        for item in player_backpack.inventory
        for item_name, item_attribute in item.items()
    ]
    print(item_name_list)

    @staticmethod
    def inventory_items():
        for number, inventory_item in enumerate(player_backpack.inventory):
            print(f"{number},{inventory_item}")

    @staticmethod
    def equipment_items():
        for number, (equipment_item, attributes) in enumerate(
            player_equipment.equipment.items()
        ):
            print(number, (equipment_item, attributes))

    def change_of_items(self):
        print(list(set(PlayerChangeEquipment.item_name_list)))
        one_type_item_list = []
        type_of_item = input("Any type of items you want change ")
        if type_of_item in PlayerChangeEquipment.item_name_list:
            for item in player_backpack.inventory:
                for item_name, item_attribute in item.items():
                    if type_of_item == item_name:
                        one_type_item_list.append(item)
            for number, item in enumerate(one_type_item_list):
                print(number, item)
            enter_item_number = input("Enter item number which you want change")
            try:
                if type_of_item in [item for item in player_equipment.equipment]:
                    if item in one_type_item_list:
                        (
                            player_equipment.equipment[type_of_item],
                            one_type_item_list[int(enter_item_number)][type_of_item],
                        ) = (
                            one_type_item_list[int(enter_item_number)][type_of_item],
                            player_equipment.equipment[type_of_item],
                        )

                else:
                    player_equipment.equipment[type_of_item] = one_type_item_list[
                        int(enter_item_number)
                    ][type_of_item]
                    player_backpack.inventory.pop(int(enter_item_number))
            except IndexError:
                print("You entered incorrect number")
        else:
            print("This item is not available in inventory")

    def player_change_eq_options(self):
        while True:
            try:
                for option in ChangeEqOptions:
                    print(option.value, option.name)
                equipment_choice = input("Please choose option ")
                if (
                    equipment_choice == ChangeEqOptions.INVENTORY.name
                    or int(equipment_choice) == ChangeEqOptions.INVENTORY.value
                ):
                    PlayerChangeEquipment.inventory_items()
                elif (
                    equipment_choice == ChangeEqOptions.EQUIPMENT.name
                    or int(equipment_choice) == ChangeEqOptions.EQUIPMENT.value
                ):
                    PlayerChangeEquipment.equipment_items()
                elif (
                    equipment_choice == ChangeEqOptions.CHANGE.name
                    or int(equipment_choice) == ChangeEqOptions.CHANGE.value
                ):
                    PlayerChangeEquipment.change_of_items(self)
            except ValueError:
                if equipment_choice == "Q":
                    break
                else:
                    print("You cannot enter a letters except [Q]")


p = PlayerChangeEquipment()

