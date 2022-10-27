from game_map import moves
from rozmiar_mapy import game_map_size
from game_character import player
from campfire_rest import explore
from game_system import game_stystem
from player_menu import character_menu


class GameDirections:
    position = 0
    east = 0  # +
    west = 0  # -

    def start_direction(self):
        while True:
            if self.position == 0:
                self.start_position()
            elif self.position > 0:
                if self.east < game_map_size.map:
                    enter_direction = input("Enter direction [E][U][W][MENU]").upper()
                    self.east_direction_positive(enter_direction)
                if self.east == game_map_size.map:
                    self.east_direction_negative()

            elif self.position < 0:
                if self.west < game_map_size.map:
                    enter_direction = input("Enter direction [E][U][W][MENU]").upper()
                    self.west_direction_positive(enter_direction)

                if self.west == game_map_size.map:
                    self.west_direction_negative()

    def start_position(self):
        direction = input("Enter direction [E][U][W][MENU]").upper()
        if direction == "E":
            self.east += 1
            self.west -= 1
            self.position += 1
            game_stystem()
        if direction == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1
            game_stystem()
        if direction == 'MENU':
            character_menu.player_menu(direction)


    def east_direction_negative(self):
        direction = input("Enter direction [U][W][C][Menu]").upper()
        if direction == "E":
            if self.east == self.position:
                print("You can't go any further on EAST")
                print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
        elif direction == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1
            print("Position", self.position)
            game_stystem()
        elif direction == 'MENU':
            character_menu.player_menu(direction)
        else:
            direction = input("Enter direction [U][W][C][MENU]").upper()

    def east_direction_positive(self, direct):
        if direct == "E":
            self.east += 1
            self.west -= 1
            self.position += 1
            print("Position", self.position)
            game_stystem()

        if direct == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1
            print("Position", self.position)
            game_stystem()
        if direct == 'MENU':
            character_menu.player_menu(direct)

    def west_direction_negative(self):
        direction = input("Enter direction [E][U][D][MENU]").upper()
        if direction == "W":
            if self.west == abs(self.position):
                print("You can't go any further on WEST")
                print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")

        elif direction == "E":
            print(direction)
            self.east += 1
            self.west -= 1
            self.position += 1
            game_stystem()

        elif direction == 'MENU':
            character_menu.player_menu(direction)

        else:
            direction = input("Enter direction [E][U][D][Menu]").upper()

    def west_direction_positive(self, direct):
        if direct == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1
            game_stystem()
        if direct == "E":
            self.east += 1
            self.west -= 1
            self.position += 1
            game_stystem()
        if direct == 'MENU':
            character_menu.player_menu(direct)


class GameMoves:
    def game_moves(self, start):
        if start == "start" or start == "1":
            game_map_size()
        if player.stamina > 0:
            game_direction.start_direction()
        if player.stamina <= 0:
            explore.explore_menu()


game_direction = GameDirections()
game_start = GameMoves()

game_start.game_moves("start")
