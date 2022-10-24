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
            print(f"WEST:{self.west}|{self.position}|{self.east}:EAST")
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
            elif self.position >= 0:
                direction = input("Enter direction [E][U][W] NR 1")
                if direction == "E":
                    self.east += 1
                    self.west -= 1
                    self.position += 1
                if direction == "W":
                    self.east -= 1
                    self.west += 1
                    self.position -= 1
            elif self.position <= 0:
                direction = input("Enter direction [E][U][W] NR 2")
                if direction == 'W':
                    self.east -= 1
                    self.west += 1
                    self.position -= 1
                if direction == 'E':
                    self.east += 1
                    self.west -= 1
                    self.position += 1
                    
            # elif self.position <= 0:
            # direction = input("Enter direction [E][U][W] NR 2")
            #     self.west -= 1
            #     self.east += 1
            #     pass

        # while True:
        #     if self.east == self.position and self.west == self.position:
        #         direction = input("Enter direction [E][U][W] NUM 1")
        #         if direction == 'E':
        #             self.position += 1
        #             continue
        #         elif direction == 'W':
        #             self.position -= 1
        #             continue
        #     if self.east > 0 and self.west < 0:
        #         direction = input("Enter direction [E][U][W] NUM 2")

        # if direction == 'E':
        #     self.east += 1
        #     self.west -= 1
        #     self.position += 1
        #     print(self.position)
        #     direction = input("Enter direction [E][U][W] NUM 2")
        #     if direction == 'E':
        #         self.east += 1
        #         self.west -= 1
        #         self.position += 1
        #         print(self.position)
        #         direction = input("Enter direction [E][U][W] NUM 3")
        #     if direction == 'W':
        #         self.east -= 1
        #         self.west += 1
        #         self.position -= 1
        #         print(self.position)
        #         direction = input("Enter direction [E][U][W] NUM 4")
        # if direction == 'W':
        #     self.east -= 1
        #     self.west += 1
        #     self.position -= 1
        #     print(self.position)
        #     direction = input("Enter direction [E][U][W] NUM 5")
        #     if direction == 'E':
        #         self.east += 1
        #         self.west -= 1
        #         self.position += 1
        #         print(self.position)
        #     if direction == 'W':
        #         self.east -= 1
        #         self.west += 1
        #         self.position -= 1
        #         print(self.position)

        # while True:
        #     if self.east == 0 and self.west == 0:
        #         direction = input("Choose move direction [E][U][W] num 111111111111111111111111111")
        #     if direction == 'E' and game_map_size.map > self.east:
        #         self.position += 1
        #         self.east += 1
        #         self.west -= 1
        #         while self.east < game_map_size.map:
        #             if self.east > 0 and self.west < 0:
        #                 self.east += 1
        #                 direction = input("Choose move direction [E][U][W] num 2")
        #             if self.east == game_map_size.map:
        #                 while True:
        #                     direction = input("Choose move direction [U][W] num 3")
        #                     if direction == 'W':
        #                         self.east -= 1
        #                         self.west += 1
        #                         print(self.west)
        #                         break
        #                     if direction == 'E':
        #                         print("You cannot go on East")
        #     if direction == 'W' and game_map_size.map > self.west:
        #         self.position += 1
        #         self.east -= 1
        #         self.west += 1

        # if direction == 'W' and game_map_size.map > self.west:
        #     self.position -= 1
        #     self.west += 1
        #     self.east -= 1
        #     if self.east != 0 and self.west != 0:
        #         direction = input("Choose move direction [E][U][W] num 3")

        # if direction == 'E':
        #     self.east += 1
        #     self.position += 1
        #     direction = input("Choose move direction [E][U][W]")
        #     if direction == 'E':
        #         self.east_direction_positive()
        #     elif direction == 'W':
        #         self.west_direction_negative()
        #     elif self.position == 0:
        #         self.start_direction()
        # elif direction == 'W':
        #     self.position -= 1

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
