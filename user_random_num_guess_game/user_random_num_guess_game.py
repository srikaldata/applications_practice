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
def get_user_input(max_attempts):
    while True:
            
        try:
            curr_user_ip = int(input(f'Enter your guess: '))
            if max_attempts == 5 and (1 <= curr_user_ip <= 50):
                return curr_user_ip
            elif max_attempts == 7 and (1 <= curr_user_ip <= 100):
                return curr_user_ip
            elif max_attempts == 10 and (1 <= curr_user_ip <= 1000):
                return curr_user_ip
            else:
                map_values = lambda x: {5: 50, 7: 100, 10: 1000}.get(x, 0)
                print(f'Error: Please enter a number between 1 and {map_values(max_attempts)}.')
        except ValueError:
            print('Error: Please enter valid integer numbers')
        except TypeError:
            print('Error: Please enter an integer')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            


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
    
    while True:
        
        print('''Choose difficulty level: \n
            1: Easy: guess between 1 and 50 \n
            2: Medium: guess between 1 and 100 \n
            3: Hard: guess between 1 and 1000                
            ''')
        
        try:
            user_difficulty_level = int(input('Enter your preferred difficulty level: '))
            if user_difficulty_level in [1, 2, 3]:
                return user_difficulty_level
            else:
                print('Please enter 1, 2, or 3.')
        except ValueError:
            print('Invalid input. Please enter an integer: 1 or 2 or 3')

# getting user choice to replay the game or not
def game_replay_user_ip():
    user_choice = input('Do you want to replay the game? [yes/no]: ')
    if user_choice in ['yes', 'Yes', 'YES', 'y', 'Y'] :
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
        user_ip = get_user_input(max_attempts)
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


# main function that performs all the functions
def main():
    welcome_message()
    user_difficulty_level = get_difficulty_level()
    random_num, max_attempts = generate_random_num(user_difficulty_level)
    play(random_num, max_attempts)
    game_replay_user_ip()


# condition to whether play the game or to list the leaderboard
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        list_leaderboard()
    else:
        main()
        