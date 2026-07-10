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
