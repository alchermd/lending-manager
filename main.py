#!/usr/bin/python3.5
''' Main program '''

import os
import time
from datetime import date
from modules.Borrower import Borrower

def clear_delay(secs):
    ''' Delays execution of the program and then clears the screen afterwards. '''
    time.sleep(secs)
    os.system("clear")


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

    if customer_is_new:
        database[name] = Borrower(name)
        print("You are now registered to our services, {}".format(name))
        clear_delay(2)
    else:
        print("Welcome back, {}".format(name))
        clear_delay(1)

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
            amt = int(input())
            clear_delay(1)

            # Ask for a confirmation.
            print("A 5% interest rate will be applied weekly on this account.")
            print("Enter \"YES\" to confirm: ", end='')
            agree = input().upper() == "YES"
            clear_delay(1)

            if agree:
                database[name].open_account(amt, date.today(), 5)
                print("Account created! Summary: ")
                database[name].show_credits(-1)
                clear_delay(5)

            else:
                continue

    print("Thank you for using our services. See you soon!")

main()
