#!/usr/bin/python3.5
''' Main program '''

import os
import sys
from datetime import date
from modules.Borrower import Borrower
from modules.helpers import clear_delay, press_enter


def main():
    ''' The main function that allows the user to interact with the rest of the program. '''
    # Setup
    os.system("clear")
    database = {}

    # Greet the user.
    print("Good day! Welcome to our lending company!")
    clear_delay(1)

    # Prompt the user if they are a new customer.
    print("Are you a new customer? (Y/N) ", end='')
    customer_is_new = input().upper() == 'Y'
    clear_delay(1)

    # Ask for their name.
    print("What is your name? ", end='')
    name = input()
    clear_delay(1)

    # Name validation.
    if customer_is_new and name not in database:
        database[name] = Borrower(name)
        print("You are now registered to our services, {}.".format(name))
        clear_delay(2)
    elif not customer_is_new and name in database:
        print("Welcome back, {}".format(name))
        clear_delay(1)
    else:
        print("Cannot access account.")
        clear_delay(1)
        sys.exit()

    # Interface loop.
    choice = None
    while choice != 'Q':
        print("How may we help you?")
        print("[0]: Create a new account on my name.")
        print("[1]: Check accounts under my name.")
        print("[2]: Pay an existing account.")
        print("[Q]: Exit the program.")
        print("\nI want to: ", end='')

        choice = input().upper()
        clear_delay(1)

        # Account creation.
        if choice == '0':
            # Prompt for amount.
            print("How much will you borrow?")
            print("Amount: ", end='')
            amt = input()
            clear_delay(1)

            # Validate amount.
            if not amt.isdigit():
                print("Invalid value.")
                clear_delay(2)
                continue
            amt = float(amt)

            # Ask for a confirmation.
            print("A 5% interest rate will be applied weekly on this account.")
            print("Enter \"YES\" to confirm: ", end='')
            agree = input().upper() == "YES"
            clear_delay(1)

            if agree:
                database[name].open_account(amt, date.today(), 5)
                print("Account created! Summary: ")
                database[name].show_credits(-1)
                press_enter()

            else:
                continue

        # Check accounts.
        elif choice == '1':
            # Check if the user has no existing accounts.
            if not database[name].accounts:
                print("You have no accounts under your name.")
                clear_delay(2)

            else:
                print("Enter account id (leave blank to show all acounts): ", end='')
                acc_id = input()

                if acc_id == "":
                    database[name].show_credits()
                else:
                    database[name].show_credits(int(acc_id))

                press_enter()

        # Pay account(s)
        elif choice == '2':
            # Check if the user has no existing accounts.
            if not database[name].accounts:
                print("You have no accounts under your name.")
                clear_delay(2)

            else:
                print("Here are your accounts:")
                database[name].show_credits()

                acc_id = int(press_enter("Enter account id to pay: "))

                # Validate acc_id
                if acc_id < 0 or acc_id >= len(database[name].accounts):
                    print("Invalid account id")
                    clear_delay(2)

                else:
                    # Make payment
                    print("Enter amount to pay: ", end='')
                    amt = int(input())
                    database[name].pay(acc_id, amt)
                    clear_delay(2)

                    # Show feedback
                    print("Payment succeeded!")
                    database[name].show_credits(acc_id)
                    press_enter()

    print("Thank you for using our services. See you soon!")

main()
