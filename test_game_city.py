
import random
import time
from enum import Enum, auto
from game_character import player_backpack
from game_character import player
from game_merchant import Merchant
from test_bank import NewBank


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
    Guess = auto()
    Dice = auto()
    Dice_Guess = auto()
    Quit = "Q"

    @staticmethod
    def guess_option():
        player_chances = 10
        guess_number = random.randint(1,2000)
        while True:
            coins = input("How many coins u want bet? ")
            print(guess_number)
            try:
                if int(coins) == 0:
                    print("You cannot bet 0 coins")
                elif int(coins) < 0:
                    print("You cannot bet less than 0 coins")
                elif int(coins) > player_backpack.coins:
                    print(f"You cannot bet more coins than is in your pocket {player_backpack.coins}")
                elif int(coins) <= player_backpack.coins and int(coins) > 0:
                    while True:
                        if guess_number > 0 and player_chances > 0:
                            try:
                                player_number = input("Choose number in the range of [1-2000]")
                                if int(player_number) > 2000:
                                    print("Guessing number cannot be greater than 2000")
                                elif int(player_number) == 0:
                                    print("Guessing number cannot be equal 0")
                                elif int(player_number) < 0:
                                    print("Guessing number cannot be lower than 0")
                                elif int(player_number) > guess_number:
                                    print(f'Rolled number is lower than {player_number}. Left chances {player_chances-1}/{player_chances}')
                                    player_chances -= 1
                                elif int(player_number) < guess_number:
                                    print(f'Rolled number is greater than {player_number}. Left chances {player_chances-1}/10')
                                    player_chances -= 1
                                elif int(player_number) == guess_number:
                                    print(f"!-{guess_number}-!-CONGRATULATIONS-!-{guess_number}-!")
                                    player_backpack.coins += (player_chances * int(coins))
                                    print(f"You won {player_chances * int(coins)}")
                                    break
                                else:
                                    print("!-!-!-YOU LOSE-!-!-!")
                                    player_backpack.coins -= int(coins)
                            except ValueError:
                                if player_number == "Q":
                                    print("You cannot leave from guess number game. Continue")
                                else:      
                                    print("Entered number cannot be a letter")
            except ValueError:
                if coins == "Q":
                    break
                else:      
                    print("Entered number cannot be a letter")
    @staticmethod
    def dice_option_first():
        while True:
            try:
                dice_draw = random.randint(1, 6)
                coins = input("How many coins u want bet? ")
                if int(coins) == 0:
                    print("You cannot bet 0 coins")
                elif int(coins) < 0:
                    print("You cannot bet less than 0 coins")
                elif int(coins) > player_backpack.coins:
                    print(f"You cannot bet more coins than is in your pocket {player_backpack.coins}")        
                elif int(coins) <= player_backpack.coins and int(coins) > 0:
                    while True:
                        try:
                            player_number = input("Please enter a number [1-6] ")
                            if int(player_number) == dice_draw:
                                print("!-!-!-CONGRATULATIONS-!-!-!")
                                print(f"You won {int(coins)*4}")
                                player_backpack.coins += int(coins) * 4
                                break
                            elif int(player_number) == 0:
                                print("Entered number cannot be equal 0")
                            elif int(player_number) < 0:
                                print("Entered number cannot be less than 0")
                            elif int(player_number) > 6:
                                print("Entered number cannot be greater than 6")  
                            else:
                                print("!-!-!-YOU LOSE-!-!-!")
                                print(f'You lose {int(coins)} coins')
                                player_backpack.coins -= int(coins)
                                break
                        except ValueError:
                            if player_number == "Q":
                                print("You cannot leave from guess number game. Continue")
                            else:      
                                print("Entered number cannot be a letter")

            except ValueError:
                if coins == "Q":
                    break
                else:
                    print("Entered number cannot be a letter")

    @staticmethod
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
                    while True:
                        player_number = input("Please enter a [Low][High] ")
                        if player_number == "Low" and (int(dice_draw)) <= 3 and (int(dice_draw)) > 0:
                            if dice_draw in [1,2,3]:
                                print(f"!-{dice_draw}-!-CONGRATULATIONS-!-{dice_draw}-!")
                                print(f"You won {int(coins)}")
                                player_backpack.coins += int(coins)
                                print(player_backpack.coins)
                                break
                        elif player_number == "High" and (int(dice_draw)) <= 6 and (int(dice_draw)) > 3:
                            if dice_draw in [4,5,6]:
                                print(f"!-{dice_draw}-!-CONGRATULATIONS-!-{dice_draw}-!")
                                print(f"You won {int(coins)}")
                                player_backpack.coins += int(coins)
                                print(player_backpack.coins)
                                break
                        elif player_number not in ['Low', 'High']:
                            if player_number == "Q":
                                print("You cannot leave from guess number game. Continue")
                            else:
                                print("You should choose between [Low] or [High]")
                        else:
                            print(f"!-{dice_draw}-!-YOU LOSE-!-{dice_draw}-!")
                            print(f'You lose {int(coins)}')
                            player_backpack.coins -= int(coins)
                            break
            except ValueError:
                if coins == "Q":
                    break
                else:
                    print("Entered number cannot be a letter, except [Q]")

    @staticmethod
    def play_city_game():
        print("Hello dear player in city dice game")
        print("Here you can guess dice number")
        print("You can guess if value is High or Low")
        print("Or you can just guess a number")

        while True:
            print("[1] Guess Dice Number")
            print("[2] Guess High or Low")
            print("[3] Guess Number")
            print("[Q] Quit")
            game = input("Choose type of a dice game")
            try:
                if int(game) == CityGames.Dice.value:
                    CityGames.dice_option_first()
                elif int(game) == CityGames.Dice_Guess.value:
                    CityGames.dice_option_second()
                elif int(game) == CityGames.Guess.value: 
                    CityGames.guess_option()
            except ValueError:
                if game == "Q":
                    break
                else:
                    print("Entered number cannot be a letter, except [Q]")

        
class CityCampfire(Enum):
    campfire_count = auto()
    campfire_half = auto()
    campfire_max = auto()
    campfire_quit = "Q"

    
    def campfire():
        stamine_to_regeneration = player.max_stamina - player.stamina
        while True:
            for campfire in CityCampfire:
                print(f'[{campfire.value}] to use a {campfire.name.replace("_"," ")}')
            try:
                stamine_regen = input("Choose number which you want regenerate")
                if stamine_regen == 'count' or int(stamine_regen) == CityCampfire.campfire_count.value:
                    while True:
                        stamine_count = input(f"Enter stamine count. You can regenerate {stamine_to_regeneration} points")
                        try:
                            if int(stamine_count) < 0:
                                print("You cannot regenerate stamine less than 1 point")
                            elif int(stamine_count) == 0:
                                print("You cannot regenerate stamine equal 0")
                            elif int(stamine_count) > stamine_to_regeneration:
                                print(f"You cannot regenerate stamine greate than {stamine_to_regeneration} points")
                            elif int(stamine_count) <= stamine_to_regeneration:
                                for regeneration in range(int(stamine_count))[::-1]:
                                    time.sleep(0.5)
                                    print(regeneration)
                                player.stamina += int(stamine_count)
                        except ValueError:
                            if stamine_count == "Q":
                                break  
                            else:
                                print("Entered value must be a number, except [Q]")
                elif stamine_regen == 'half' or int(stamine_regen) == CityCampfire.campfire_half.value:
                    for regeneration in range(int(stamine_to_regeneration/2))[::-1]:
                        time.sleep(0.5)
                        print(regeneration)
                    player.stamina += stamine_to_regeneration/2
                elif stamine_regen == 'max' or int(stamine_regen) == CityCampfire.campfire_max.value:
                    for regeneration in range(int(stamine_to_regeneration))[::-1]:
                        time.sleep(0.5)
                        print(regeneration)
                elif stamine_regen == 'quit' or int(stamine_regen) == CityCampfire.campfire_quit.value:
                    break
    
            except ValueError:
                if stamine_regen == "Q":
                    break
                else:
                    print("Entered value must be a number, except [Q]")



class City:

    
    def city(self):
        services = input(f"Check list of available services in city[Service][Info][Q]").upper()
        if services == "SERVICE":
            while True:
                try:
                    for service in CityNpcServices:
                        print(f"[{service.value.value}] {service.name.upper()}")
                    select_service = input("Enter service which you want to use")
                    if select_service == CityNpcServices.chest.name or int(select_service) == CityNpc.Edward.value:
                        print("CHEST")
                    elif select_service == CityNpcServices.campfire.name or int(select_service) == CityNpc.Fiora.value:
                        CityCampfire.campfire()
                    elif select_service == CityNpcServices.bank.name or int(select_service) == CityNpc.Marie.value:
                        bank.bank()
                    elif select_service == CityNpcServices.blacksmith.name or int(select_service) == CityNpc.Tom.value:
                        print("BLACKSMITH")
                    elif select_service == CityNpcServices.gambling.name or int(select_service) == CityNpc.Max.value:
                        CityGames.play_city_game()
                    elif select_service == CityNpcServices.shop.name or int(select_service) == CityNpc.Figo.value:
                        Merchant.merchant()
                    elif select_service == CityNpcServices.magic.name or int(select_service) == CityNpc.Amigo.value:
                        print("MAGIC")
                except ValueError:
                    if select_service == "Q":
                        break
                    else:
                        print("Entered value must be a number, except [Q]")
        
        


bank = NewBank()

