import pyttsx3

from rozmiar_mapy import game_map_size
from game_informations import GameAttributes
from opcja_otwierania_skrzyni import stamina_regeneration
from game_clear_function import clearConsole
from game_character import player
from game_system import main_game_system


from game_moves import North_Moves
from game_moves import South_Moves
from game_moves import Down_Moves
from game_city import city


engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)

# Bot writting


def talk():
    return engine.runAndWait()

# Text for Bota


def botText(text):
    engine.say(f"{text}")


# botText("Podaj nazwe użytkownika")
# talk()
# username = input("Podaj nazwę użytkownika")
# botText(f"Witaj,{username}")
# talk()
# Zaczęcie gry
print(f"Start[1]".center(100))
print(f"Leave[0]".center(100))


start_exit = int(input(f"".center(50)))


clearConsole()


# Game


if start_exit == 1:

    game_map_size()
    clearConsole()
    while True:
        if player.getStamina() > 0:
            print(f'{100*"="}'.center(100))
            print(f"Choose a direction [N][S][D] Commends:[info][chest][statistic][pocket][eq] ".center(100))
            print(f'{100*"="}'.center(100))
            move = input(f"".center(50)).upper()
            main_game_system(move)
            if player.getStamina() > 0:
                if f'{move.upper()}' == "N":
                    North_Moves()
                    while GameAttributes.N == game_map_size.map:
                        print(f"{100 * '='}")
                        print(f"Choose a direction [S][D][K]. Commands:[info][chest][statistic][pocket][eq]Katakumby ".center(100))
                        print(f"{100 * '='}")
                        move = input(f"".center(50)).upper()
                        clearConsole()
                        main_game_system(move)
                        if f'{move.upper()}' == "S":
                            South_Moves()
                        if f'{move.upper()}' == "S" and GameAttributes.N < game_map_size.map:
                            print(f'{100*"="}'.center(100))
                            print(f"Choose Direction [N][S][D]. Commands:[info][chest][statistic][pocket][eq] ".center(100))
                            print(f'{100*"="}'.center(100))
                            move = input(f"".center(50)).upper()
                            main_game_system(move)

                            if f'{move.upper()}' == "N":
                                North_Moves()
                            if f'{move.upper()}' == "S":
                                South_Moves()
                            elif player.getStamina() == 0:
                                stamina_regeneration()

                        elif player.getStamina() == 0:
                            stamina_regeneration()
                if f'{move.upper()}' == "S":
                    South_Moves()
                    while GameAttributes.S == game_map_size.map:
                        if player.getStamina() > 0:
                            print(f"{100 * '='}")
                            print(f"Choose Direction [N][D][C] Commands:[info][chest][statistic][pocket][eq] ".center(100))
                            print(f"{100 * '='}")
                            move = input(f"".center(50)).upper()
                            main_game_system(move)
                            clearConsole()

                            if f'{move.upper()}' == "C":
                                city(move)

                            if f'{move.upper()}' == "N":
                                North_Moves()
                            if f'{move.upper()}' == "N" and GameAttributes.N < game_map_size.map:
                                print(f'{100*"="}'.center(100))
                                print(f"Choose Direction [N][S][D] Commands:[info][chest][statistic][pocket][eq] ".center(100))
                                print(f'{100*"="}'.center(100))
                                move = input(f"".center(50)).upper()
                                main_game_system(move)

                                if f'{move.upper()}' == "N":
                                    North_Moves()
                                elif player.getStamina() == 0:
                                    stamina_regeneration()
                                if f'{move.upper()}' == "S":
                                    South_Moves()
                        else:
                            stamina_regeneration()

                elif player.getStamina() == 0:
                    stamina_regeneration()
            elif player.getStamina() == 0:
                stamina_regeneration()

        elif player.getStamina() == 0:
            stamina_regeneration()


elif start_exit == 0:
    print("Leaving")
