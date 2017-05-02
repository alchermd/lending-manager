''' Account module used for creating accounts. '''

class Account:
    ''' Class used for Account objects. '''
    balance = 0
    def __init__(self, name, base_amount, start_date, interest):
        self.name = name
        self.base_amount = base_amount
        self.start_date = start_date
        self.interest = interest


    def show_info(self):
        ''' Prints the account information. '''
        print("Account: {}".format(self.name))
        print("Borrowed {} for {}% at {}.".format(self.base_amount, self.interest, self.start_date))
