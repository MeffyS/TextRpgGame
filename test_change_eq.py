from enum import Enum
from game_character import player_backpack
from game_character import player_equipment
from game_character import player


class ChangeEqOptions(Enum):
    INVENTORY = "1"
    EQUIPMENT = "2"
    CHANGE = "3"
    QUIT = "Q"


class PlayerChangeEquipment:

    used_items_by_player = player_equipment.equipment.items()

    item_name_list = [
        item_name for item in player_backpack.inventory for item_name, _ in item.items()
    ]

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
        while True:
            type_of_item = input("Any type of items you want change ")
            if type_of_item in PlayerChangeEquipment.item_name_list:
                for item in player_backpack.inventory:
                    for item_name, item_attribute in item.items():
                        if type_of_item == item_name:
                            one_type_item_list.append(item)
                for number, item in enumerate(one_type_item_list):
                    print(number, item)
                enter_item_number = input("Enter item number which you want change ")
                try:
                    if type_of_item in [item for item in player_equipment.equipment]:
                        if item in one_type_item_list:
                            (
                                player_equipment.equipment[type_of_item],
                                one_type_item_list[int(enter_item_number)][
                                    type_of_item
                                ],
                            ) = (
                                one_type_item_list[int(enter_item_number)][
                                    type_of_item
                                ],
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
                if type_of_item in ["q", "Q"]:
                    break
                else:
                    print(
                        f"{type_of_item.upper()!r} item is not available in inventory"
                    )

    def player_change_eq_options(self):
        while True:
            try:
                for option in ChangeEqOptions:
                    print(f"Click [{option.value}] to {option.name}")
                equipment_choice = input("Please choose option ").upper()
                if (
                    equipment_choice == ChangeEqOptions.INVENTORY.name
                    or equipment_choice == ChangeEqOptions.INVENTORY.value
                ):
                    PlayerChangeEquipment.inventory_items()
                elif (
                    equipment_choice == ChangeEqOptions.EQUIPMENT.name
                    or equipment_choice == ChangeEqOptions.EQUIPMENT.value
                ):
                    PlayerChangeEquipment.equipment_items()
                elif (
                    equipment_choice == ChangeEqOptions.CHANGE.name
                    or equipment_choice == ChangeEqOptions.CHANGE.value
                ):
                    PlayerChangeEquipment.change_of_items(self)

                elif (
                    equipment_choice == ChangeEqOptions.QUIT.name
                    or equipment_choice == ChangeEqOptions.QUIT.value
                ):
                    break
            except ValueError:
                print("You cannot enter a letters except [Q]")

    def main_equipment(self):
        summed_attributes_values = {}
        if player_equipment.equipment == {}:
            pass
            # print("Actually you dont have a items")
            # print(summed_attributes_values)
        else:
            for _, item_list in PlayerChangeEquipment.used_items_by_player:
                for (
                    item,
                    count,
                ) in item_list:
                    if item in summed_attributes_values:
                        summed_attributes_values[item] += count
                        continue
                    else:
                        summed_attributes_values[item] = count
            try:
                player.max_attack += summed_attributes_values["Attack"]
                player.defence += summed_attributes_values["Defence"]
                player.max_health += summed_attributes_values["Health"]
                player.max_mana += summed_attributes_values["Mana"]
                player.max_stamina += summed_attributes_values["Stamina"]
            except KeyError:
                pass



change_eq = PlayerChangeEquipment()


