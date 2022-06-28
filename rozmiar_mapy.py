from game_clear_function import clearConsole

def map_size():
    while True:
        print(f'{100*"="}')

        print(f'Enter a map size in range [2-25]'.center(100))
        print(f'{100*"="}')
        map_size.map = int(input(f''.center(50)))
        if map_size.map < 2 or map_size.map == 0 or map_size.map > 25:
            clearConsole()
            print(f'{100*"="}'.center(100))
            print(f"Enter a correct map size in range [2-25]".center(100))
            continue
        else:
            break
