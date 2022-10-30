import random
import time
from enum import Enum, auto
from game_character import player_backpack
from game_character import player
from game_merchant import Merchant
from game_bank import NewBank
from game_well import coin_well_draw


class CityNpc(Enum):
    Edward = auto()
    Fiora = auto()
    Marie = auto()
    Tom = auto()
    Max = auto()
    Figo = auto()
    Amigo = auto()
    Frank = auto()


class CityNpcServices(Enum):
    CHEST = CityNpc.Edward
    CAMPFIRE = CityNpc.Fiora
    BANK = CityNpc.Marie
    BLACKSMITH = CityNpc.Tom
    GAMBLING = CityNpc.Max
    SHOP = CityNpc.Figo
    MAGIC = CityNpc.Amigo
    WELL = CityNpc.Frank


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
            "FireBall": 1000,
            "GreatFireBall": 3000,
            "CityTeleport": 5000,
            "Thunder": 7000,
            "HealthRegeneration": 1000,
            "GreatHealthRegeneration": 3000,
            "UltraHealthRegeneration": 5000,
        }
        return skills_price


class CityInformations:

    informations = f"""In city, you can use a: 
    merchant service, 
    store items in storage,
    withdraw,deposit coins to bank, 
    regenerate stamine, 
    selling, buying items, 
    play games with gambler, 
    upgrade items"""



class CityGames(Enum):
    GUESS = '1'
    DICE = '2'
    DICE_GUESS = '3'
    QUIT = "Q"

    @staticmethod
    def guess_option():
        player_chances = 10
        guess_number = random.randint(1, 2000)
        while True:
            coins = input("How many coins u want bet? ")
            try:
                if int(coins) == 0:
                    print("You cannot bet 0 coins")
                elif int(coins) < 0:
                    print("You cannot bet less than 0 coins")
                elif int(coins) > player_backpack.coins:
                    print(
                        f"You cannot bet more coins than is in your pocket {player_backpack.coins}"
                    )
                elif int(coins) <= player_backpack.coins and int(coins) > 0:
                    while True:
                        if guess_number > 0 and player_chances > 0:
                            try:
                                player_number = input(
                                    "Choose number in the range of [1-2000]"
                                )
                                if int(player_number) > 2000:
                                    print("Guessing number cannot be greater than 2000")
                                elif int(player_number) == 0:
                                    print("Guessing number cannot be equal 0")
                                elif int(player_number) < 0:
                                    print("Guessing number cannot be lower than 0")
                                elif int(player_number) > guess_number:
                                    print(
                                        f"Rolled number is lower than {player_number}. Left chances {player_chances-1}/10"
                                    )
                                    player_chances -= 1
                                elif int(player_number) < guess_number:
                                    print(
                                        f"Rolled number is greater than {player_number}. Left chances {player_chances-1}/10"
                                    )
                                    player_chances -= 1
                                elif int(player_number) == guess_number:
                                    print(
                                        f"!-{guess_number}-!-CONGRATULATIONS-!-{guess_number}-!"
                                    )
                                    player_backpack.coins += player_chances * int(coins)
                                    print(f"You won {player_chances * int(coins)*2}")
                                    break
                                else:
                                    print("!-!-!-YOU LOSE-!-!-!")
                                    player_backpack.coins -= int(coins)
                                    break
                            except ValueError:
                                if player_number == "Q":
                                    print(
                                        "You cannot leave from guess number game. Continue"
                                    )
                                else:
                                    print("Entered number cannot be a letter")
                        else:
                            break
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
                    print(
                        f"You cannot bet more coins than is in your pocket {player_backpack.coins}"
                    )
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
                                print(f"You lose {int(coins)} coins")
                                player_backpack.coins -= int(coins)
                                break
                        except ValueError:
                            if player_number == "Q":
                                print(
                                    "You cannot leave from guess number game. Continue"
                                )
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
                coins = input("How many coins u want bet?")
                if int(coins) == 0:
                    print("You cannot bet 0 coins")
                elif int(coins) < 0:
                    print("You cannot bet less than 0 coins")
                elif int(coins) > player_backpack.coins:
                    print(
                        f"You cannot bet more coins than is in your pocket {player_backpack.coins}"
                    )
                elif int(coins) <= player_backpack.coins and int(coins) is not False:
                    while True:
                        player_number = input("Please enter a [Low][High] ")
                        if (
                            player_number == "Low"
                            and (int(dice_draw)) <= 3
                            and (int(dice_draw)) > 0
                        ):
                            if dice_draw in [1, 2, 3]:
                                print(
                                    f"!-{dice_draw}-!-CONGRATULATIONS-!-{dice_draw}-!"
                                )
                                print(f"You won {int(coins)}")
                                player_backpack.coins += int(coins)
                                print(player_backpack.coins)
                                break
                        elif (
                            player_number == "High"
                            and (int(dice_draw)) <= 6
                            and (int(dice_draw)) > 3
                        ):
                            if dice_draw in [4, 5, 6]:
                                print(
                                    f"!-{dice_draw}-!-CONGRATULATIONS-!-{dice_draw}-!"
                                )
                                print(f"You won {int(coins)}")
                                player_backpack.coins += int(coins)
                                print(player_backpack.coins)
                                break
                        elif player_number not in ["Low", "High"]:
                            if player_number == "Q":
                                print(
                                    "You cannot leave from guess number game. Continue"
                                )
                            else:
                                print("You should choose between [Low] or [High]")
                        else:
                            print(f"!-{dice_draw}-!-YOU LOSE-!-{dice_draw}-!")
                            print(f"You lose {int(coins)}")
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
            print("[1] Guess Number")
            print("[2] Guess High or Low")
            print("[3] Guess Dice Number")
            print("[Q] Quit")
            game = input("Choose type of a dice game").upper()
            try:
                if game == CityGames.DICE_GUESS.value:
                    CityGames.dice_option_first()
                elif game == CityGames.DICE.value:
                    CityGames.dice_option_second()
                elif game == CityGames.GUESS.value:
                    CityGames.guess_option()
                elif game == CityGames.QUIT.value:
                    break
            except ValueError:
                print(f"Entered {game!r} is not correct")


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
                if (
                    stamine_regen == "count"
                    or int(stamine_regen) == CityCampfire.campfire_count.value
                ):
                    while True:
                        stamine_count = input(
                            f"Enter stamine count. You can regenerate {stamine_to_regeneration} points"
                        )
                        try:
                            if int(stamine_count) < 0:
                                print("You cannot regenerate stamine less than 1 point")
                            elif int(stamine_count) == 0:
                                print("You cannot regenerate stamine equal 0")
                            elif int(stamine_count) > stamine_to_regeneration:
                                print(
                                    f"You cannot regenerate stamine greate than {stamine_to_regeneration} points"
                                )
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
                elif (
                    stamine_regen == "half"
                    or int(stamine_regen) == CityCampfire.campfire_half.value
                ):
                    for regeneration in range(int(stamine_to_regeneration / 2))[::-1]:
                        time.sleep(0.5)
                        print(regeneration)
                    player.stamina += stamine_to_regeneration / 2
                elif (
                    stamine_regen == "max"
                    or int(stamine_regen) == CityCampfire.campfire_max.value
                ):
                    for regeneration in range(int(stamine_to_regeneration))[::-1]:
                        time.sleep(0.5)
                        print(regeneration)
                elif (
                    stamine_regen == "quit"
                    or int(stamine_regen) == CityCampfire.campfire_quit.value
                ):
                    break

            except ValueError:
                if stamine_regen == "Q":
                    break
                else:
                    print("Entered value must be a number, except [Q]")


class City:
    def city(self):
        print('welcome in elvarion city!'.upper())
        services = input(
            f"Check list of available services in city[SERVICE][INFO][Q]"
        ).upper()
        if services == "SERVICE":
            while True:
                try:
                    for service in CityNpcServices:
                        print(f"[{service.value.value}] {service.name.upper()}")
                    select_service = input("Enter service which you want to use")
                    if (
                        select_service == CityNpcServices.CHEST.name
                        or int(select_service) == CityNpc.Edward.value
                    ):
                        print("CHEST")
                    elif (
                        select_service == CityNpcServices.CAMPFIRE.name
                        or int(select_service) == CityNpc.Fiora.value
                    ):
                        CityCampfire.campfire()
                    elif (
                        select_service == CityNpcServices.BANK.name
                        or int(select_service) == CityNpc.Marie.value
                    ):
                        bank.bank()
                    elif (
                        select_service == CityNpcServices.BLACKSMITH.name
                        or int(select_service) == CityNpc.Tom.value
                    ):
                        print("BLACKSMITH")
                    elif (
                        select_service == CityNpcServices.GAMBLING.name
                        or int(select_service) == CityNpc.Max.value
                    ):
                        CityGames.play_city_game()
                    elif (
                        select_service == CityNpcServices.SHOP.name
                        or int(select_service) == CityNpc.Figo.value
                    ):
                        Merchant.merchant()
                    elif (
                        select_service == CityNpcServices.MAGIC.name
                        or int(select_service) == CityNpc.Amigo.value
                    ):
                        print("MAGIC")
                    elif (
                        select_service == CityNpcServices.WELL.name
                        or int(select_service) == CityNpc.Frank.value
                    ):
                        coin_well_draw()
                except ValueError:
                    if select_service == "Q":
                        break
                    else:
                        print("Entered value must be a number, except [Q]")
        if services == "INFO":
            print(CityInformations.informations)


bank = NewBank()
game_city = City()
# game_city.city()
