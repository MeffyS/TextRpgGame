from enum import IntEnum, Enum
from game_character import player
from game_clear_function import clearConsole
from game_character import player_statistic


class Points(Enum):
    HEALTH = '1'
    MANA = '2'
    STAMINA = '3'
    DEFENCE = '4'
    ATTACK = '5'
    MAGIC = '6'
    LUCKY = '7'


def player_stats(move):
    if move == 'STATISTIC':
        clearConsole()
        while True:
            print(f'{100 * "="}')
            print(player_statistic.statistic())
            print(f'{100 * "="}')
            choice = input("Which attribute you want upgrade?[1-7] ").upper()

            clearConsole()
            if choice == "Q":
                break
            elif player.getPoints() > 0:
                how_many_points = int(input(f'How many points you want add? '))
                clearConsole()
                if int(how_many_points) > player.getPoints():
                    print(f'{100 * "="}')
                    print(f"You dont have a points to upgrade. Your points [{player.getPoints()}]")

                elif int(how_many_points) <= player.getPoints():
                    print(player_statistic.statistic())
                    print(f'You have a {player.getPoints()} upgrade points')

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

                    elif Points.STAMINA.name == choice or Points.STAMINA.value == choice:
                        player.stamina = player.getStamina() + how_many_points
                        player.max_stamina = player.getMaxStamina() + how_many_points
                        player.points = player.getPoints() - how_many_points
                        print(f"Left {player.points} points")
                        clearConsole()
                        
                    elif Points.DEFENCE.name == choice or Points.DEFENCE.value == choice:
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
