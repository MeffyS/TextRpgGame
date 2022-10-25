from turtle import position
from game_map import GameMoves
from rozmiar_mapy import game_map_size
from game_character import player


class GameDirections:
    position = 0
    east = 0  # +
    west = 0  # -

    def start_direction(self):
        while True:
            if self.position == 0:
                direction = input("Enter direction [E][U][W] NR 0")
                if direction == "E":
                    self.east += 1
                    self.west -= 1
                    self.position += 1
                if direction == "W":
                    self.east -= 1
                    self.west += 1
                    self.position -= 1
            elif self.position > 0:
                if self.east < game_map_size.map:
                    direction = input("Enter direction [E][U][W] NR 1")
                    if direction == "E":
                        self.east += 1
                        self.west -= 1
                        self.position += 1
                    if direction == "W":
                        self.east -= 1
                        self.west += 1
                        self.position -= 1
                if self.east == game_map_size.map:
                    if direction == "E":
                        if self.east == self.position:
                            print("You can't go any further")
                            print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
                            direction = input("Enter direction [U][W][C] NR 4")
                    elif direction == "W":
                        self.east -= 1
                        self.west += 1
                        self.position -= 1
                    else:
                        direction = input("Enter direction [U][W][C] NR 4")
            
            elif self.position < 0:
                if self.west < game_map_size.map:
                    direction = input("Enter direction [E][U][W] NR 2")
                    if direction == 'W':
                        self.east -= 1
                        self.west += 1
                        self.position -= 1
                    if direction == 'E':
                        self.east += 1
                        self.west -= 1
                        self.position += 1
                if self.west == game_map_size.map:
                    if direction == 'W':
                        if self.west != self.position:
                            print("You can't go any further")
                            print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
                            direction = input("Enter direction [E][U][D] NR 4")
                    if direction == 'E':
                        self.east += 1
                        self.west -= 1
                        self.position += 1
                    else:
                        direction = input("Enter direction [E][U][D] NR 4")



    def east_direction_negative(self):
        print("Enter direction ")
        self.east -= 1
        self.position += 1
        print(self.position)

    def east_direction_positive(self):
        self.east += 1
        self.position += 1
        print(self.position)

    def west_direction_negative(self):
        self.west -= 1
        self.position += 1
        print(self.position)

    def west_direction_positive(self):
        self.west += 1
        self.position += 1
        print(self.position)


class GameMoves:
    def game_moves(self, start):
        if start == "start" or start == "1":
            game_map_size()
        if player.stamina > 0:
            gd.start_direction()


gd = GameDirections()
gm = GameMoves()
gm.game_moves("start")
