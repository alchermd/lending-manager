''' Main program '''

from datetime import date
from modules.Account import Account


def main():
    ''' Main function '''
    # Create an account for 5000
    sample = Account("John Doe", 5000, date(2017, 3, 30), 5)
    sample.show_info()

    # Pay 5000 to base amount + interest
    sample.pay(5000)
    print()
    sample.show_info()

main()
