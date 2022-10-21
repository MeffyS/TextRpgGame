from enum import Enum
from operator import add
from game_clear_function import clearConsole
from game_character import player


class Points(Enum):
    MAX_HEALTH = [0, player.max_health, "HEALTH"]
    MAX_MANA = [1, player.max_mana, "MANA"]
    MAX_STAMINA = [2, player.max_stamina, "STAMINA"]
    DEFENCE = [3, player.defence, "DEFENCE"]
    ATTACK = [4, player.max_attack, "ATTACK"]
    MAGIC = [5, player.magic, "MAGIC"]
    LUCKY = [6, player.lucky, "LUCKY"]
    QUIT = [7, "Q", "QUIT"]


attribute_dict = {}


def add_points(attribute):

    while True:
        suffix = ""
        if player.points > 1:
            suffix = "s"
        points_count = input(
            f"How many [{player.points}] point{suffix} you want spend to upgrade your {attribute.upper()}?[Q]: "
        )
        try:
            if int(points_count) <= player.points and int(points_count) > 0:
                player[attribute] += int(points_count)
                player.points -= int(points_count)
                Points[attribute.upper()].value[1] = player[attribute]
                return player[attribute]
            elif int(points_count) == 0:
                break
            else:
                print(
                    f"Invalid value points {points_count}. Your current status of points {player.points} "
                )
        except ValueError:
            if points_count == "Q" or "q":
                break
            else:
                print("Entered value cannot be a letter sequence")
                continue


def player_attributes(move):
    if move == "STATISTIC":
        clearConsole()
        while True:
            suffix = ""
            if player.points > 1:
                suffix = "s"
            print(f"You have [{player.points}] point{suffix} to add.")
            for number, attr in enumerate(Points):
                print(f"{number:<3}|{attr.value[2]:<9}|{attr.value[1]:<10}")
                attribute_dict[attr.value[0]] = attr.name

            attribute = input("Enter attribute which you want upgrade: ")

            if attribute == "Q" or attribute == "q":
                break

            if attribute == Points.MAX_HEALTH.value[2] or attribute == str(
                Points.MAX_HEALTH.value[0]
            ):
                attribute = "max_health"
                add_points(attribute)

            elif attribute == Points.MAX_MANA.value[2] or attribute == str(
                Points.MAX_MANA.value[0]
            ):
                attribute = "max_mana"
                add_points(attribute)

            elif attribute == Points.MAX_STAMINA.value[2] or attribute == str(
                Points.MAX_STAMINA.value[0]
            ):
                attribute = "max_stamina"
                add_points(attribute)

            elif attribute == Points.DEFENCE.value[2] or attribute == str(
                Points.DEFENCE.value[0]
            ):
                attribute = "defence"
                add_points(attribute.lower())

            elif attribute == Points.ATTACK.value[2] or attribute == str(
                Points.ATTACK.value[0]
            ):
                attribute = "max_attack"
                add_points(attribute)

            elif attribute == Points.MAGIC.value[2] or attribute == str(
                Points.MAGIC.value[0]
            ):
                attribute = "magic"
                add_points(attribute.lower())

            elif attribute == Points.LUCKY.value[2] or attribute == str(
                Points.LUCKY.value[0]
            ):
                attribute = "lucky"
                add_points(attribute.lower())
            elif attribute == Points.QUIT.value[2] or attribute == str(
                Points.QUIT.value[0]
            ):
                break
