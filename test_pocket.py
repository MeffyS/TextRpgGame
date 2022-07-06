
from game_character import player_backpack
from game_character import player
from enum import Enum, auto

class PocketOptions(Enum):
    SmallHealthPotion = auto()
    SmallManaPotion = auto()
    SmallStaminaPotion = auto()


class PlayerPocket:

    
    def pocket(self):
        while True:
        print("In your pocket u have a: ")
        for number, (pocket_item, pocket_item_count) in enumerate(player_backpack.potion_pocket.items()):
            print(f'[{number+1}] {pocket_item} [{pocket_item_count}]')
        item_name = input("Enter a item")
        if item_name == str(PocketOptions.HealthPotion.value) or item_name == PocketOptions.HealthPotion.name:
            player_backpack.potion_pocket['SmallHealthPotion'] -= 1
            player.health += 50
            if player_backpack.potion_pocket['SmallHealthPotion'] == 0:
                player_backpack.potion_pocket.pop('SmallHealthPotion')
            if player.health > player.max_health:
                player.health == player.max_health
        elif item_name == str(PocketOptions.ManaPotion.value) or item_name == PocketOptions.ManaPotion.name:
            player_backpack.potion_pocket['SmallHealthPotion'] -= 1
            player.mana += 50
            if player_backpack.potion_pocket['SmallHealthPotion'] == 0:
                player_backpack.potion_pocket.pop('SmallHealthPotion')
            if player.mana > player.max_mana:
                player.mana == player.max_mana    
        elif item_name == str(PocketOptions.StaminaPotion.value) or item_name == PocketOptions.StaminaPotion.name:
            player_backpack.potion_pocket['SmallHealthPotion'] -= 1
            player.stamina += 50
            if player_backpack.potion_pocket['SmallHealthPotion'] == 0:
                player_backpack.potion_pocket.pop('SmallHealthPotion')
            if player.stamina > player.max_stamina:
                player.stamina == player.max_stamina         

a = PlayerPocket()
a.pocket()


# a = PlayerPocket()
# a.pocket()

# def your_equipment():
#     print(f"In your pocket u have a:".center(100))
#     print()
#     for eq_item, count in equipment_name_count:
#         print(f'{eq_item}:{count}'.center(100))
#     while True:
#         clearConsole()
#         print(f"{100 * '='}")
#         print(f"Do u want use any item?[Y][Q]".center(100))
#         if_use_item = input(f"".center(50)).upper()
#         if if_use_item == "Y":
#             {item_name: item_count for (
#                 item_name, item_count) in equipment_name_count}
#             while sum(GameAttributes.pocket.values()) > 0:
#                 print(f"{100 * '='}")
#                 for item_name, item_count in equipment_name_count:
#                     print(f'[{item_name}][{item_count}]'.center(100))
#                 print(f"{100 * '='}")    
#                 print(f"Enter item name".center(100))
#                 print(f"{100 * '='}")
#                 what_to_use = input(f"".center(42))
#                 if range(sum(GameAttributes.pocket.values())) == 0:
#                     break
#                 elif what_to_use == "Q":
#                     break
#                 elif what_to_use in GameAttributes.pocket.keys():
#                     if what_to_use == "ManaPotion":
#                         clearConsole()
#                         GameAttributes.pocket[f'{what_to_use}'] -= 1
#                         player.mana += 50
#                         print(f"{100 * '='}")
#                         print(f"{what_to_use} has been used".center(100))

#                         if GameAttributes.pocket[f'{what_to_use}'] == 0:
#                             GameAttributes.pocket.pop(f'{what_to_use}')
#                     elif what_to_use == "HealthPotion":
#                         if player.health < player.max_health:
#                             GameAttributes.pocket[f'{what_to_use}'] -= 1
#                             player.health += 50
#                             print(f"{100 * '='}")
#                             print(f"{what_to_use} has been used".center(100))

#                             if GameAttributes.pocket[f'{what_to_use}'] == 0:
#                                 GameAttributes.pocket.pop(f'{what_to_use}')
#                         else:
#                             clearConsole()
#                             print(f"{100 * '='}")
#                             print(f"Your health is maximal {player.health}/{player.max_health}".center(100))


#                     elif what_to_use == "StaminaPotion":
#                         clearConsole()
#                         GameAttributes.pocket[f'{what_to_use}'] -= 1
#                         player.stamina += 50
#                         print(f"{what_to_use} has been used".center(100))
#                         if GameAttributes.pocket[f'{what_to_use}'] == 0:
#                             GameAttributes.pocket.pop(f'{what_to_use}')
#                     else:
#                         print(f"{100 * '='}")
#                         print(f"This item cannot be used".center(100))
#                         print(f"{100 * '='}")
#                         continue
#                 elif what_to_use not in GameAttributes.pocket.keys():
#                     print(f"{100 * '='}")
#                     print(f"This item isn't in inventory".center(100))
#                     print(f"{100 * '='}")
#                     continue
#                 else:
#                     print(f"{100 * '='}")
#                     print(f"Click Q to exit [Q]".center(100))
#                     print(f"{100 * '='}")

#         elif if_use_item == "Q":
#             break
#         else:
#             print(f"{100 * '='}")
#             print(f"Click Q to exit [Q]".center(100))
#             print(f"{100 * '='}")