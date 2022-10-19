from ctypes.wintypes import POINT
from enum import IntEnum, Enum
from game_character import player
from game_clear_function import clearConsole
from game_character import player_statistic


class Points(Enum):
    HEALTH = ["1", player.max_health]
    MANA = ["2", player.max_mana]
    STAMINA = ["3", player.max_stamina]
    DEFENCE = ["4", player.defence]
    ATTACK = ["5", player.max_attack]
    MAGIC = ["6", player.magic]
    LUCKY = ["7", player.lucky]
    QUIT = ["8", "Q"]


def player_stats(move):
    if move == "STATISTIC":
        clearConsole()
        attribute_occurrence_name = [attribute.name for attribute in Points]
        attribute_occurrence_value = [attribute.value for attribute in Points]
        while True:
            print(f'{100 * "="}')
            for point in Points:
                print(f"[{point.value[0]}] [{point.name}][{point.value[1]}]")

            print(f'{100 * "="}')
            choice = input(
                f"Which attribute you want upgrade? 1 - {len(Points)-1}"
            ).upper()

            clearConsole()
            if (
                choice == "Q"
                or choice == Points.QUIT.value
                or choice == Points.QUIT.name
            ):
                break
            if choice not in attribute_occurrence_name and choice not in attribute_occurrence_value[0][0]:
                print(attribute_occurrence_value[int(choice)-1][0])

            elif player.getPoints() > 0:
                how_many_points = int(input(f"How many points you want add? "))
                clearConsole()
                if int(how_many_points) > player.getPoints():
                    print(f'{100 * "="}')
                    print(
                        f"You dont have a points to upgrade. Your points [{player.getPoints()}]"
                    )

                elif int(how_many_points) <= player.getPoints():
                    print(player_statistic.statistic())
                    print(f"You have a {player.getPoints()} upgrade points")

                    if Points.HEALTH.name == choice or Points.HEALTH.value == choice:
                        player.health = player.getHealth() + how_many_points
                        player.max_health = player.getMaxHealth() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()

                    elif Points.MANA.name == choice or Points.MANA.value == choice:
                        player.mana = player.getMana() + how_many_points
                        player.max_mana = player.getMaxMana() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()

                    elif (
                        Points.STAMINA.name == choice or Points.STAMINA.value == choice
                    ):
                        player.stamina = player.getStamina() + how_many_points
                        player.max_stamina = player.getMaxStamina() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()

                    elif (
                        Points.DEFENCE.name == choice or Points.DEFENCE.value == choice
                    ):
                        player.defence = player.getDefence() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()

                    elif Points.ATTACK.name == choice or Points.ATTACK.value == choice:
                        player.max_attack = player.getMaxAttack() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()

                    elif Points.MAGIC.name == choice or Points.MAGIC.value == choice:
                        player.magic = player.getMagic() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()

                    elif Points.LUCKY.name == choice or Points.LUCKY.value == choice:
                        player.lucky = player.getLucky() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()

            else:
                print(f'{100 * "="}')
                print("You dont have a points to upgrade")
                print(f'{100 * "="}')
                break


player_stats("STATISTIC")

# z = [x.name for x in Points]
# print(z)
