import random
import time
from enum import Enum

import well_monster
import game_church
from gold_chances_variables import coins_in_chest
from game_clear_function import clearConsole
from game_character import player
from game_character import player_backpack




well_drop = Enum('well', ('POSITIVE_COINS', 'POSITIVE_HEALTH',
                          'NOTHING', 'NEGATIVE_COINS', 'NEGATIVE_HEALTH', 'CHESTS', 'DUNGEGON_KEY', 'DEATH'))

chance_well_drop = {
    well_drop.POSITIVE_COINS: 0,
    well_drop.NEGATIVE_COINS: 0,
    well_drop.NOTHING: 0,
    well_drop.POSITIVE_HEALTH: 0,
    well_drop.NEGATIVE_HEALTH: 0,
    well_drop.CHESTS: 0,
    well_drop.DEATH: 100,


}

chance_well_drop_values = list(chance_well_drop.values())
chance_well_drop_keys = list(chance_well_drop.keys())


# well_draw = random.choices(chance_well_drop_keys, chance_well_drop_values)[0]


def well_regeneration():
    print("By tossing a gold coin to well, some resident, pushed You and You fell inside")
    for regenerate_health in range(player.max_health)[::-1]:
        time.sleep(0)
        print(f'You are unconscious by {regenerate_health} seconds'.center(100))
        player.health = player.max_health
    print(f'{100 * "="}')
    print(f"You woke up, You are inside well. What do you want to do?".center(100))
    print(f'{100 * "="}')
    print(f"Explore? Leave?[Explore][Leave]".center(100))
    well_action = input(f"".center(50)).upper()
    clearConsole()
    if well_action == "EXPLORE":
        well_monster.draw_monster(well_action)
    elif well_action == "LEAVE":
        print(f'{100 * "="}')
        print("You leaving")


def coin_well_draw():
    
    while True:
        if player.health > 0:
            well_draw = random.choices(chance_well_drop_keys, chance_well_drop_values)[0]
            print(f'{100 * "="}')
            coin = input("Do you want drop golden coin to inside of a well?[Y] ").upper()
            if coin == "Y":
                try:
                    if player_backpack.city_items['Golden Coin'] >= 1:
                        if 'Golden Coin' in player_backpack.city_items:
                            if well_draw == well_draw.POSITIVE_HEALTH:
                                player.health += 50
                                print("Your health has been increased about 50 points")
                                print(player.health)
                                player_backpack.city_items['Golden Coin'] -= 1

                            elif well_draw == well_draw.NOTHING:
                                print("Your coin disappeared somewhere down the well")
                                player_backpack.city_items['Golden Coin'] -= 1

                            elif well_draw == well_draw.POSITIVE_COINS:
                                print(player_backpack.coins)
                                player_backpack.coins += (1*1000)
                                print(player_backpack.coins)
                                print("Your coins has beed insceased about 1000 coins")
                                player_backpack.city_items['Golden Coin'] -= 1

                            elif well_draw == well_draw.NEGATIVE_COINS:
                                print(player_backpack.coins)
                                player_backpack.coins -= (1*1000)
                                print(player_backpack.coins)
                                player_backpack.city_items['Golden Coin'] -= 1
                                print("Your coins has been decreased about 1000 coins")

                            elif well_draw == well_draw.NEGATIVE_HEALTH:
                                player.health -= 50
                                print("Your health has been decreased about 50 points")
                                print(player.health)
                                player_backpack.city_items['Golden Coin'] -= 1

                            elif well_draw == well_draw.CHESTS:
                                print(f'OLD CHEST COUNT: {player_backpack.new_chests}')
                                
                                if 'pink' and 'red' and 'orange' and 'yellow' and 'green' and 'blue' and 'gray' not in player_backpack.new_chests:
                                    for chest in coins_in_chest:
                                        print(chest.name)
                                        player_backpack.new_chests[chest.name] = 1

                                elif player_backpack.city_items['Golden Coin'] == 1:
                                    print("You dont have a golden coins in your inventory")
                                    print(f'{100 * "="}')
                                    break

                                elif 'pink' or 'red' or 'orange' or 'yellow' or 'green' or 'blue' or 'gray' in player_backpack.new_chests:
                                    for chest in coins_in_chest:
                                        print(chest.name)
                                        
                                        if chest.name in player_backpack.new_chests:
                                            player_backpack.new_chests[chest.name] += 1
                                        elif chest.name not in player_backpack.new_chests:
                                            player_backpack.new_chests[chest.name] = 1
                                    player_backpack.city_items['Golden Coin'] -= 1

                                else:
                                    player_backpack.city_items['Golden Coin'] -= 1
                                    for chest in coins_in_chest:
                                        print(chest.name)
                                        player_backpack.new_chests[chest.name] += 1
                                print(f'NEW CHEST COUNT: {player_backpack.new_chests}')


                            elif well_draw == well_draw.DEATH:
                                if player_backpack.city_items['Golden Coin'] >= 1:
                                    player_backpack.city_items['Golden Coin'] -= 1
                                    well_regeneration()

                    else:
                        print(f'{100 * "="}')
                        print("You dont have a golden coins in your inventory")
                        print(f'{100 * "="}')
                except KeyError:
                    print("You dont have a golden coin")
            elif coin == "Q":
                break
        else:
            game_church.church()        

def well_leave(leave):
    print(f'{100 * "="}')
    print( "Except for the bad smell,I can't see anything else here. Leaving")

if __name__ == '__main__':
    coin_well_draw()