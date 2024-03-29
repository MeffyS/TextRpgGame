# PLAYER SKILLS DECORATORS
from game_generators import thunder_attack

import well_monster
import time
from game_clear_function import clearConsole




def skill_name(function):
    def skill_name_using(*args, **kwargs):
        print(f'{100*"="}')
        skill_name = function.__name__.replace('_', ' ').title()
        print(f'{skill_name}'.center(100))
        print(f'{100*"="}')
        return function(*args, **kwargs)
    return skill_name_using


def thunder_attack_generator(thunder):
    def using_thunder(*args, **kwargs):
        attack_sum = 0
        clearConsole()
        print("*T*H*U*N*D*E*R*")
        for attack in thunder_attack():
            time.sleep(0.2)
            if attack:
                print(attack, "HIT")
                attack_sum += attack
        clearConsole()         
        print(f'{100*"="}')       
        print(f"Thunder took the monster  {attack_sum} health points. Left: {well_monster.Monster.health - attack_sum} Health Points ")
        print(f'{100*"="}')

        
        well_monster.Monster.health -= attack_sum

        return thunder(*args, **kwargs), attack_sum
    return using_thunder
