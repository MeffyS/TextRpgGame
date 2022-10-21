from rozmiar_mapy import game_map_size
from game_map import GameMoves
from campfire_rest import explore
from game_clear_function import clearConsole
from game_character import player
from game_system import main_game_system

from test_game_city import City


print(f"Start[1]".center(100))
print(f"About[2]".center(100))
print(f"Leave[0]".center(100))


start_exit = int(input(f"".center(50)))
# username = input("Enter username ")

clearConsole()


# Game

if start_exit == 1:
    game_map_size()
    clearConsole()
    while True:
        if player.getStamina() > 0:
            print(f'{100*"="}'.center(100))
            print(
                f"Choose a direction [N][S][U] Commends:[info][chest][statistic][pocket][eq] ".center(
                    100
                )
            )
            print(f'{100*"="}'.center(100))
            move = input(f"".center(50)).upper()
            main_game_system(move)
            if player.getStamina() > 0:
                if f"{move.upper()}" == "N":
                    GameMoves.north_moves()
                    while GameMoves.north == game_map_size.map:
                        print(f"{100 * '='}")
                        print(
                            f"Choose a direction [S][U][D]. Commands:[info][chest][statistic][pocket][eq] Dungeon ".center(
                                100
                            )
                        )
                        print(f"{100 * '='}")
                        move = input(f"".center(50)).upper()
                        clearConsole()
                        main_game_system(move)
                        if f"{move.upper()}" == "S":
                            GameMoves.south_moves()
                        if (
                            f"{move.upper()}" == "S"
                            and GameMoves.north < game_map_size.map
                        ):
                            print(f'{100*"="}'.center(100))
                            print(
                                f"Choose Direction [N][S][U]. Commands:[info][chest][statistic][pocket][eq] ".center(
                                    100
                                )
                            )
                            print(f'{100*"="}'.center(100))
                            move = input(f"".center(50)).upper()
                            main_game_system(move)

                            if f"{move.upper()}" == "N":
                                GameMoves.north_moves()
                            if f"{move.upper()}" == "S":
                                GameMoves.south_moves()
                            elif player.getStamina() == 0:
                                explore.explore_menu()

                        elif player.getStamina() == 0:
                            explore.explore_menu()
                if f"{move.upper()}" == "S":
                    GameMoves.south_moves()
                    while GameMoves.south == game_map_size.map:
                        if player.getStamina() > 0:
                            print(f"{100 * '='}")
                            print(
                                f"Choose Direction [N][U][C] Commands:[info][chest][statistic][pocket][eq] ".center(
                                    100
                                )
                            )
                            print(f"{100 * '='}")
                            move = input(f"".center(50)).upper()
                            main_game_system(move)
                            clearConsole()

                            if f"{move.upper()}" == "C":
                                City.city(move)

                            if f"{move.upper()}" == "N":
                                GameMoves.north_moves()
                            if (
                                f"{move.upper()}" == "N"
                                and GameMoves.north < game_map_size.map
                            ):
                                print(f'{100*"="}'.center(100))
                                print(
                                    f"Choose Direction [N][S][U] Commands:[info][chest][statistic][pocket][eq] ".center(
                                        100
                                    )
                                )
                                print(f'{100*"="}'.center(100))
                                move = input(f"".center(50)).upper()
                                main_game_system(move)

                                if f"{move.upper()}" == "N":
                                    GameMoves.north_moves()
                                elif player.getStamina() == 0:
                                    explore.explore_menu()
                                if f"{move.upper()}" == "S":
                                    GameMoves.south_moves()
                        else:
                            explore.explore_menu()

                elif player.getStamina() == 0:
                    explore.explore_menu()
            elif player.getStamina() == 0:
                explore.explore_menu()

        elif player.getStamina() == 0:
            explore.explore_menu()

elif start_exit == 2:
    game_informations()


elif start_exit == 0:
    print("Leaving")
