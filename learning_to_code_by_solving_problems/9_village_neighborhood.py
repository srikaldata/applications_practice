# find the size of the smallest neghborhood

# input
# num of villages 3 to 100
# village positions for all subsequent inputs

# output
# size of the smallext neighborhood with 1 digit after decimal pt

num_villages = int(input('num of villages:'))
village_positions = []

for _ in range(num_villages):
    village_positions.append(int(input('position of the village:')))

# sorting from small to large
village_positions.sort()

# initializing village size
min_village_size = float(1000000000)
