import random
from game_character import player
from game_character import player_backpack
from game_character import player_level_up
from game_informations import your_equipment
from game_drop_system import drop_item
from game_church import church



class Monster:

    def __init__(self, monster_name ='test_name', health=2500, mana=0, defence=0, attack_min=0, attack_max=0, magic=0, experience=0, coins=0):
        self.__monster_name = monster_name
        self.__health = health
        self.__mana = 0
        self.__defence = 0
        self.__attack_max = 0
        self.__attack_min = 0
        self.__magic = 0
        self.__experience = 0
        self.__coins = 0

# MONSTER WHICH PLAYER CAN FIGHT IN WELL!

class Rat(Monster):
    def __init__(self, monster_name='Rat', health=0, attack_min=0, attack_max=0,experience=0, coins=0):
        super().__init__(monster_name, health, attack_min, attack_max, experience, coins)
        self.__monster_name = monster_name
        self.__health = 20
        self.__attack_min = 5
        self.__attack_max = 10
        self.__experience = 5
        self.__coins = random.randint(1,5)


class Bat(Monster):
    def __init__(self, monster_name='Bat', health=0, attack_min=0, attack_max=0,experience=0, coins=0):
        super().__init__(monster_name, health, attack_min, attack_max, experience, coins)
        self.__monster_name = monster_name
        self.__health = 25
        self.__attack_min = 7
        self.__attack_max = 12
        self.__experience = 8
        self.__coins = random.randint(2,8)


class Bug(Monster):
    def __init__(self, monster_name='Bug', health=0, attack_min=0, attack_max=0,experience=0, coins=0):
        super().__init__(monster_name, health, attack_min, attack_max, experience, coins)
        self.__monster_name = monster_name
        self.__health = 30
        self.__attack_min = 10
        self.__attack_max = 12
        self.__experience = 12
        self.__coins = random.randint(4,12)


class Spider(Monster):
    def __init__(self, monster_name='Spider', health=0, attack_min=0, attack_max=0,experience=0, coins=0):
        super().__init__(monster_name, health, attack_min, attack_max, experience, coins)
        self.__monster_name = monster_name
        self.__health = 45
        self.__attack_min = 20
        self.__attack_max = 30
        self.__experience = 20
        self.__coins = random.randint(20,25)


class Slime(Monster):
    def __init__(self, monster_name='Slime', health=0, attack_min=0, attack_max=0,experience=0, coins=0):
        super().__init__(monster_name, health, attack_min, attack_max, experience, coins)
        self.__monster_name = monster_name
        self.__health = 60
        self.__attack_min = 26
        self.__attack_max = 36
        self.__experience = 50
        self.__coins = random.randint(40,50)


class Ghost(Monster):
    def __init__(self, monster_name='Ghost', health=0, attack_min=0, attack_max=0,physic_defence=0, experience=0, coins=0):
        super().__init__(monster_name, health, attack_min, attack_max, experience, coins)
        self.__monster_name =monster_name
        self.__health = 100
        self.__attack_min = 15
        self.__attack_max = 60
        self.__physic_defence = 0.9
        self.__experience = 100
        self.__coins = random.randint(60,120)



def draw_monster():
    monster_list = [Rat(),Bat(),Bug(),Spider(),Slime(),Ghost()]

    return random.choice(monster_list)


class FightWithMonster:

    def fight(self):
        __monster = draw_monster()
        print(f"You will fight with, {__monster.monster_name}")
        while True:
            fight = input(f"Hit monster [A], Pocket[P], Escape [Q]")
            if fight == 'A':
                player_hit = random.randint(player.min_attack,player.max_attack)
                monster_hit = random.randint(__monster.attack_min, __monster.attack_max)
                __monster.health -= player_hit
                player.health -= monster_hit
                print(f"Monster lose {player_hit}. Left {__monster.health}")
                print(f"You lose {monster_hit}. Left {player.health}/{player.max_health}")
                if __monster.health <= 0 and player.health <= 0:
                    print("You are dead. Monster is dead")
                    break
                elif player.health > 0 and __monster.health <= 0:
                    print("Monster is dead")
                    player_backpack.coins += __monster.coins
                    player.experience += __monster.experience
                    print(f"From {__monster.__monster_name} you got +{__monster.experience} exp and +{__monster.coins} coins ")
                    player_level_up.level_up()
                    drop_item()
                    
                    
                    break
                elif __monster.health > 0 and player.health <= 0:
                    print('You are dead')  
                    church()  
                    break
            elif fight == "P":
                your_equipment()
            elif fight == "Q":
                player_escape = input("Do u want escape? You lose 50 points of stamine [Q] ")
                if player_escape == "Q":
                    player.stamina -= 50
                    break
            else:
                print("Choose other value")
            
  

b = Ghost()
b.

    




