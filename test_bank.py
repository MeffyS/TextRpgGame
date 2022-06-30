from game_character import player_backpack
from enum import Enum, auto

class BankOptions(Enum):
    DEPOSIT = auto()
    WITHDRAW = auto()
    BALANCE = auto()
    POCKET = auto()
    QUIT = 'Q'


class BankWithdraw:

    def withdraw():
        print(f"You choosed option WITHDRAW")
        withdraw = input(f"How many coins you want withdrawn?")
        if int(withdraw) > BankBalance.balance:
            print(f"You dont have {int(withdraw)} in bank. In Your bank balance you got {BankBalance.balance}")
        elif int(withdraw) == 0:
            print(f"You cannot withdrawn 0 coins")




    pass

class BankDeposit:
    pass

class BankBalance:
    balance = 0
    print(f"Dear player, your total bank balance is {balance} coins")


class BankPocket:
    print(f"Dear player, your total pocket balance is {player_backpack.coins} coins")


class Bank:
    for option in BankOptions:
        print(f"[{option.value}] {option.name}")
    bank_choice = input("Please enter ur choice") 
    if bank_choice == BankOptions.DEPOSIT.name or int(bank_choice) == BankOptions.DEPOSIT.value:
        print("DEPOST")
        pass
    elif bank_choice == BankOptions.WITHDRAW.name or int(bank_choice) == BankOptions.WITHDRAW.value:
        BankWithdraw.withdraw()

    elif bank_choice == BankOptions.BALANCE.name or int(bank_choice) == BankOptions.BALANCE.value:
        pass
    elif bank_choice == BankOptions.POCKET.name or int(bank_choice) == BankOptions.POCKET.value:
        pass
    elif bank_choice == BankOptions.QUIT.name or int(bank_choice) == BankOptions.QUIT.value:
        pass

bank_withdraw = BankWithdraw()
bank_balance = BankBalance()

