from enum import Enum
from game_clear_function import clearConsole
from game_character import player
import sys


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
    points_count = input(f"How many {player.points} you want spend?")
    player[attribute] += int(points_count)
    return player[attribute]

    # return player[attribute]


# add_points()
# print(player.max_health)
# add_points('s')
# print("hp", player.mana)


def player_attributes(move):
    if move == "STATISTIC":
        clearConsole()
        print(f"You have {player.points} points to add.")
        for number, attr in enumerate(Points):
            print(number, attr.name, attr.value[1])
            attribute_dict[attr.value[0]] = attr.name

        attribute = input("Enter attribute which you want upgrade ")

        if attribute == "Q" or attribute == "q":
            print("EXIT")

        if attribute == Points.HEALTH.name or attribute == Points.HEALTH.value[0]:
            attribute = "max_health"
            add_points(attribute)
            print(player.max_health)

        elif attribute == Points.MANA.name or int(attribute) == Points.MANA.value[0]:
            attribute = "max_mana"
            print(attribute)
        elif (
            attribute == Points.STAMINA.name
            or int(attribute) == Points.STAMINA.value[0]
        ):
            attribute = "max_stamina"
        elif (
            attribute == Points.DEFENCE.name
            or int(attribute) == Points.DEFENCE.value[0]
        ):
            pass
        elif (
            attribute == Points.ATTACK.name or int(attribute) == Points.ATTACK.value[0]
        ):
            attribute = "max_attack"
        elif attribute == Points.MAGIC.name or int(attribute) == Points.MAGIC.value[0]:
            pass
        elif attribute == Points.LUCKY.name or int(attribute) == Points.LUCKY.value[0]:
            pass

            # if attribute.isdigit() is True:
            #     upgrade = input(f"Do you want upgrade a {attribute_dict.get(int(attribute))}")
            # else:
            #     upgrade = input(f"Do you want upgrade a {attribute} ")
            #     if upgrade == "Y":
            #         points_count = input(f"How many {player.points} you want spend?")
            #         if player.points >= int(points_count):
            #             player[attribute.lower()] += int(points_count)
            #             print(player[attribute.lower()])
            #             return player[attribute.lower()]
        # elif attribute == Points.MANA.name or int(attribute) == Points.MANA.value[0]:
        #     print(f"Do you want upgrade a {attribute_dict.get(int(attribute))}")


player_attributes("STATISTIC")
# print(attribute_dict)
