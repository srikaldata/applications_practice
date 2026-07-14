# how many times to play the slot machine before going broke

# input:
# num of quarters available
# num times the first slot machine has already played
# num times the second slot machine already played
# num times the third slot machine already played

# output:
# total tries before going broke

num_quarters = int(input('num of quarters available: '))
first_m_plays = int(input('num of previous plays in FIRST machine: '))
second_m_plays = int(input('num of previous plays in SECOND machine: '))
third_m_plays = int(input('num of previous plays in THIRD machine: '))

machine = 1
num_plays = 0

# looping through playing each machine for each quarter in a continuous loop until the person is broke
while num_quarters >= 1:
    num_quarters -= 1
    
    # when playing in the first machine:
    if machine == 1:
        first_m_plays +=1
        if first_m_plays == 35:
            num_quarters += 30
            first_m_plays=0
