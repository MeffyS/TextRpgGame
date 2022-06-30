from game_clear_function import clearConsole

def game_map_size():
    while True:
        try:
            game_map_size.map= int(input("Enter a map size in range [2-25]"))
            if game_map_size.map < 2 or game_map_size.map > 25:
                print("Incorrect mape size")
            else:
                break
        except ValueError:
            print("Entered value must be a number")

