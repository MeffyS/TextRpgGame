

from game_character import player
import time
from game_clear_function import clearConsole as clearConsole
from game_stage_chest_open import chests_opening as game_open_stage


def chest_opening(chest):
    if chest == "CHEST":  # chest
        clearConsole()
        open_chest = input(
            "Do you want go to opening chest option? Yes/No ").upper()
        if open_chest == "YES":

            game_open_stage()

        else:
            pass


def stamina_regeneration():
    clearConsole()
    print(f'{100*"="}')
    print(
        f"To regenerate stamine, you can rest by the camfire.[campfire][chest]".center(100))
    print(f'{100*"="}')
    campfire = input(f"".center(50)).upper()
    clearConsole()
    if campfire == 'CAMPFIRE':
        while True:
            print(f'{100*"="}')
            print(
                f"How many stamine you want to regenerate?[Max = 100][Min = 15]".center(100))
            print(f'{100*"="}')
            regeneration_time = input("".center(50))
            if regeneration_time.isdigit():
                if int(regeneration_time) + player.stamina > player.max_stamina:
                    clearConsole()
                    print(f'{100*"="}')
                    print(
                        f"You cannot exceed more than {player.stamina}/{player.max_stamina} stamina points".center(100))

                else:
                    clearConsole()
                    if int(regeneration_time) < 15:
                        print(f'{100*"="}')
                        print(
                            f"{regeneration_time} is to small value to regenerate".center(100))
                    elif int(regeneration_time) > 100:
                        print(f'{100*"="}')
                        print(
                            f"{regeneration_time} is to high value to regenerate".center(100))
                        print(f'{100*"="}')
                    elif int(regeneration_time):
                        print(f'{100*"="}')
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

    elif campfire == "CHEST":
        game_open_stage()
