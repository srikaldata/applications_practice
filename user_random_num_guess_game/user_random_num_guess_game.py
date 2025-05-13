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


# get the difficulty level from the user
def get_difficulty_level():
    print('''Choose difficulty level: \n
          1: Easy: guess between 1 and 50 \n
          2: Medium: guess between 1 and 100 \n
          3: Hard: guess between 1 and 1000                
          ''')
    user_difficulty_level = int(input('Enter your preferred difficulty level: '))
    return user_difficulty_level


# getting user choice to replay the game or not
def game_replay_user_ip():
    user_choice = input('Do you want to replay the game? [yes/no]: ')
    if user_choice == 'yes':
        main()
    else:
        print('Thanks for playing the game. See you again!')


# playing the game
def play(random_num, max_attempts):
    status = False
    attempts = 0
    
    while not status:
        
        # when number of attempts exceeds the max attempts made
        if attempts > max_attempts:
            print('You have exceeded MAXIMUM NUM OF ATTEMPTS. Replay the game!')
            game_replay_user_ip()
            break
        
        attempts += 1
        user_ip = get_user_input()
        status = compare_ip_randnum(user_ip, random_num)
        
        # when the answer is found leaderboard is generated
        if status == True:
            save_leaderboard(attempts)


# saving the score to leaderboard
def save_leaderboard(num_attempts):
    name = input('Please enter your name for leaderboard: ')
    with open('guess_game_leaderboard.txt', 'a') as file:
        file.write(f'{name}||{1000 - ((num_attempts-1)*100)}\n')
    print('score successfully added to leaderboard')


# printing the leaderboard in the console
def list_leaderboard():
    with open('guess_game_leaderboard.txt', 'a') as file:
        winners = file.readlines()
    result = {}
    for person in winners:
        name, score = person.split('||')
        print(name, score)
