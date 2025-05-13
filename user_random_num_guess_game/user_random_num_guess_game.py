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


# compare the user input and the random number generated
def compare_ip_randnum(user_ip, random_num):
    
    status = False
    
    # if the number guessed is higher than target
    if user_ip > random_num:
        print('Your guess is HIGHER!')
    
    # if the number guessed is lower than target
    elif user_ip < random_num:
        print('Your guess is LOWER!')
        
    # when the number guessed is correct
    elif user_ip == random_num:
        print('You have correctly guessed. YOU WIN!')
        status = True
    
    return status
