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
    
    print('calculating min village size...')

    # calculating the minimum size of each village
    for i in range(1, num_villages-1):
        left_limit = (village_positions[i]-village_positions[i-1])/2
        right_limit= (village_positions[i+1]-village_positions[i])/2
        
        village_size = left_limit + right_limit
        
        # updating previous minimum village size
        if village_size < min_village_size:
            min_village_size=village_size

    print(min_village_size)
    print()

# testing the function with different use cases
calc_min_village_size(5, [1,2,3,4,5])
calc_min_village_size(2, [10,20])
calc_min_village_size(2, [100000000,199999999])
calc_min_village_size(3, [9,9999, 99999999])
calc_min_village_size(5, [1, 10, 100, 1000, 10000])
calc_min_village_size(12, [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009, 1000010, 1000011])
