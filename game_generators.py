import random
import time

from game_character import Character

# PLAYER SKILLS

player = Character()

def thunder_attack():
    for _ in range(random.randint(1,20)):
        attack = random.randint(player.min_attack*player.level, player.max_attack*player.level)
        yield attack
