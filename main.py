''' Main program '''

from datetime import date
from modules.Account import Account


def main():
    ''' Main function '''
    sample = Account("John Doe", 5000, date(2017, 5, 2), 5)
    sample.show_info()

main()
