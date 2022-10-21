
from game_character import player_backpack
from game_character import player
from enum import Enum, auto
from items import SP, MP, HP

class PocketOptions(Enum):
    HealthPotion = auto()
    ManaPotion = auto()
    StaminaPotion = auto()


class PlayerPotionPocket:

    @classmethod
    def open_pocket(cls):
        agree = 'Y'
        disagree = 'Q'
        while True:
            explore_pocket = input("Do you want open pocket? [Y][Q] ")
            if explore_pocket == agree:
                PlayerPotionPocket.pocket('POCKET')
            elif explore_pocket == disagree:
                break
            else:
                print("Entered value is incorrect, please try [Y][Q]")

    @classmethod
    def pocket(cls,move):
        if move == 'POCKET':
            while True:
                useable = []
                print("In your pocket u have a: ")
                for pocket_item, pocket_item_count in player_backpack.potion_pocket.items():
                    print(pocket_item_count, pocket_item)
                item_name = input("Enter a item or [Q] ")
                if item_name in player_backpack.potion_pocket:    

                    if item_name == str(PocketOptions.HealthPotion.value) or item_name == PocketOptions.HealthPotion.name:
                        if player.mana > player.max_mana:
                            player_backpack.potion_pocket['HealthPotion'] -= 1
                            player.health += (HP.health * player.level)
                            print(f'+{HP.health * player.level} health points')
                            if player_backpack.potion_pocket['HealthPotion'] == 0:
                                player_backpack.potion_pocket.pop('HealthPotion')
                            if player.health > player.max_health:
                                player.health == player.max_health
                                break
                        else:
                            print("You are full health")  

                    elif item_name == str(PocketOptions.ManaPotion.value) or item_name == PocketOptions.ManaPotion.name:
                        if player.mana > player.max_mana:
                            player_backpack.potion_pocket['ManaPotion'] -= 1
                            player.mana += (MP.mana * player.level)
                            print(f'+{MP.mana * player.level} mana points')
                            if player_backpack.potion_pocket['ManaPotion'] == 0:
                                player_backpack.potion_pocket.pop('ManaPotion')
                            if player.mana > player.max_mana:
                                player.mana == player.max_mana
                                break
                        else:
                            print("You are full mana")    

                    elif item_name == str(PocketOptions.StaminaPotion.value) or item_name == PocketOptions.StaminaPotion.name:
                        if player.stamina < player.max_stamina:
                            player_backpack.potion_pocket['StaminaPotion'] -= 1
                            player.stamina += SP.stamine * player.level
                            print(f'+ {SP.stamine * player.level} stamina points')
                            if player_backpack.potion_pocket['StaminaPotion'] == 0:
                                player_backpack.potion_pocket.pop('StaminaPotion')
                            if player.stamina > player.max_stamina:
                                player.stamina == player.max_stamina
                                break
                        else:
                            print("You are full stamina")

                elif item_name == 'Q':
                    break
                else:
                    print(f"You dont have {item_name} in your potion pocket")

player_pocket = PlayerPotionPocket()
player_pocket.open_pocket()
