from rozmiar_mapy import game_map_size
from game_character import player
from campfire_rest import explore
from game_system import game_stystem
from player_menu import character_menu
from test_game_city import game_city


def game_coordinates(self):
        print(f"WEST POSITION: [ {self.west} ] || PLAYER {self.position} POSITION || [ {self.east} ] :EAST POSITION")



class GameDirections:
    position = 0
    east = 0  # +
    west = 0  # -

    def start_direction(self):

        while True:
            if player.stamina > 0:
                game_coordinates(self)
                if self.position == 0:
                    self.start_position()
                elif self.position > 0:
                    if self.east < game_map_size.map:
                        enter_direction = input("Enter direction [W][U][E][MENU] NR 1").upper()
                        self.east_direction_positive(enter_direction)
                    if self.east == game_map_size.map:
                        self.east_direction_negative()

                elif self.position < 0:
                    if self.west < game_map_size.map:
                        enter_direction = input("Enter direction [W][U][E][MENU] NR 2").upper()
                        self.west_direction_positive(enter_direction)

                    if self.west == game_map_size.map:
                        self.west_direction_negative()
            else:
                game_stystem()

    def start_position(self):
        
        direction = input("Enter direction [W][U][E][MENU] NR 3").upper()
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
        direction = input("Enter direction [W][U][C][MENU NR 4]").upper()
        if direction == "E":
            if self.east == self.position:
                print("You can't go any further on EAST")
                print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
        elif direction == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1
            game_stystem()
        elif direction == 'MENU':
            character_menu.player_menu(direction)
        elif direction == 'C':
             game_city.city()
        else:
            direction = input("Enter direction [W][U][C][MENU] NR 5").upper()



    def east_direction_positive(self, direct):
        if direct == "E":
            self.east += 1
            self.west -= 1
            self.position += 1
            game_stystem()
        if direct == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1
            game_stystem()
        if direct == 'MENU':
            character_menu.player_menu(direct)


    def west_direction_negative(self):
        direction = input("Enter direction [D][U][E][MENU] NR 6").upper()
        if direction == "W":
            if self.west == abs(self.position):
                print("You can't go any further on WEST")
                print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")

        elif direction == "E":
            self.east += 1
            self.west -= 1
            self.position += 1
            game_stystem()


        elif direction == 'MENU':
            character_menu.player_menu(direction)

        else:
            direction = input("Enter direction [D][U][E][MENU] NR 7").upper()

    def west_direction_positive(self, direct):
        if direct == "W" :
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