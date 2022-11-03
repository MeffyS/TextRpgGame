from game_character import player_backpack
from enum import Enum
from items import SMP, SHP, SSP, MP, HP, SP, GMP, GHP, GSP


class PotionShop(Enum):
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


class ShopOptions(Enum):
    BUY = "1"
    SELL = "2"
    LOOK = "3"
    QUIT = "Q"


def display_sell_item_list():
    print("ITEMS IN YOUR POTION POCKET")
    for item_number, item in enumerate(player_backpack.potion_pocket.items()):
        print(f"[{item_number}] {item[0]}. Potion count [{item[1]}]")


def display_buy_item_list():
    print("MERCHANT ITEMS")
    for item in PotionShop.__members__.values():
        if (
            item.value[2] in PotionShop.EXIT.value
            or item.value[3] in PotionShop.EXIT.value
        ):
            print(f"ENTER NUMBER: [{item.value[0]}] TO EXIT [{item.value[1]}]")
        else:
            print(
                f"ENTER NUMBER: [{item.value[0]}] TO BUY [{item.value[1]}]. COST ITEM: [{item.value[3]}] COINS. REGENERATION [{item.value[2]}] POINTS"
            )




def new_sell_item(available_item_list, money, inventory):
    display_sell_item_list()
    while True:
        if len(player_backpack.potion_pocket) > 0:
            enter_number = input("Enter a item number which you want sell ")
            try:
                if enter_number == "Q":
                    return money, inventory
                if int(enter_number) < 0:
                    print("Entered value cannot have a negative value")

                if int(enter_number) <= len(player_backpack.potion_pocket) - 1:
                    for item_number, item_name in enumerate(player_backpack.potion_pocket):
                        if int(enter_number) == item_number:
                            for potion in available_item_list.__members__.values():
                                if potion.value[1] == item_name:
                                    while True:
                                        enter_count = input(
                                            f"You entered {potion.value[1]}. How many {potion.value[1]} you want to sell: "
                                        )
                                        if enter_count == "Q":
                                            return money, inventory
                                        if (
                                            int(enter_count) <= int(inventory[item_name])
                                            and int(enter_count) > 0
                                        ):
                                            if not enter_count.isdigit():
                                                print("Entered value must be a just digit")
                                            if enter_count.isdigit():
                                                inventory[item_name] -= int(enter_count)
                                                money += round(potion.value[3] / 2) * int(
                                                    enter_count
                                                )

                                            if inventory[item_name] == 0:
                                                del inventory[item_name]

                                        else:
                                            print(
                                                f"Entered value cannot be higher than {int(inventory[item_name])}"
                                            )
                                        return money, inventory
            except ValueError:
                print("You can only enter [Q] to Quit, or choose number")
        else:
            print('Your pocket is actually empty'.upper())
            return money, inventory


# player_backpack.coins, player_backpack.potion_pocket = new_sell_item(
#     PotionShop, player_backpack.coins, player_backpack.potion_pocket
# )


def new_buy_item(available_item_list, money, inventory):
    display_buy_item_list()
    while True:
        item_number = input("Enter a item number which one you want to buy ")
        for item in available_item_list.__members__.values():
            if item_number in item.value[0]:
                while True:
                    item_count = input(f"How many {item.value[1]!r} you want buy? ")
                    try:
                        if int(item_count) > 0 and money >= item.value[3] * int(
                            item_count
                        ):
                            if item.value[1] not in inventory:
                                inventory[item.value[1]] = int(item_count)
                            else:
                                inventory[item.value[1]] += int(item_count)
                            money -= item.value[3] * int(item_count)
                        elif int(item_count) < 0:
                            print(f"Entered value {item_count!r} cannot be negative")
                        else:
                            print(
                                f"You dont have a money. {money:,}/{(item.value[3] * int(item_count)):,}"
                            )
                    except ValueError:
                        print(
                            f"Entered value {item_count!r} is not correct. Please try enter a number."
                        )
                        continue
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
                        (
                            player_backpack.coins,
                            player_backpack.potion_pocket,
                        ) = new_buy_item(
                            PotionShop,
                            player_backpack.coins,
                            player_backpack.potion_pocket,
                        )
                        # break
                    else:
                        (
                            player_backpack.coins,
                            player_backpack.potion_pocket,
                        ) = new_sell_item(
                            PotionShop,
                            player_backpack.coins,
                            player_backpack.potion_pocket,
                        )
                        # break
                except ValueError:
                    print(f"Entered value must be postive number")

            elif (
                select_option == ShopOptions.LOOK.name
                or select_option == ShopOptions.LOOK.value
            ):
                display_buy_item_list()
            elif (
                select_option == ShopOptions.QUIT.name
                or select_option == ShopOptions.QUIT.value
            ):
                break
            else:
                print(
                    f"You entered incorrect value [{select_option}]. Please try again"
                )


# si = ShopItems()
if __name__ == "__main__":
    pass