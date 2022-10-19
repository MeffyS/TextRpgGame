from game_character import player
import game_informations
from game_clear_function import clearConsole


def level_statistic():
    player.max_attack = player.getMaxAttack() + (player.getLevel())
    player.health = player.getHealth() + (25*player.getLevel())
    player.max_health = player.getMaxHealth() + (25*player.getLevel())
    player.max_mana = player.getMana() + (25*player.getLevel())
    player.max_stamina = player.getStamina() + 10
    player.level = player.getLevel() + 1
    player.points = player.getPoints() + 5



def level_up():
    
    clearConsole()
    if player.experience >= player.level * 100:
        player.experience = player.experience - \
            (player.level * 100)
        level_statistic()
        if 'Golden Coin' not in game_informations.GameAttributes.pocket:
            game_informations.GameAttributes.pocket['Golden Coin'] = 1
        else:
            game_informations.GameAttributes.pocket['Golden Coin'] += 1


        print(f'{48*"="}({player.level}){48*"="}'.center(100))
        print(f"You have advanced to level {player.level}".center(100))
        print(f'{99*"="}'.center(100))

        
