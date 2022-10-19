from game_character import player_backpack
from enum import Enum, auto

shop_items = {
    "SmallManaPotion": 50,
    "SmallHealthPotion": 100,
    "SmallStaminaPotion": 150,
}


class ShopOptions(Enum):
    BUY = "1"
    SELL = "2"
    LOOK = "3"
    QUIT = "Q"


def display_item_list():
    print("MERCHANT ITEMS")
    for number, (item, price) in enumerate(shop_items.items()):
        print(f"[{number}] {item}:{price}")


def buy_item(available_item_list, money, inventory):
    display_item_list()
    item_name = input(f"Enter item name which you want ")
    item_count = int(input(f"Enter how many items you want "))
    if item_name not in available_item_list:
        print(f"You cannot buy {item_name} becouse is not available in merchant")
    else:
        if item_count > 0 and money >= available_item_list[item_name] * item_count:
            if item_name not in inventory:
                inventory[item_name] = item_count
            else:
                inventory[item_name] += item_count
            money -= available_item_list[item_name] * item_count
        else:
            print(
                f"You dont have a money. {money:,}/{(available_item_list[item_name] * item_count):,}"
            )
    return int(money), inventory


def sell_item(available_item_list, money, inventory):
    display_item_list()
    item_name = input(f"Enter item name which you want ")
    item_count = int(input(f"Enter how many items you want "))
    if item_name not in inventory and item_name not in available_item_list:
        print(f"{item_name} is not available in your inventory and merchant")
    elif item_name not in inventory and item_name in available_item_list:
        print(f"{item_name} is not available in your inventory")
    elif item_name in inventory and item_name not in available_item_list:
        print(f"{item_name} is not on sell")
    else:
        if (
            item_name in inventory
            and item_name in available_item_list
            and item_count > inventory[item_name]
            or item_count < 0
        ):
            print(
                f"[{item_name}] cannot be selling becouse you entered to incorrect count {item_count}"
            )
        else:
            inventory[item_name] -= item_count
            money += (available_item_list[item_name] * item_count) / 2
            if inventory[item_name] == 0:
                del inventory[item_name]

    return int(money), inventory


class Merchant:

    def merchant():
        print("==========MERCHANT==========")
        while True:
            for option in ShopOptions:
                print(f"Enter [{option.value}] to [{option.name}]")
            select_option = input(f"Enter a [BUY|SELL|LOOK|QUIT] or [1,2,3,Q] ").upper()
            if select_option in [
                ShopOptions.BUY.name,
                ShopOptions.SELL.name,
                ShopOptions.BUY.value,
                ShopOptions.SELL.value,
            ]:
                try:
                    if (
                        select_option == ShopOptions.BUY.name
                        or select_option == ShopOptions.BUY.value
                    ):
                        player_backpack.coins, player_backpack.potion_pocket = buy_item(shop_items, player_backpack.coins, player_backpack.potion_pocket)
                        break
                    else:
                        player_backpack.coins, player_backpack.potion_pocket = sell_item(shop_items, player_backpack.coins, player_backpack.potion_pocket)
                        break
                except ValueError:
                    print(f"Entered value must be postive number")

            elif (
                select_option == ShopOptions.LOOK.name
                or select_option == ShopOptions.LOOK.value
            ):
                display_item_list()
            elif (
                select_option == ShopOptions.QUIT.name
                or select_option == ShopOptions.QUIT.value
            ):
                break
            else:
                print(f"You entered incorrect value [{select_option}]. Please try again")


print("INVENTORY", player_backpack.potion_pocket)
print("MONEY", player_backpack.coins)
