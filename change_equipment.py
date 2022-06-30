
from game_clear_function import clearConsole
import game_informations
from game_character import player_inventory
from game_character import player_equipment


def changing_equipment():
    clearConsole()
    print(f'{100 * "="}')
    print("Your character is currently wearing")
    print(f'{100 * "="}')
    for items in player_equipment.equipment:
        print(items, player_equipment.equipment[items])
       
    while True:
        item_names = [
            item for item in player_inventory.inventory for item in item]
        eq_names = [
            item for item in player_equipment.equipment]
        print(f'{100 * "="}')    
        print('You wearing', eq_names)    
        print(f'{100 * "="}')
        print(f'Items in inventory{item_names}')
        print(f'{100 * "="}')
        choose_item_name = input("Any list items you want to see")
        clearConsole()
        player_one_type_inventory = []
        print(f'{100 * "="}')
        print('You wearing', eq_names)
        print(f'{100 * "="}')
        print('Items to change', item_names)
        print(f'{100 * "="}')
        for player_inventory_item in player_inventory.inventory:
            for player_inventory_new_item, _ in player_inventory_item.items():
                if choose_item_name == player_inventory_new_item:
                    player_one_type_inventory.append(player_inventory_item)
       
        if choose_item_name == "Q":
            break
        elif choose_item_name not in eq_names and choose_item_name not in item_names and choose_item_name != "Q":
            continue
        elif choose_item_name in eq_names:
            
            while True:
                change_eq = input("Do you wanna change part eq?[Y][Q] ").upper()
                clearConsole()
                if change_eq == "Y":
                    print(f'{100 * "="}')
                    for item_number, item in enumerate(player_one_type_inventory):
                        print(item_number, item)
                    print(f'{100 * "="}')
                    if item in player_one_type_inventory:
                        while True:
                            try:
                                item_value = input("Enter a number")
                                clearConsole()
                                if int(item_value) <= len(player_one_type_inventory) and int(item_value) >= 0:
                                    player_equipment.equipment[choose_item_name], player_one_type_inventory[int(item_value)][choose_item_name] = player_one_type_inventory[int(
                                        item_value)][choose_item_name], player_equipment.equipment[choose_item_name]
                                    print(f'{100 * "="}')    
                                    print(f'{choose_item_name} {player_one_type_inventory[int(item_value)][choose_item_name]} CHANGED TO ➡ {choose_item_name} {player_equipment.equipment[choose_item_name]}')    
                                    break
                                elif item_value == "Q":
                                    break
                                else:
                                    print("Enter a correct number")
                                    continue
                            except IndexError:
                                print("Enter a correct number")
                        break
                    else:
                        print(f'{100 * "="}')
                        print(
                            f"You dont have a {choose_item_name} in ur inventory")
                        print(f'{100 * "="}')    
                        break
                elif change_eq == "Q":
                    break
                elif change_eq != "Q":
                    continue

        elif choose_item_name not in eq_names:
            
            for item_number, item in enumerate(player_one_type_inventory):
                print(item_number, item)
            print(f'{100 * "="}')
            while True:
                try:
                    item_value = input("Enter a number")
                    clearConsole()
                    if item_value.isdigit():
                        for item_num, item in enumerate(player_inventory.inventory):
                            if item == player_one_type_inventory[int(item_value)]:
                                while True:
                                    choose_item = input(
                                        "Do u want add item to ur eq[Y][N]")
                                    clearConsole()
                                    if choose_item == "Y":
                                        player_equipment.equipment[
                                            choose_item_name] = player_one_type_inventory[int(item_value)][choose_item_name]
                                        player_inventory.inventory.pop(
                                            item_num)
                                        print(f'{100 * "="}')    
                                        print(f'{choose_item_name},{player_one_type_inventory[int(item_value)][choose_item_name]} has been added')
                                        
                                        break
                                    elif choose_item == "Q":
                                        break
                                    elif choose_item != "Q":
                                        print("Enter a correct value")
                                    else:
                                        print("Enter a correct value")
                                        continue
                        break
                    else:
                        print("Enter a correct number")
                except IndexError:
                    print("Enter a correct number")
        elif choose_item_name == "Q":
            break

        else:
            print("This item does not belong to your inventory ")
            break
