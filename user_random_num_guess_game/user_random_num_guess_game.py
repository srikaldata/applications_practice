# importing necessary module
import random
import sys

# constant for testing
MAX_ATTEMPTS = 10

# fn for welcome message
def welcome_message():
    print('Welcome to the number guessing game!')


# fn to generate a random num based on the difficulty level
def generate_random_num(user_difficulty_level):
    if user_difficulty_level == 1:
        num, max_attempts = random.randint(1, 50), 5
    
    elif user_difficulty_level == 2:
        num, max_attempts = random.randint(1, 100), 7
    
    elif user_difficulty_level == 3:
        num, max_attempts = random.randint(1, 1000), 10
    
    # default difficulty
    else:
        num, max_attempts = random.randint(1, 100), 7
    return num, max_attempts


# get the user input
def get_user_input():
    curr_user_ip = int(input('Enter your guess: '))
    return curr_user_ip
