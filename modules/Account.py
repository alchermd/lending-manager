''' Account module used for creating accounts. '''

import datetime

class Account:
    ''' Class used for Account objects. '''
    balance = 0
    interest = 0
    og_amount = 0

    def __init__(self, name, base_amount, start_date, int_rate):
        self.name = name
        self.og_amount = self.base_amount = base_amount
        self.start_date = start_date
        self.int_rate = int_rate * 0.01

        self.update_interest()
        self.update_balance()

    def show_info(self):
        ''' Prints the account information. '''
        print("Account: {}".format(self.name))
        print("Opened: {}".format(self.start_date))
        print("Statement: {} for {}% interest rate weekly.".format(self.og_amount, self.int_rate))
        print("Interest: {}".format(self.interest))
        print("Current balance: {}".format(self.balance))

    def update_balance(self):
        ''' Calculates the balance of the account. '''
        self.balance = self.base_amount + self.interest

    def update_interest(self):
        ''' Calculates and updated the interest of the account. '''
        weeks_due = (datetime.date.today() - self.start_date).days // 7
        self.interest = self.base_amount * self.int_rate * weeks_due

    def pay(self, amount):
        ''' Reduces the account balance by amount an amount '''
        if amount > self.interest:
            self.interest, overflow = 0, self.interest - amount
            self.base_amount += overflow
        else:
            self.interest -= amount

        self.update_balance()
        