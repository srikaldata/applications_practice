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

# calculating the minimum size of each village
for i in range(1, num_villages-1):
    left_limit = (village_positions[i]-village_positions[i-1])/2
    right_limit= (village_positions[i+1]-village_positions[i])/2
    
    village_size = left_limit + right_limit
    
    # updating previous minimum village size
    if village_size < min_village_size:
        min_village_size=village_size

print(min_village_size)

# wrapping up the logic within a function
def calc_min_village_size(num_villages, village_positions):
    # initializing village size
    min_village_size = float(1000000000)

    # calculating the minimum size of each village
    for i in range(1, num_villages-1):
        left_limit = (village_positions[i]-village_positions[i-1])/2
        right_limit= (village_positions[i+1]-village_positions[i])/2
        
        village_size = left_limit + right_limit
        
        # updating previous minimum village size
        if village_size < min_village_size:
            min_village_size=village_size

    print(min_village_size)
    