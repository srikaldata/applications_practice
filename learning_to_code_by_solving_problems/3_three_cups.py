# 3 opaque cups
# A = swap left and middle
# B = swap middle and right
# C = swap left and right

# getting the ip and setting the initial values
swap_order = input()

position = 1

# looping through the swap order and classifying the outcome
for swap in swap_order:
    if position == 1 and swap == 'A':
        position=2
    if position == 1 and swap == 'C':
        position=3
    if  position == 2 and swap == 'A':
        position=1
    if  position == 2 and swap == 'B':
        position=3
    if  position == 3 and swap == 'B':
        position=2
    if  position == 3 and swap == 'C':
        position=1

# print the final position
print(position)

# function to perform the swap cups trick
def swap_cups_trick(swap_order, position):
    for swap in swap_order:
        if position == 1 and swap == 'A':
            position=2
        if position == 1 and swap == 'C':
            position=3
        if  position == 2 and swap == 'A':
            position=1
        if  position == 2 and swap == 'B':
            position=3
        if  position == 3 and swap == 'B':
            position=2
        if  position == 3 and swap == 'C':
            position=1
    return position

# checking if the input is a string and one of abc
def swap_cups_trick(swap_order, position):
    # validation
    if not isinstance(swap_order, str) or not set(swap_order).issubset({'A', 'B', 'C'}):
        print("Please provide a valid string containing only 'A', 'B', and 'C'.")
        return None
    
    # conditional classification to find final position
    else:
        for swap in swap_order:
            if position == 1 and swap == 'A':
                position=2
            if position == 1 and swap == 'C':
                position=3
            if  position == 2 and swap == 'A':
                position=1
            if  position == 2 and swap == 'B':
                position=3
            if  position == 3 and swap == 'B':
                position=2
            if  position == 3 and swap == 'C':
                position=1
        return position
