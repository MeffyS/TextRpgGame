from game_informations import GameAttributes as GameAttributes
from game_character import player_backpack
import random
import gold_chances_variables


def draw_chest_key_nothing(draw):
    gold_chances_variables.draw = random.choices(
        gold_chances_variables.chance_key, gold_chances_variables.chance_value)[0]
    if gold_chances_variables.draw == gold_chances_variables.chest_key_or_nothing.NOTHING:
        print(f"You found nothing".center(100))
        print(f'{100*"="}'.center(100))
    elif gold_chances_variables.draw == gold_chances_variables.chest_key_or_nothing.CHEST:
        gold_chances_variables.chance_on_chest = random.choices(
            gold_chances_variables.chance_on_coins_key, gold_chances_variables.chance_on_coins_value)[0]
        print(f"You found a chest in color {gold_chances_variables.chance_on_chest.name}".center(100))
        print(f'{100*"="}'.center(100))

        if gold_chances_variables.chance_on_chest.name not in GameAttributes.player_chests:
            GameAttributes.player_chests[gold_chances_variables.chance_on_chest.name] = 1

        else:
            GameAttributes.player_chests[gold_chances_variables.chance_on_chest.name] = GameAttributes.player_chests[
                gold_chances_variables.chance_on_chest.name] + 1

    elif gold_chances_variables.draw == gold_chances_variables.chest_key_or_nothing.KEY:
        print(f"You found catacombs key".center(100))
        print(f'{100*"="}'.center(100))
        if gold_chances_variables.chest_key_or_nothing.KEY.name not in player_backpack.dungeon_items:
            player_backpack.dungeon_items[gold_chances_variables.chest_key_or_nothing.KEY.name] = 1
        else:
            player_backpack.dungeon_items[gold_chances_variables.chest_key_or_nothing.KEY.name] += 1



