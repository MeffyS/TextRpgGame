
import time
from enum import Enum
import random

from game_informations import GameAttributes
from game_character import player
from game_merchant import Merchant
from game_deposit import money_deposit
from game_clear_function import clearConsole


class NPC(Enum):
    Tom = 1
    Edward = 2
    Fiora = 3
    Marie = 4
    Max = 5
    Figo = 6
    Amigo = 7


class CityServices(Enum):
    chest = NPC.Edward
    campfire = NPC.Fiora
    bank = NPC.Marie
    blacksmith = NPC.Tom
    gambling = NPC.Max
    shop = NPC.Figo
    magic = NPC.Amigo

class SkillList(Enum):
    FireBall = 1
    GreatFireBall = 2
    CityTeleport = 3
    Thunder = 4
    HealthRegeneration = 5
    GreatHealthRegeneration = 6
    UltraHealthRegeneration = 7


skill_price = {
    'FireBall': 1000,
    'GreatFireBall': 2000,
    'CityTeleport': 5000,
    'Thunder': 7000,
    'HealthRegeneration': 1000,
    'GreatHealthRegeneration': 3000,
    'UltraHealthRegeneration': 5000
}                                                                           


class GamblingGames(Enum):
    dice = 1
    number = 2
    gallows = 3

    def play_dice():
        while True:
            try:
                coins = input("How many coins u want bet? ")
                if coins == "Q":
                    break
                elif int(coins) == 0:
                    print("You cannot bet 0 coins")
                elif int(coins) < 0:
                    print("Number of coins cannot be negative")
                elif int(coins) <= GameAttributes.Coins and int(coins) > 0:
                    dice_draw = random.randint(1, 6)
                    enter_number = input(
                        "Choose number [1-6] and win coins.[Q] ")

                    if int(enter_number) > 6:
                        print("The number cannot be greater than [6]")
                    elif int(enter_number) == 0:
                        print("The number cannot be equal [0]")
                    elif int(enter_number) < 1:
                        print("The number cannot be lower than [1]")
                    elif int(enter_number) == dice_draw:
                        print(f"ROLLED NUMBER{dice_draw}")
                        print("YOU WIN")
                        GameAttributes.Coins += int(coins)
                        print(GameAttributes.Coins)
                    elif int(enter_number) != dice_draw:
                        print(f"ROLLED NUMBER{dice_draw}")
                        print("YOU LOSE")
                        GameAttributes.Coins -= int(coins)
                        print(GameAttributes.Coins)
                    elif enter_number == "Q":
                        break
            except Exception:
                continue

    def play_guess():

        while True:
            coins = input("How many coins u want bet? ")
            i = 10
            guess = random.randint(1, 2000)

            if coins == 'Q':
                break
            elif int(coins) == 0:
                print("You cannot bet 0 coins")
            elif int(coins) < 0:
                print("Number of coins cannot be negative")
            elif int(coins) <= GameAttributes.Coins and int(coins) > 0:
                while True:
                    try:
                        if i > 0:
                            enter_number = input("Choose number [1-2000]")
                            if int(enter_number) > 2000:
                                print(
                                    "The number cannot be greater than [2000]")
                            elif int(enter_number) < 0:
                                print("The number cannot be lower than [0]")
                            elif int(enter_number) == 0:
                                print("The number cannot be equal [0]")
                            elif int(enter_number) > guess:
                                print("Rolled number is lower")
                                i = i - 1
                                print(i)
                            elif int(enter_number) < guess:
                                print("Rolled number is greater")
                                i = i - 1
                                print(i)
                            elif int(enter_number) == guess:
                                print("CONGRATULATIONS YOU WON")
                                GameAttributes.Coins = GameAttributes.Coins + \
                                    (int(coins)*i)
                                print(f"WON {(int(coins)*i)}")
                                break

                        elif i == 0:
                            print(
                                f"YOU LOSE, GUESSING NUMBER: {guess}")
                            GameAttributes.Coins -= int(coins)
                            break
                        elif enter_number == guess:
                            continue
                    except Exception:
                        print(GameAttributes.Coins)
                        GameAttributes.Coins -= int(coins)
                        print(GameAttributes.Coins)
                        break


def city_stamine(campfire):
    while True:
        if campfire == 'CAMPFIRE':
            print(f'{100*"="}')
            print(
                f"How many stamine you want to regenerate?[Max = 250][Min = 1][Q]".center(100))
            print(f'{100*"="}')
            print(f"Your currently stamine {player.stamina}/{player.max_stamina}".center(100))
            regeneration_time = input("".center(50))
            if regeneration_time.isdigit():
                if int(regeneration_time) + player.stamina > player.max_stamina:
                    clearConsole()
                    print(f'{100*"="}')
                    print(
                        f"You cannot exceed more than {player.stamina}/{player.max_stamina} stamina points".center(100))

                else:
                    clearConsole()
                    if int(regeneration_time) < 1:
                        print(f'{100*"="}')
                        print(
                            f"{regeneration_time} is to small value to regenerate".center(100))
                    elif int(regeneration_time) > 250:
                        print(f'{100*"="}')
                        print(
                            f"{regeneration_time} is to high value to regenerate".center(100))
                    elif int(regeneration_time):
                        for reg_time in range(int(regeneration_time))[::-1]:
                            print(f'{reg_time} ***REGENERATE***'.center(100))
                            time.sleep(0.1)
                            if reg_time == 0:
                                player.stamina = player.stamina + \
                                    int(regeneration_time)
                                break
            elif regeneration_time == "Q":
                break
            elif regeneration_time != "Q":
                clearConsole()
                print(f'{100*"="}')
                print(f"You cannot use {regeneration_time} value. Try enter value or [Q]".center(100))
                continue
            else:
                if regeneration_time.isdigit() < 0:
                    print(f"{regeneration_time} is to low value to regenerate".center(100))
                else:
                    clearConsole()
                    print(f'{100*"="}')
                    print(f"You cannot use {regeneration_time} value. Try enter value or [Q]".center(100))
                    continue
            

def informations():
    informations = (f"""In city, you can use a: 
    merchant service, 
    store items in storage,
    withdraw,deposit coins to bank, 
    regenerate stamine, 
    selling, buying items, 
    play games with gambler, 
    upgrade items""".center(100))
    print(informations)


def welcome(move):
    greetings = 'WELCOME'
    if move == "C":
        informations
        for _, welcome in enumerate(greetings):
            time.sleep(0.1)
            
            print(f'{23*"*" + "🔰" + welcome + "🔰" + 23*"*"}'.center(100))


def city(move):
    welcome(move)
    while True:
        print(f"{100 * '='}")
        print(f"Check list of available services in city[Service][Info][Q]".center(100))
        print(f"{100 * '='}")
        services = input(f"".center(50)).upper()
        if services == "SERVICE":
            clearConsole()
            print(f'{100*"="}')
            for service in CityServices:
                print(f'[{service.name}] ➡ [{service.value.name}]'.center(100))
            print(f'{100*"="}')
            while True:
                
                print((f"Which service you want to use?[{CityServices.shop.name}][{CityServices.chest.name}][{CityServices.campfire.name}][{CityServices.bank.name}][{CityServices.blacksmith.name}][{CityServices.gambling.name}][well][Q] ".center(100)))
                print(f'{100*"="}')
                use_service = input(f"".center(50)).upper()
                if use_service == 'GAMBLING':
                    clearConsole()
                    print(
                        f'Yoo!!. I"am {CityServices.gambling.value}. Do you want some gambling?'.center(100))
                    print(
                        f'[{GamblingGames.dice.name}],[{GamblingGames.number.name}],[{GamblingGames.gallows.name}]')
                    print(f"Choose a game".center(100))
                    choose_game = input(f"".center(50))
                    if choose_game == GamblingGames.dice.name:
                        GamblingGames.play_dice()
                    elif choose_game == GamblingGames.number.name:
                        GamblingGames.play_guess()
                elif use_service == "CAMPFIRE":
                    clearConsole()
                    print(f"{100 * '='}")
                    print(f'Traveler!. My name is a {CityServices.campfire.value}. By my campfire you can easy regenerate you stamine'.center(100))

                    city_stamine(use_service)
                elif use_service == "SHOP":
                    clearConsole()
                    print(f'Welcome, You just dropped by {CityServices.shop.value}. I can offer you some trading? Here are my goods:'.center(100))
                    Merchant.merchant(use_service)
                elif use_service == "WELL":
                    clearConsole()
                    coin_well_draw()
                elif use_service == 'BANK':
                    clearConsole()
                    money_deposit(use_service)
                elif use_service == "MAGIC":
                    clearConsole()
                    print("HeEy,HeY, I'a,m sso sorry 'HICK' that I'a 'HICK' drunk, but i can 'HICK' show u some maghhic".center(100))
                    print(f"Do u want see skills?[Y][Q] ".center(100))
                    what_do = input(f"".center(50))
                    if what_do == 'Y':
                        for skill,price in skill_price.items():
                            print(f'{skill:30} : {price:10,} coins'.center(100))
                    elif what_do == 'Q':
                        clearConsole()
                        break

                elif use_service == 'Q':
                    clearConsole()
                    break #break na continue
        elif services == "INFO":
            clearConsole()
            informations()
        elif services == "Q":
            clearConsole()
            break