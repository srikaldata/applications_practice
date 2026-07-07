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
app_3 = int(input())
app_2 = int(input())
app_1 = int(input())

ban_3 = int(input())
ban_2 = int(input())
ban_1 = int(input())

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
