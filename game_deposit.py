from game_informations import GameAttributes
from enum import Enum
from game_clear_function import clearConsole


class BankFuncionality(Enum):
    deposit = 1
    withdraw = 2
    balance = 3
    pocket = 4


def money_deposit(coins):
    bank_money = 100

    if coins == 'BANK':
        while True:
            print("You use the services of the town's bank")
            deposit_withdraw_balance = input(
                f"You can deposit coins, withdraw coins or look your account balance.[withdraw][deposit][balance][pocket] ").upper()
            clearConsole()
            try:
                if deposit_withdraw_balance == BankFuncionality.deposit.name or deposit_withdraw_balance == str(BankFuncionality.deposit.value):
                    clearConsole()
                    deposit_sum = input("How many coins you want deposit? ")
                    clearConsole()
                    if deposit_sum == "Q":
                        continue
                    elif int(deposit_sum) == 0:
                        print("You cannot deposit 0 coins")
                    elif int(deposit_sum) < 0:
                        print("Deposit coins cannot have a negative value")
                    elif GameAttributes.Coins >= int(deposit_sum) and GameAttributes.Coins > 0:
                        if GameAttributes.Coins >= 100 or bank_money >= 100:
                            bank_money += (int(deposit_sum)-100)
                            GameAttributes.Coins -= (int(deposit_sum))
                            print(GameAttributes.Coins)
                            print(
                                '100 coins were taken for a payment to bank from the coins balance')
                            print(
                                f"Your account balance: {bank_money}")
                        else:
                            print(
                                f"You dont have coins to pay the deposit {GameAttributes.Coins}|100")

                    elif GameAttributes.Coins < int(deposit_sum):
                        print(f"You dont have a coins in ur pocket")
                        print(f'Coins Balance: {GameAttributes.Coins}')
                    else:
                        continue

                elif deposit_withdraw_balance == BankFuncionality.withdraw.name or deposit_withdraw_balance == str(BankFuncionality.withdraw.value):
                    clearConsole()
                    withdraw_sum = input("How many coins you want withdraw? ")
                    clearConsole()
                    if withdraw_sum == 'Q':
                        continue
                    elif int(withdraw_sum) == 0:
                        print("You cannot withdraw 0 coins")
                    elif int(withdraw_sum) < 0:
                        print("Withdraw coins cannot have a negative value")
                    elif int(withdraw_sum) <= bank_money and int(withdraw_sum) > 0:
                        if GameAttributes.Coins >= 100 or bank_money >= 100:
                            GameAttributes.Coins += (int(withdraw_sum)-100)
                            bank_money -= int(withdraw_sum)
                            print(
                                '100 coins were taken for a withdrawal from the bank')
                            print(
                                f"Your pocket balance: {GameAttributes.Coins}")
                        else:
                            print(
                                "You don't have coins to pay the withdrawal")
                    elif int(withdraw_sum) > bank_money:
                        print("You don't have that much coins in the bank")
                        print(f'Coins balace: {bank_money}')
                elif deposit_withdraw_balance == BankFuncionality.balance.name or deposit_withdraw_balance == str(BankFuncionality.balance.value):
                    print(f"In bank you have a {bank_money} coins")
                elif deposit_withdraw_balance == BankFuncionality.pocket.name or deposit_withdraw_balance == str(BankFuncionality.pocket.value):
                    print(f"In pocket you have a {GameAttributes.Coins} coins")
                elif deposit_withdraw_balance == "Q":
                    break
            except Exception:
                print("Incorrect value")
