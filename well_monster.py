import random

from game_character import player
from game_character import player_level_up


from game_clear_function import clearConsole
import game_well
import game_player_atributes

from game_informations import your_equipment
from game_informations import GameAttributes
from game_drop_system import drop_item as drop



def monster():
    monster_file_part_one = 'D:/PythonGra/TextRpgGame-01.07.2022/nazwa_potwora/nazwa_potwora_1.txt'
    monster_file_part_two = 'D:/PythonGra/TextRpgGame-01.07.2022/nazwa_potwora/nazwa_potwora_2.txt'
    

    with open(monster_file_part_one) as file, open(monster_file_part_two) as file2:
        file_one_contents = file.readlines()
        file_two_contents = file2.readlines()
        for _ in range(1):
            emotions = (random.choice(file_one_contents)).strip()
            animals = (random.choice(file_two_contents[0:3])).strip()
            print(f'{100 * "="}')
            print(f"Drawing enemy is: {animals}".center(100))
            print(f'{100 * "="}')

    if animals == "Rat":
        print('RAAT')

    elif animals == "Wolf":
        print('RAAT')

    elif animals == "Bear":
        print('RAAT')
    elif animals == "Tiger":
        print('RAAT')

    return animals


class Monster:

    def __init__(self, health=2500, mana=0, defence=0, attack_min=0, attack_max=0, magic=0, experience=0, coins=0):
        self.health = health
        self.mana = 0
        self.defence = 0
        self.attack_max = 0
        self.attack_min = 0
        self.magic = 0
        self.experience = 0
        self.coins = 0


def fight(self, *args, **kwargs):

    minimal_atak = int(player.max_attack - 1)
    maximal_atak = int(player.max_attack + 1)
    while True:
        if self.health <= 0 and player.health <= 0:
            player.skill_count = 2
            player.min_attack = player.max_attack
            print("YOU ARE DEAD, MONSTER IS DEAD")
            church()
        elif self.health > 0 and player.health > 0:
            print(
                "What do you want to do?[A-Attack][S-Skill][P-Pocket][Q-Exit] ".center(100))
            what_to_do = input("".center(50)).upper()
            if what_to_do == 'A':
                draw_attack = random.randint(minimal_atak, maximal_atak)
                round_attack = round(draw_attack, 0)
                self.health -= round_attack
                clearConsole()
                print(f'{100*"="}')
                print(
                    f'The normal attack took the monster {round_attack} health points. LEFT {self.health} monster Health Points'.center(100))
                print(f'{100*"="}')
                monster_hit = round(random.randint(
                    self.attack_min, self.attack_max)) / player.defence
                player.health -= monster_hit
                print(
                    f'The monster attack took YOU {round(monster_hit)} health points. LEFT {round(player.health)} player Health Points'.center(100))
                print(f'{100*"="}')
            elif what_to_do == 'S':
                from player_skills import used_skill
                clearConsole()
                used_skill(self, *args, **kwargs)
            elif what_to_do == 'P':
                your_equipment()
            elif what_to_do == "Q":
                print(f'{100*"="}')
                print(
                    f"Do you want escape? Your stamina will be reduced by 50 points. Your stamine state is {player.stamina}/{player.max_stamina} [Y][N]".center(100))
                print(f'{100*"="}')
                escape = input(f"".center(50)).upper()
                if escape == "Y":
                    if player.stamina >= 50:
                        player.stamina -= 50
                        player.skill_count = 2
                        player.min_attack = player.max_attack
                        print(player.stamina)
                        break
                    else:
                        print(
                            f"You dont have enough stamine {player.stamina}/50. You must continue a fight!".center(100))
                elif escape == "N":
                    continue
        elif self.health <= 0:
            print(f'The monster is dead'.center(100))
            print(100*'=')
            player.skill_count = 2
            player.min_attack = player.max_attack
            player.experience += self.experience
            GameAttributes.Coins += self.coins
            print(
                f'You got from the monster +{self.experience} experience and +{self.coins} coins ')
            player_level_up.level_up()
            drop()
            leaving_the_well = input("Exit[Q] ").upper()
            game_well.well_leave(leaving_the_well)
            break
        elif player.health <= 0:
            player.skill_count = 2
            player.min_attack = player.max_attack
            print("You are dead")
            break
            


def draw_monster(self):
    monster_name = monster()

    if monster_name == "Rat":
        rat = Rat()
        mob_health = rat.health
        mob_attack_min = rat.attack_min
        mob_attack_max = rat.attack_max
        mob_defence = rat.defence
        fight(rat, mob_health, mob_attack_min, mob_attack_max, mob_defence)

    elif monster_name == "Wolf":
        wolf = Wolf()
        mob_health = wolf.health
        mob_attack_min = wolf.attack_min
        mob_attack_max = wolf.attack_max
        mob_defence = wolf.defence
        fight(wolf, mob_health, mob_attack_min, mob_attack_max, mob_defence)

    elif monster_name == "Bear":

        bear = Bear()
        mob_health = bear.health
        mob_attack_min = bear.attack_min
        mob_attack_max = bear.attack_max
        mob_defence = bear.defence
        fight(bear, mob_health, mob_attack_min, mob_attack_max, mob_defence)

    elif monster_name == "Tiger":
        tiger = Tiger()
        mob_health = tiger.health
        mob_attack_min = tiger.attack_min
        mob_attack_max = tiger.attack_max
        mob_defence = tiger.defence
        fight(tiger, mob_health,mob_attack_min,mob_attack_max,mob_defence)


class Rat(Monster):
    def __init__(self, health=0, mana=0, defence=0, attack_min=1, attack_max=4, magic=0, experience=0, coins=0):
        super().__init__(health, mana, defence, attack_min,
                         attack_max, magic, experience, coins)
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.attack = random.randint(self.attack_min, self.attack_max)
        self.health = 10
        self.experience = 5
        self.coins = random.randint(1, 10)


class Wolf(Monster):
    def __init__(self, health=0, mana=0, defence=0, attack_min=2, attack_max=10, magic=0, experience=0, coins=0):
        super().__init__(health, mana, defence, attack_min,
                         attack_max, magic, experience, coins)
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.attack = random.randint(self.attack_min, self.attack_max)
        self.health = 25
        self.experience = 30
        self.coins = random.randint(10, 15)


class Bear(Monster):
    def __init__(self, health=0, mana=0, defence=0, attack_min=5, attack_max=20, magic=0, experience=0, coins=0):
        super().__init__(health, mana, defence, attack_min,
                         attack_max, magic, experience, coins)
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.attack = random.randint(self.attack_min, self.attack_max)
        self.health = 50
        self.experience = 65
        self.coins = random.randint(15, 20)


class Tiger(Monster):
    def __init__(self, health=0, mana=0, defence=0, attack_min=8, attack_max=25, magic=0, experience=0, coins=0):
        super().__init__(health, mana, defence, attack_min,
                         attack_max, magic, experience, coins)
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.attack = random.randint(self.attack_min, self.attack_max)
        self.health = 60
        self.experience = 70
        self.coins = random.randint(20, 25)
