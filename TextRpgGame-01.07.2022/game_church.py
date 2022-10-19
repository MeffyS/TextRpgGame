import time
from game_character import player


def church():
    if player.health < 0:
        for regenerate_health in range(player.max_health)[::-1]:
            time.sleep(0)
            print(f'You are unconscious by {regenerate_health} seconds')
        player.health = player.max_health
        print(f'{100*"="}')
        print("Any good villager help you, and pulled out you from well ")
        print(f'{100*"="}')
        
