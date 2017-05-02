''' Account module used for creating accounts. '''

import datetime

class Account:
    ''' Class used for Account objects. '''
    balance = 0
    def __init__(self, name, base_amount, start_date, interest):
        self.name = name
        self.base_amount = base_amount
        self.start_date = start_date
        self.interest = interest * 0.01
        self.update_balance()

    def show_info(self):
        ''' Prints the account information. '''
        # Update the balance to ensure accurate data
        self.update_balance()

        print("Account: {}".format(self.name))
        print("Borrowed {} for {}% interest at {}.".format(self.base_amount, self.interest, self.start_date))
        print("Current balance: {}".format(self.balance))

    def update_balance(self):
        ''' Calculates the balance of the account. '''
        weeks_due = (datetime.date.today() - self.start_date).days // 7
        self.balance = self.base_amount * self.interest * weeks_due
