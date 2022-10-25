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
                    enter_direction = input("Enter direction [E][U][W] NR 1")
                    self.east_direction_positive(enter_direction)
                if self.east == game_map_size.map:
                    self.east_direction_negative()
                    # if direction == "E":
                    #     if self.east == self.position:
                    #         print("You can't go any further")
                    #         print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
                    #         direction = input("Enter direction [U][W][C] NR 4")
                    # elif direction == "W":
                    #     self.east -= 1
                    #     self.west += 1
                    #     self.position -= 1
                    # else:
                    #     direction = input("Enter direction [U][W][C] NR 4")
            elif self.position < 0:
                if self.west < game_map_size.map:
                    enter_direction = input("Enter direction [E][U][W] NR 2")
                    self.west_direction_positive(enter_direction)
                    # if direction == "W":
                    #     self.east -= 1
                    #     self.west += 1
                    #     self.position -= 1
                    # if direction == "E":
                    #     self.east += 1
                    #     self.west -= 1
                    #     self.position += 1
                if self.west == game_map_size.map:
                    self.west_direction_negative()
                    # if direction == "W":
                    #     if self.west != self.position:
                    #         print("You can't go any further on WEST")
                    #         print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
                    #         direction = input("Enter direction [E][U][D] NR 4")
                    # if direction == "E":
                    #     self.east += 1
                    #     self.west -= 1
                    #     self.position += 1
                    # else:
                    #     direction = input("Enter direction [E][U][D] NR 4")

    def east_direction_negative(self):
        direction = input("Enter direction [U][W][C] NR 4")
        if direction == "E":
            if self.east == self.position:
                print("You can't go any further on EAST")
                print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
                # direction = input("Enter direction [U][W][C] NR 5 nr 0")
        elif direction == "W":
            print(direction)
            self.east -= 1
            self.west += 1
            self.position -= 1
        else:
            direction = input("Enter direction [U][W][C] NR 5 nr 1")

    def east_direction_positive(self, direct):
        if direct == "E":
            self.east += 1
            self.west -= 1
            self.position += 1
        if direct == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1

    def west_direction_negative(self):
        direction = input("Enter direction [E][U][D] NR 6 nr 1")
        if direction == "W":
            if self.west == abs(self.position):
                print("You can't go any further on WEST")
                print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
                # direction = input("Enter direction [E][U][D] NR 6")
        elif direction == "E":
            print(direction)
            self.east += 1
            self.west -= 1
            self.position += 1
        else:
            direction = input("Enter direction [E][U][D] NR 6 nr 2")

    def west_direction_positive(self, direct):
        if direct == "W":
            self.east -= 1
            self.west += 1
            self.position -= 1
        if direct == "E":
            self.east += 1
            self.west -= 1
            self.position += 1


class GameMoves:
    def game_moves(self, start):
        if start == "start" or start == "1":
            game_map_size()
        if player.stamina > 0:
            gd.start_direction()


gd = GameDirections()
gm = GameMoves()
gm.game_moves("start")
