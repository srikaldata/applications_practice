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


# fn for the countdown timer
def countdown_timer(minutes):
    total_seconds = minutes * 60
    total_seconds = 5
    
    while total_seconds:
        current_min = total_seconds // 60
        current_sec =  total_seconds % 60
        print(f'\rTime left: {current_min:02d}:{current_sec:02d}', end='')
        time.sleep(1)
        total_seconds -= 1


# system notification after the the timer ends  
def notify(msg):
    notification.notify(title = 'Pomodoro Timer', message = msg, timeout = 5)

