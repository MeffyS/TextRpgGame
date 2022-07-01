from telnetlib import GA
import time
from game_character import player
from game_character import player_equipment
from game_character import player_statistic
from game_character import player_informations
from game_character import CharacterBackpack
from change_equipment import changing_equipment
from game_clear_function import clearConsole


class GameAttributes:
    N = 0
    S = 0
    Floor = 1
    Moves = 0
    Coins = 6000
    player_chests = {}
    opened_chests = {}
    pocket = {'HealthPotion':1,'Golden Coin':120,'ManaPotion':20,'Diamond':20}
    player_equipment = {
        'Bow': [('Magic', 3), ('Mana', 3), ('Lucky', 4), ('Health', 3), ('Attack', 26)], 
        'Earrings': [('Stamina', 8), ('Experience', 2), ('Attack', 4)],
        'Helmet': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
        'Gloves': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
        'Chest': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
        'Boots': [('Defence', 8), ('Experience', 2), ('Attack', 4)],
        
        }
    player_inventory = [{'Gloves': [('Stamina', 2)]}, {'Helmet': [('Attack', 5)]}, {'Gloves': [('Attack', 30), ('Defence', 30), ('Health', 30), ('Mana', 30), ('Stamina', 30)]}]
    player_skills = []


used_items_by_player = player_equipment.equipment.items()
equipment_name_count = GameAttributes.pocket.items()


def main_equipment(move):
    summed_attributes_values = {}
    if move == "EQ":
        if player_equipment.equipment == {}:
            print("Actually you dont have a items")
            print(summed_attributes_values)
        else:
            for _, item_list in used_items_by_player:
                for item, count, in item_list:
                    if item in summed_attributes_values:
                        summed_attributes_values[item] += count
                        continue
                    else:
                        summed_attributes_values[item] = count
            try:
                player.max_attack += summed_attributes_values['Attack']
                player.defence += summed_attributes_values['Defence']
                player.max_health += summed_attributes_values['Health']
                player.max_mana += summed_attributes_values['Mana']
                player.max_stamina += summed_attributes_values['Stamina']
            except KeyError:
                player_informations.informations()
            for item, attribute in player_equipment.equipment.items():
                print(item, attribute)    
            player_equipment.equipment
            changing_equipment()

def your_equipment():
    print(f"In your pocket u have a:".center(100))
    print()
    for eq_item, count in equipment_name_count:
        print(f'{eq_item}:{count}'.center(100))
    while True:
        clearConsole()
        print(f"{100 * '='}")
        print(f"Do u want use any item?[Y][Q]".center(100))
        if_use_item = input(f"".center(50)).upper()
        if if_use_item == "Y":
            {item_name: item_count for (
                item_name, item_count) in equipment_name_count}
            while sum(GameAttributes.pocket.values()) > 0:
                print(f"{100 * '='}")
                for item_name, item_count in equipment_name_count:
                    print(f'[{item_name}][{item_count}]'.center(100))
                print(f"{100 * '='}")    
                print(f"Enter item name".center(100))
                print(f"{100 * '='}")
                what_to_use = input(f"".center(42))
                if range(sum(GameAttributes.pocket.values())) == 0:
                    break
                elif what_to_use == "Q":
                    break
                elif what_to_use in GameAttributes.pocket.keys():
                    if what_to_use == "ManaPotion":
                        clearConsole()
                        GameAttributes.pocket[f'{what_to_use}'] -= 1
                        player.mana += 50
                        print(f"{100 * '='}")
                        print(f"{what_to_use} has been used".center(100))

                        if GameAttributes.pocket[f'{what_to_use}'] == 0:
                            GameAttributes.pocket.pop(f'{what_to_use}')
                    elif what_to_use == "HealthPotion":
                        if player.health < player.max_health:
                            GameAttributes.pocket[f'{what_to_use}'] -= 1
                            player.health += 50
                            print(f"{100 * '='}")
                            print(f"{what_to_use} has been used".center(100))

                            if GameAttributes.pocket[f'{what_to_use}'] == 0:
                                GameAttributes.pocket.pop(f'{what_to_use}')
                        else:
                            clearConsole()
                            print(f"{100 * '='}")
                            print(f"Your health is maximal {player.health}/{player.max_health}".center(100))


                    elif what_to_use == "StaminaPotion":
                        clearConsole()
                        GameAttributes.pocket[f'{what_to_use}'] -= 1
                        player.stamina += 50
                        print(f"{what_to_use} has been used".center(100))
                        if GameAttributes.pocket[f'{what_to_use}'] == 0:
                            GameAttributes.pocket.pop(f'{what_to_use}')
                    else:
                        print(f"{100 * '='}")
                        print(f"This item cannot be used".center(100))
                        print(f"{100 * '='}")
                        continue
                elif what_to_use not in GameAttributes.pocket.keys():
                    print(f"{100 * '='}")
                    print(f"This item isn't in inventory".center(100))
                    print(f"{100 * '='}")
                    continue
                else:
                    print(f"{100 * '='}")
                    print(f"Click Q to exit [Q]".center(100))
                    print(f"{100 * '='}")

        elif if_use_item == "Q":
            break
        else:
            print(f"{100 * '='}")
            print(f"Click Q to exit [Q]".center(100))
            print(f"{100 * '='}")


def informations(info):

    if info == "INFO":
        clearConsole()
        sorted(GameAttributes.player_chests.items(),
               key=lambda x: x[1], reverse=True)
        print(f'{100*"="}')

        print(f"Level: {player.getLevel()}, Experience: {player.getExperience()} xp")
        
        print(f'{100*"="}')

        print(f"Statistic: Health:{player.getHealth()}/{player.getMaxHealth()},Mana:{player.getMana()}/{player.getMaxMana()},Stamina:{player.getStamina()}/{player.getMaxStamina()},Attack:{player.getMinAttack()}/{player.getMaxAttack()},Defence:{player.getDefence()},Magic:{player.getMagic()},Lucky:{player.getLucky()}")

        print(f'{100*"="}')

        # print(
        #     f'\n[Coins {GameAttributes.Coins}],\n[Floor {GameAttributes.Floor}],\n[Moves {GameAttributes.Moves}]')
        # print(
        #     f'[Chests {GameAttributes.player_chests}],[Left chests:{sum(GameAttributes.player_chests.values())}]')
        # print("Opened chests", GameAttributes.opened_chests)
  


def pocket(pocket):
    if pocket == 'pocket':
        # your_equipment()
        print(GameAttributes.pocket)


def direction_move():
    print(f"NORTH:{GameAttributes.N}||{GameAttributes.S}:SOUTH".center(100))
    
