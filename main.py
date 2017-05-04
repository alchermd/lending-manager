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
    os.system("clear")

    # Greet the user.
    print("Good day! Welcome to our lending company!")
    clear_delay(1.5)

    # Prompt the user if they are a new customer.
    print("Are you a returning customer? (Y/N) ", end='')
    customer_is_new = input().upper() == 'Y'
    clear_delay(1.5)

    # Ask for their name.
    print("What is your name? ", end='')
    name = input()
    clear_delay(1.5)

    if customer_is_new:
        print("Let's open your first account, {}".format(name))
        clear_delay(1.5)
    else:
        print("Welcome back, {}".format(name))
        clear_delay(1.5)

main()
