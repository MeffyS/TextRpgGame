
import random
from enum import Enum, auto
from game_character import player_backpack
from game_city import CityServices


class CityNpc(Enum):
    Edward = auto()
    Fiora = auto()
    Marie = auto()
    Tom = auto()
    Max = auto()
    Figo = auto()
    Amigo = auto()

class CityNpcServices(Enum):
    chest = CityNpc.Edward
    campfire = CityNpc.Fiora
    bank = CityNpc.Marie
    blacksmith = CityNpc.Tom
    gambling = CityNpc.Max
    shop = CityNpc.Figo
    magic = CityNpc.Amigo

class CitySkills(Enum):
    FireBall = auto()
    GreatFireBall = auto()
    CityTeleport = auto()
    Thunder = auto()
    HealthRegeneration = auto()
    GreatHealthRegeneration = auto()
    UltraHealthRegeneration = auto()


    def city_skills_price():

        skills_price = {
            'FireBall': 1000,
            'GreatFireBall': 2000,
            'CityTeleport': 5000,
            'Thunder': 7000,
            'HealthRegeneration': 1000,
            'GreatHealthRegeneration': 3000,
            'UltraHealthRegeneration': 5000,
            }
        return skills_price

class CityInformations:

    informations = (f"""In city, you can use a: 
    merchant service, 
    store items in storage,
    withdraw,deposit coins to bank, 
    regenerate stamine, 
    selling, buying items, 
    play games with gambler, 
    upgrade items""")


class CityGames(Enum):
    Gambling = auto()
    Dice = auto()

    @staticmethod
    def dice_option_first():
        while True:
                    try:
                        dice_draw = random.randint(1, 6)
                        coins= input("How many coins u want bet?")
                        if int(coins) == 0:
                            print("You cannot bet 0 coins")
                        elif int(coins) < 0:
                            print("You cannot bet less than 0 coins")
                        elif int(coins) > player_backpack.coins:
                            print(f"You cannot bet more coins than is in your pocket {player_backpack.coins}")
                        elif int(coins) <= player_backpack.coins:
                            enter_number = input("Please enter a number [1-6] ")
                            if int(enter_number) == dice_draw:
                                print("!-!-!-CONGRATULATIONS-!-!-!")
                                print(f"You won {int(coins)*4}")
                                player_backpack.coins += int(coins) * 4
                            elif int(enter_number) != dice_draw:
                                print("!-!-!-YOU LOSE-!-!-!")
                                print(f'You lose {int(coins)}')
                                player_backpack.coins -= int(coins)
                            elif int(enter_number) == 0:
                                print("Entered number cannot be equal 0")
                            elif int(enter_number) < 0:
                                print("Entered number cannot be less than 0")
                        elif int(enter_number) < 6:
                            print("Entered number cannot be greater than 6")
                    except ValueError:
                        if coins == "Q":
                            break
                        else:
                            print("Entered number cannot be a letter")

    def dice_option_second():
        while True:
            try:
                dice_draw = random.randint(1, 6)
                coins= input("How many coins u want bet?")
                if int(coins) == 0:
                    print("You cannot bet 0 coins")
                elif int(coins) < 0:
                    print("You cannot bet less than 0 coins")
                elif int(coins) > player_backpack.coins:
                    print(f"You cannot bet more coins than is in your pocket {player_backpack.coins}")
                elif int(coins) <= player_backpack.coins and int(coins) is not False:
                    enter_number = input("Please enter a [Low][High] ")
                    if enter_number == "Low" and (int(dice_draw)) <= 3 and (int(dice_draw)) > 0:
                        if dice_draw in [1,2,3]:
                            print(f"!-{dice_draw}-!-CONGRATULATIONS-!-{dice_draw}-!")
                            print(f"You won {int(coins)}")
                            player_backpack.coins += int(coins)
                            print(player_backpack.coins)
                    elif enter_number == "High" and (int(dice_draw)) <= 6 and (int(dice_draw)) > 3:
                        if dice_draw in [4,5,6]:
                            print(f"!-{dice_draw}-!-CONGRATULATIONS-!-{dice_draw}-!")
                            print(f"You won {int(coins)}")
                            player_backpack.coins += int(coins)
                            print(player_backpack.coins)
                    else:
                        print(f"!-{dice_draw}-!-YOU LOSE-!-{dice_draw}-!")
                        print(f'You lose {int(coins)}')
                        player_backpack.coins -= int(coins)
            except ValueError:
                if coins == "Q":
                    break
                else:
                    print("Entered number cannot be a letter, except [Q]")


    def play_city_game():
        print("Hello dear player in city dice game")
        print("Here you can guess dice number")
        print("You can guess if value is High or Low")
        print("Or you can just guess a number")

        while True:
            print("[0] Guess Dice Number")
            print("[1] Guess High or Low")
            print("[2] Guess High or Low")
            print("[Q] Quit")
            game = input("Choose type of a dice game")
            try:
                if int(game) == 0:
                    CityGames.dice_option_first()
                elif int(game) == 1:
                    CityGames.dice_option_second()
                elif int(game) == 2: 
                    print("DOnt work yet")
            except ValueError:
                if game == "Q":
                    break
                else:
                    print("Entered number cannot be a letter, except [Q]")

        

        

class City:
    services = input(f"Check list of available services in city[Service][Info][Q]").upper()
    if services == "SERVICE":
        for service in CityNpcServices:
            print(service.value.value, service.name)
        print(CityNpc.Edward.value)
        select_service = input("Enter service which you want to use")
        if select_service == CityNpcServices.chest.name or int(select_service) == CityNpc.Edward.value:
            print("CHEST")
        elif select_service == CityNpcServices.campfire.name or int(select_service) == CityNpc.Fiora.value:
            print("CAMPFIRE")
        elif select_service == CityNpcServices.bank.name or int(select_service) == CityNpc.Marie.value:
            print("BANK")
        elif select_service == CityNpcServices.blacksmith.name or int(select_service) == CityNpc.Tom.value:
            print("BLACKSMITH")
        elif select_service == CityNpcServices.gambling.name or int(select_service) == CityNpc.Max.value:
            CityGames.play_city_game()
        elif select_service == CityNpcServices.shop.name or int(select_service) == CityNpc.Figo.value:
            print("SHOP")
        elif select_service == CityNpcServices.magic.name or int(select_service) == CityNpc.Amigo.value:
            print("MAGIC")
        


a = City()

