''' Account module used for creating accounts. '''

import datetime

class Account:
    ''' Class used for Account objects. '''
    balance = 0
    interest = 0

    def __init__(self, name, base_amount, start_date, int_rate):
        self.name = name
        self.base_amount = base_amount
        self.start_date = start_date
        self.int_rate = int_rate * 0.01
        self.update_balance()

    def show_info(self):
        ''' Prints the account information. '''
        # Update the balance to ensure accurate data
        self.update_balance()

        print("Account: {}".format(self.name))
        print("Opened: {}".format(self.start_date))
        print("Statement: {} for {}% interest rate weekly.".format(self.base_amount, self.int_rate))
        print("Interest: {}".format(self.interest))
        print("Current balance: {}".format(self.balance))

    def update_balance(self):
        ''' Calculates the balance of the account.

            interest = base amount X interest rate x weeks due
            balance = base amount + interest
        '''
        weeks_due = (datetime.date.today() - self.start_date).days // 7
        self.interest = self.base_amount * self.int_rate * weeks_due
        self.balance = self.base_amount + self.interest
