''' Utility functions '''

import os
import time

def clear_delay(secs):
    ''' Delays execution of the program and then clears the screen afterwards. '''
    time.sleep(secs)
    os.system("clear")

def press_enter(msg="Press enter to continue"):
    ''' Delays execution of the program and then clears the screen when enter is pressed.
        An optional msg can be passed as an argument to customize the output.
        The keyboard input is returned.
    '''
    print("-" * 10)
    print(msg, end='')
    output = input()
    os.system("clear")

    return output
