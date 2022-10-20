from enum import Enum
from game_clear_function import clearConsole
from game_character import player


class Points(Enum):
    HEALTH = [0, player.max_health]
    MANA = [1, player.max_mana]
    STAMINA = [2, player.max_stamina]
    DEFENCE = [3, player.defence]
    ATTACK = [4, player.max_attack]
    MAGIC = [5, player.magic]
    LUCKY = [6, player.lucky]
    QUIT = [7, "Q"]

attribute_dict = {}


def add_points(attribute):
    while True:
        points_count = input(f"How many {player.points} you want spend?")
        try:
            if int(points_count) <= player.points and int(points_count) > 0:
                player[attribute] += int(points_count)
                return player[attribute]
            else:
                print(
                    f"Invalid value points {points_count}. Your current status of points {player.points} "
                )
        except ValueError:
            print("Entered value cannot be a letter sequence")
            continue


def player_attributes(move):
    if move == "STATISTIC":
        clearConsole()
        print(f"You have {player.points} points to add.")
        for number, attr in enumerate(Points):
            print(number, attr.name, attr.value[1])
            attribute_dict[attr.value[0]] = attr.name
        
        while True:
            attribute = input("Enter attribute which you want upgrade ")

            if attribute == "Q" or attribute == "q":
                break

            if attribute == Points.HEALTH.name or attribute == str(Points.HEALTH.value[0]):
                attribute = "max_health"
                add_points(attribute)

            elif attribute == Points.MANA.name or attribute == str(Points.MANA.value[0]):
                attribute = "max_mana"
                add_points(attribute)

            elif attribute == Points.STAMINA.name or attribute == str(
                Points.STAMINA.value[0]
            ):
                attribute = "max_stamina"
                add_points(attribute)

            elif attribute == Points.DEFENCE.name or attribute == str(
                Points.DEFENCE.value[0]
            ):
                attribute = "defence"
                add_points(attribute.lower())

            elif attribute == Points.ATTACK.name or attribute == str(
                Points.ATTACK.value[0]
            ):
                attribute = "max_attack"
                add_points(attribute)

            elif attribute == Points.MAGIC.name or attribute == str(Points.MAGIC.value[0]):
                attribute = "magic"
                add_points(attribute.lower())

            elif attribute == Points.LUCKY.name or attribute == str(Points.LUCKY.value[0]):
                attribute = "lucky"
                add_points(attribute.lower())
            elif attribute == Points.QUIT.name or attribute == str(Points.QUIT.value[0]):
                break


player_attributes("STATISTIC")
