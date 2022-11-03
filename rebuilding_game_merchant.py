from game_character import player_backpack
from enum import Enum
from items import SMP, SHP, SSP, MP, HP, SP, GMP, GHP, GSP

shop_items = {
    "SmallManaPotion": 50,
    "SmallHealthPotion": 100,
    "SmallStaminaPotion": 150,
}


class ShopItems(Enum):
    SMALL_MANA_POTION = ["1", "Small Mana Potion", SMP.mana, SMP.price]
    SMALL_HEALTH_POTION = ["2", "Small Health Potion", SHP.health, SHP.price]
    SMALL_STAMINA_POTION = ["3", "Small Stamina Potion", SSP.stamine, SSP.price]
    MANA_POTION = ["4", "Mana Potion", MP.mana, MP.price]
    HEALTH_POTION = ["5", "Health Potion", HP.health, HP.price]
    STAMINA_POTION = ["6", "Stamina Potion", SP.stamine, SP.price]
    GREAT_MANA_POTION = ["7", "Great Mana Potion", GMP.mana, GMP.price]
    GREAT_HEALTH_POTION = ["8", "Great Health Potion", GHP.health, GHP.price]
    GREAT_STAMINA_POTION = ["9", "Great Stamina Potion", GSP.stamine, GSP.price]
    EXIT = ["Q", "Quit", "X", "X"]


# while True:
#     item_number = input("Enter a item number which one you want to buy ")
#     for item in ShopItems.__members__.values():
#         if item_number in item.value[0]:
#             item_count = input(f'How many {item.value[1]!r} you want buy? ')
#     break


class ShopOptions(Enum):
    BUY = "1"
    SELL = "2"
    LOOK = "3"
    QUIT = "Q"


def display_item_list():
    print("MERCHANT ITEMS")
    for item in ShopItems.__members__.values():
        if (
            item.value[2] in ShopItems.EXIT.value
            or item.value[3] in ShopItems.EXIT.value
        ):
            print(f"ENTER NUMBER: [{item.value[0]}] TO EXIT [{item.value[1]}]")
        else:
            print(
                f"ENTER NUMBER: [{item.value[0]}] TO BUY [{item.value[1]}]. COST ITEM: [{item.value[3]}] COINS. REGENERATION [{item.value[2]}] POINTS"
            )


print(player_backpack.coins)


def new_buy_item(available_item_list, money, inventory):
    display_item_list()
    while True:
        item_number = input("Enter a item number which one you want to buy ")
        for item in available_item_list.__members__.values():
            if item_number in item.value[0]:
                item_count = input(f"How many {item.value[1]!r} you want buy? ")
                if int(item_count) > 0 and money >= item.value[3] * int(item_count):
                    if item.value[1] not in inventory:
                        inventory[item.value[1]] = int(item_count)
                    else:
                        inventory[item.value[1]] += int(item_count)
                    money -= item.value[3] * int(item_count)
                else:
                    print(
                        f"You dont have a money. {money:,}/{(item.value[3] * int(item_count)):,}"
                    )
                return int(money), inventory


player_backpack.coins, player_backpack.potion_pocket = new_buy_item(
    ShopItems, player_backpack.coins, player_backpack.potion_pocket
)
print(player_backpack.coins)


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
    @staticmethod
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
                        player_backpack.coins, player_backpack.potion_pocket = buy_item(
                            ShopItems,
                            player_backpack.coins,
                            player_backpack.potion_pocket,
                        )
                        break
                    else:
                        (
                            player_backpack.coins,
                            player_backpack.potion_pocket,
                        ) = sell_item(
                            shop_items,
                            player_backpack.coins,
                            player_backpack.potion_pocket,
                        )
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
                print(
                    f"You entered incorrect value [{select_option}]. Please try again"
                )


m = Merchant()
# m.merchant()

# si = ShopItems()
