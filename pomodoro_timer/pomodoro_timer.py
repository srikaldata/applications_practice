# importing packages
import time
import os
from plyer import notification

# import requests 
# ntfy.sh (pub sub)


# default settings
DEFAULT_POMODORO_TIMER_MINS = 25
DEFAULT_SHORT_BREAK_TIME_MINS = 5
DEFAULT_LONG_BREAK_TIME_MINS = 5
DEFAULT_CYCLES_FOR_LONG_BREAK = 3


# function to clear the terminal window
def clear_window():
    os.system('cls')

