''' Borrower module used for creating borrower objects. '''
from modules.Account import Account

class Borrower:
    ''' Borrower class creates a borrower object that can hold multiple accounts. '''
    accounts = []

    def __init__(self, name, credit_status=True):
        self.name = name
        self.credit_status = credit_status

    def open_account(self, base_amount, start_date, int_rate):
        ''' Adds an account object to the borrower's accounts list. '''
        if self.credit_status:
            self.accounts.append(Account(self.name, base_amount, start_date, int_rate))
        else:
            print("Bad credit status")

    def show_credits(self, index=None):
        ''' Shows the account information of the given index.
            Shows an error message if no accounts are opened.
            Shows all the accounts otherwise.
        '''
        if index is None:
            for account in self.accounts:
                print("-" * 10)
                print("ID: {}".format(self.accounts.index(account)))
                account.show_info()
        elif not self.accounts:
            print("No accounts opened")
        else:
            print("-" * 10)
            print("ID: {}".format(self.accounts.index(self.accounts[-1])))
            self.accounts[index].show_info()

    def pay(self, index, amount):
        ''' Pays an amount to the account at index. '''
        self.accounts[index].pay(amount)
        