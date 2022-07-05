from enum import Enum

coins_in_chest = Enum('coins', ('gray', 'blue',
                               'green', 'yellow', 'orange', 'red', 'pink'))

chance_on_chest = {

    coins_in_chest.gray: 64,
    coins_in_chest.blue: 32,
    coins_in_chest.green: 16,
    coins_in_chest.yellow: 8,
    coins_in_chest.orange: 4,
    coins_in_chest.red: 2,
    coins_in_chest.pink: 1,

}

chance_on_coins = {

    coins_in_chest.gray: 1,
    coins_in_chest.blue: 2,
    coins_in_chest.green: 4,
    coins_in_chest.yellow: 8,
    coins_in_chest.orange: 16,
    coins_in_chest.red: 32,
    coins_in_chest.pink: 641,

}

chest_key_or_nothing = Enum('chest', ('CHEST', 'NOTHING', 'KEY'))

chance_on_chest_key_or_nothing = {
    chest_key_or_nothing.NOTHING: 20,
    chest_key_or_nothing.CHEST: 20,
    chest_key_or_nothing.KEY: 20,

}

chance_value = list(chance_on_chest_key_or_nothing.values())
chance_key = list(chance_on_chest_key_or_nothing.keys())

chance_on_coins_value = list(chance_on_chest.values())
chance_on_coins_key = list(chance_on_chest.keys())
