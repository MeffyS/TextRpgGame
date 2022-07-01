from game_character import player_backpack
from enum import Enum, auto

class BankOptions(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()
    BALANCE = auto()
    POCKET = auto()
    QUIT = "Q"

class BankWithdraw:

    def withdraw():
        print(f"You choosed option WITHDRAW")
        withdraw = input(f"How many coins you want withdrawn?")
        try:
            if int(withdraw) > BankBalance.balance:
                print(f"You dont have {int(withdraw)} in bank. In Your bank balance you got {BankBalance.balance}")
            elif int(withdraw) == 0:
                print(f"You cannot withdrawn 0 coins")
            elif int(withdraw) < 0:
                print(f"You cannot withrdawn coins with negative value")
            elif int(withdraw) <= BankBalance.balance:
                BankBalance.balance -= int(withdraw)
                player_backpack.coins += int(withdraw)
                print(f"You withdraw to bank {withdraw} coins. You have a {BankBalance.balance} coins in pocket")
        except ValueError:
            if withdraw == "Q":
                print("exit")
            else:
                print("You cannot enter a letters, except [Q] ")

class BankDeposit:
    def deposit():
        print(f"You choosed option DEPOSIT")
        while True:
            deposit = input(f"How many coins you want deposit?")
            try:
                if int(deposit) > player_backpack.coins:
                    print(f"You dont have {int(deposit)} in pocket. In Your pocket balance you got {player_backpack.coins}")
                elif int(deposit) == 0:
                    print(f"You cannot deposit 0 coins")
                elif int(deposit) < 0:
                    print(f"You cannot deposit coins with negative value")
                elif int(deposit) <= player_backpack.coins:
                    BankBalance.balance += int(deposit)
                    player_backpack.coins -= int(deposit)
                    print(f"You deposit to bank {deposit} coins. You have a {player_backpack.coins} coins in pocket")
                break
            except ValueError:
                if deposit == "Q":
                    break
                else:
                    print("You cannot enter a letters, except [Q] ")


class BankBalance:
    balance = 10

    def bank_balance():
        print(f"Dear player, your total bank balance is {BankBalance.balance} coins")

class BankPocket:

    def pocket_balance():
        print(f"Dear player, your total pocket balance is {player_backpack.coins} coins")


class Bank:
    for option in BankOptions:
        print(f"[{option.value}] {option.name}")
    while True:
        bank_choice = input("Please enter ur choice") 
        try:
            if bank_choice == BankOptions.DEPOSIT.name or int(bank_choice) == BankOptions.DEPOSIT.value:
                BankDeposit.deposit()
            elif bank_choice == BankOptions.WITHDRAW.name or int(bank_choice) == BankOptions.WITHDRAW.value:
                BankWithdraw.withdraw()   
            elif bank_choice == BankOptions.BALANCE.name or int(bank_choice) == BankOptions.BALANCE.value:
                BankBalance.bank_balance()
            elif bank_choice == BankOptions.POCKET.name or int(bank_choice) == BankOptions.POCKET.value:
                BankPocket.pocket_balance()
        except ValueError:
            if bank_choice == "Q":
                break
            else:
                print("You cannot enter a letters except [Q]")

