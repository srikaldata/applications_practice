# input:
# num succ 3 pt apples
# num succ 2 pt apples
# num succ 1 pt apples
# num succ 3 pt bananas
# num succ 2 pt bananas
# num succ 1 pt bananas

# output:
# A or B or T for tie


# get the inputs
app_3 = int(input('apple 3 pointers count:'))
app_2 = int(input('apple 2 pointers count:'))
app_1 = int(input('apple 1 pointers count:'))

ban_3 = int(input('banana 3 pointers count:'))
ban_2 = int(input('banana 2 pointers count:'))
ban_1 = int(input('banana 1 pointers count:'))

# calculate total pts
app_total = app_3 * 3 + app_2 * 2 + app_1 * 1
ban_total = ban_3 * 3 + ban_2 * 2 + ban_1 * 1

# determining the winner
if app_total > ban_total:
    print('A')
elif app_total < ban_total:
    print('B')
else:
    print('T')

# converting the code into a funtion
def find_the_winner(app_3,app_2,app_1,ban_3,ban_2,ban_1):
    
    # calculate total pts
    app_total = app_3 * 3 + app_2 * 2 + app_1 * 1
    ban_total = ban_3 * 3 + ban_2 * 2 + ban_1 * 1

    # determining the winner
    if app_total > ban_total:
        return 'A'
    elif app_total < ban_total:
        return 'B'
    else:
        return 'T'

#  test the fn
print(find_the_winner('A',app_2,app_1,ban_3,ban_2,ban_1))
print(find_the_winner(1,1,1,1,1,1))
print(find_the_winner(1,1,1,1,1,0.6))
print(find_the_winner(app_3,app_2,app_1,ban_3,ban_2,ban_1))
