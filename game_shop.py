from enum import Enum


from game_informations import GameAttributes
from game_clear_function import clearConsole


class GameShop:
    ManaPotion = "ManaPotion"
    HealthPotion = "HealthPotion"
    StaminaPotion = "StaminaPotion"
    DungeonKey = "DungeonKey"
    Diamond = "Diamond"  # health
    Emerald = "Emerald"  # mana
    Aquamarine = "Aquamarine"  # samine
    Ruby = "Ruby"  # defence
    Sapphire = "Sapphire"  # attack
    Topaz = "Topaz"  # magic
    Pearl = "Pearl"  # lucky

    shop_items = {
        ManaPotion: '50',
        HealthPotion: '100',
        StaminaPotion: '150',
        DungeonKey: '25000',
        Diamond: '2500',
        Emerald: '2500',
        Aquamarine: '2500',
        Sapphire: '2500',
        Topaz: '2500',
        Pearl: '2500',
    }


def look_items():
    clearConsole()
    print(f'{100 * "="}')
    print(f"ITEMS IN SHOP".center(100))
    print(f'{100 * "="}')
    for item, price in GameShop.shop_items.items():
        print(f'{item:30}:{price:10}'.center(100))



def merchant(shop):
    if shop == "SHOP":
        while True:
            print(f'{100 * "="}')
            print(f'Here you can buying,selling,looking[BUY][SELL][LOOK][Q]'.center(100))
            print(f'{100 * "="}')
            sell_buy_look = input(f"".center(50)).upper()
            if sell_buy_look == "BUY":
                clearConsole()
                while True:
                    print(f'{100 * "="}')
                    print(f"ITEMS IN SHOP".center(100))
                    print(f'{100 * "="}')
                    for item, price in GameShop.shop_items.items():
                        print(f'{item:30} {int(price):10,}'.center(100))
                        
                    print(f'{100 * "="}')
                    print(f"Choose item which you want to buy.[Q]".center(100))
                    print(f'{100 * "="}')
                    item_name = input(f"".center(50))
                    clearConsole()
                    if item_name in GameShop.shop_items:
                        while True:
                            print(f'{100 * "="}')
                            print(f"How many {item_name} you want to buy?[COUNT][MAX][Q] ".center(100))
                            print(f'{100 * "="}')
                            item_count = input(f"".center(50))
                            clearConsole()
                            item_price = int(
                                f'{GameShop.shop_items[item_name]}')
                            if item_count.isdigit():
                                if GameAttributes.Coins >= item_price * int(item_count):
                                    while True:
                                        print(f'{100 * "="}')
                                        print(f"Are you sure, that you want to buy {item_name} for {item_price * int(item_count):,} coins?[Y][Q] ".center(100))
                                        print(f'{100 * "="}')
                                        confirm_buy = input(f"".center(50))
                                        if confirm_buy == "Y":
                                            GameAttributes.Coins -= item_price * \
                                                int(item_count)
                                            print(f'{100 * "="}')
                                            print(f'You spent {int(item_price) * int(item_count):,} coins to buy {int(item_count):,} {item_name}. In your pocket you have a {GameAttributes.Coins:,} coins'.center(100).center(100))
                                            print(f'{100 * "="}')

                                            if item_name not in GameAttributes.pocket:
                                                GameAttributes.pocket[f'{item_name}'] = int(
                                                    item_count)
                                                print(GameAttributes.pocket)
                                                break

                                            elif item_name in GameAttributes.pocket:
                                                GameAttributes.pocket[f'{item_name}'] += int(
                                                    item_count)
                                                print(GameAttributes.pocket)
                                                break
                                        elif confirm_buy == "Q":
                                            break
                                        elif confirm_buy != "Q":
                                            continue
                                if GameAttributes.Coins < item_price * int(item_count):
                                    print(
                                        f"You dont have a coins {GameAttributes.Coins:,}/{item_price * int(item_count):,}".center(100))

                            elif item_count == "MAX":
                                clearConsole()
                                while True:
                                    maximal_items = GameAttributes.Coins // int(
                                        GameShop.shop_items[item_name])
                                    print(f'{100 * "="}')
                                    print(f"Are you sure that you want buy {maximal_items:,} {item_name} for {item_price * maximal_items:,} coins?[Y][Q] ".center(100))
                                    print(f'{100 * "="}')
                                    buy_warning = input(f"".center(50)).upper()
                                    if buy_warning == "Y":
                                        clearConsole()
                                        if item_name not in GameAttributes.pocket:
                                            GameAttributes.pocket[f'{item_name}'] = int(maximal_items)

                                            break
                                        else:
                                            GameAttributes.pocket[f'{item_name}'] += int(maximal_items)
                                            GameAttributes.Coins -= item_price * int(maximal_items)
                                            print(
                                                f"You spent {item_price * int(maximal_items):,} to buy {maximal_items:,} {item_name}.".center(100))
                                            print(f'{100 * "="}')
                                            print(
                                                f"Actually you have {GameAttributes.Coins:,} coins in pocket".center(100))
                                    elif buy_warning == "Q":
                                        clearConsole()
                                        break
                                    elif buy_warning != "Q":
                                        clearConsole()
                                        continue
                            elif item_count == "Q":
                                clearConsole()
                                break
                            else:
                                clearConsole()
                                print(f'{100 * "="}')
                                print(f"Enter correct value [COUNT][MAX][Q]".center(100))
                                continue
                    elif item_name not in GameShop.shop_items:
                        print(f'{100 * "="}')
                        print(f"{item_name} is not in the store".center(100))
                    elif item_name == "Q":
                        clearConsole()
                        break

            elif sell_buy_look == "SELL":
                clearConsole()
                while True:
                    print(f'{100 * "="}')
                    print(f"ITEMS IN INVENTORY".center(100))
                    print(f'{100 * "="}')
                    for item, count in GameAttributes.pocket.items():
                        print(f'{item:20}:{count:2}'.center(100))
                    print(f'{100 * "="}')
                    print(f"Which item you want to sell?[LOOK][Q] ".center(100))
                    print(f'{100 * "="}')
                    item_name = input("".center(50))
                    clearConsole()
                    if item_name in GameAttributes.pocket.keys() and item_name in GameShop.shop_items.keys():
                        clearConsole()
                        while True:
                            print(f'{100 * "="}')
                            print(f"How many {item_name} you want to sell?[COUNT][Q] ".center(100))
                            print(f'{100 * "="}')
                            item_count = input(f"".center(50))
                            clearConsole()
                            if item_count.isdigit():
                                while True:
                                    if int(item_count) <= int(GameAttributes.pocket[item_name]):
                                        print(f'{100 * "="}')
                                        print(f"Are you sure that you want sell {int(item_count):,} {item_name} for {int(int(GameShop.shop_items[item_name]) * int(item_count)/2):,} coins?[Y][Q]".center(100))
                                        print(f'{100 * "="}')
                                        sell_warning = input(f"".center(50))
                                        if sell_warning == "Y":
                                            if int(item_count) <= int(GameAttributes.pocket[item_name]):
                                                GameAttributes.Coins += int(
                                                    int(item_count) * int(GameShop.shop_items[item_name])/2)
                                                print(f'{100 * "="}')
                                                print(
                                                    f'You sold {int(item_count):,} {item_name} for {int(int(item_count) *int(GameShop.shop_items[item_name])/2):,} coins. In your pocket you have a {GameAttributes.Coins:,} coins'.center(100))
                                                GameAttributes.pocket[item_name] -= int(
                                                    item_count)
                                                if int(GameAttributes.pocket[item_name]) == 0:
                                                    GameAttributes.pocket.pop(
                                                        item_name)
                                                break
                                            elif int(item_count) < 0:
                                                clearConsole()
                                                print(f'{100 * "="}')
                                                print(
                                                    f"You cannot enter a negative value to {item_name}".center(100))
                                                print(f'{100 * "="}')    
                                                break
                                            elif int(item_count) == 0:
                                                clearConsole()
                                                print(f'{100 * "="}')
                                                print(
                                                    f"You cannot enter a value equal 0 to {item_name}".center(100))
                                                print(f'{100 * "="}')    
                                        elif sell_warning == "Q":
                                            break
                                        elif sell_warning != "Q":
                                            continue
                                        elif sell_warning.isdigit:
                                            break
                                    else:
                                        print(f'{100 * "="}')
                                        print(f"You dont have {int(item_count)} {item_name} items in ur inventory. Actually you have a {GameAttributes.pocket[item_name]} {item_name}".center(100))
                                        break

                            if item_count == "Q":
                                clearConsole()
                                break
                            elif item_count != "Q":
                                continue

                            else:
                                clearConsole()
                                print(f'{100 * "="}')
                                print(
                                    f"You dont have {item_name} {int(item_count):,} in your inventory ".center(100))
                                continue
                    elif item_name == "Q":
                        clearConsole()
                        break
                    elif item_name == "LOOK":
                        clearConsole
                        look_items()

                    elif item_name in GameAttributes.pocket.keys() and item_name not in GameShop.shop_items.keys():
                        clearConsole()
                        print(f"You cannot sell {item_name} item".center(100))
                        continue
                    else:
                        clearConsole()
                        print(f'{100 * "="}')
                        print(f"You dont have {item_name} item".center(100))
                        continue

            elif sell_buy_look == "LOOK":
                clearConsole()
                look_items()
                continue
            elif sell_buy_look == "Q":
                break
            else:
                continue
