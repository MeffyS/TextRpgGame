import time
import random
from enum import Enum

from game_character import player
from game_stage_chest_open import OpenChest
from game_player_pocket import player_pocket



class ExploreOptions(Enum):
    CHEST = "1"
    POCKET = "2"
    CAMPFIRE = "3"
    QUIT = "Q"


class ExploreChoice:
    agree = "Y"
    disagree = "Q"

    def explore_menu(self):
        print("You are exhausted. Use campfire to get stamine ")
        while True:
            for option in ExploreOptions:
                print(f"[{option.value}] {option.name}")
            try:
                while True:
                    menu_choice = input("Choose option ").upper()
                    if (
                        menu_choice == ExploreOptions.CHEST.name
                        or menu_choice == ExploreOptions.CHEST.value
                    ):
                        OpenChest.open_chest("CHEST")
                    elif (
                        menu_choice == ExploreOptions.POCKET.name
                        or menu_choice == ExploreOptions.POCKET.value
                    ):
                        player_pocket.open_pocket()
                    elif (
                        menu_choice == ExploreOptions.CAMPFIRE.name
                        or menu_choice == ExploreOptions.CAMPFIRE.value
                    ):
                        self.use_campfire()
                    elif (
                        menu_choice == ExploreOptions.QUIT.name
                        or menu_choice == ExploreOptions.QUIT.value
                    ): 
                        break
                    else:
                        print(f'{menu_choice!r} is not correct value')
            except ValueError:
                print(f"Entered value cannot be a letter. Except [Q]")
            break

    def use_campfire(self):
        while True:
            if player.stamina < 15:
                try:
                    explore_campfire = input(
                        "How many stamine you want to regenerate [15-100] "
                    )
                    if int(explore_campfire) < 15:
                        print("Entered value cannot be less than 15")
                    elif int(explore_campfire) == 0:
                        print("Entered value cannot be equal zero")
                    elif int(explore_campfire) > 100:
                        print("Entered value cannot be greater than 100")
                    else:
                        for _ in range(1, int(explore_campfire) + 1):
                            print(
                                f"STAMINE REGENERATION {player.stamina}/{player.max_stamina}"
                            )
                            time.sleep(0.2)
                            player.stamina += 1
                            if player.stamina % 10 == 0 and player.stamina != 0:
                                bonus_regen_mana = random.randint(1, 10)
                                bonus_regen_health = random.randint(1, 10)
                                player.health += bonus_regen_health
                                player.mana += bonus_regen_mana
                                if player.mana > player.max_mana:
                                    player.mana = player.max_mana
                                elif player.health > player.max_health:
                                    player.health = player.max_health
                                print(
                                    f"BONUS REGENERATE HEALTH +{bonus_regen_health}, MANA +{bonus_regen_mana}"
                                )
                                continue

                        break
                except ValueError:
                    if explore_campfire in ['Q','q']:
                        break
                    else:
                        print(f"Entered value cannot be a letter. Except [Q]")
            else:
                print("You dont need make a campfire")
                break


explore = ExploreChoice()
