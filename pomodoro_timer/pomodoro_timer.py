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


# the pomodoro timer major function 
def pomodoro_timer(tasks):
    
    cycles = 1
    task_counter = 0
    
    # keep repeating
    while cycles <= len(tasks):
        clear_window()
        print(f'***Pomodoro Session for {tasks[task_counter]} Started***')
        countdown_timer(DEFAULT_POMODORO_TIMER_MINS)
        
        # short break condition
        if cycles < DEFAULT_CYCLES_FOR_LONG_BREAK:
            clear_window()
            notify('***SHORT break started***')
            print('***SHORT break started***')
            countdown_timer(DEFAULT_SHORT_BREAK_TIME_MINS)
            task_counter += 1
        
        # long break condition
        else:
            clear_window()
            notify('***LONG break started***')
            print('***LONG break started***')
            countdown_timer(DEFAULT_LONG_BREAK_TIME_MINS)
            task_counter += 1
            
        cycles += 1
    

# fn to get task 
def get_tasks():
    is_task = True
    tasks = []
    
    while is_task:
            
        task = input('Enter you task name: ')
        tasks.append(task)
        
        any_more_task = input('Do you wish to add more tasks? (yes / no): ')
        
        if any_more_task.strip().lower() in ['no', 'n']:
            is_task = False
    
    return tasks
            
