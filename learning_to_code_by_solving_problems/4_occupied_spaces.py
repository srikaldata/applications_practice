# number of parking spaces that were occupied on yesterday and today

# inputs:
# num of parking spaces
# yesterday pattern with . means empty spot, C means the car has occupied the space
# today's num of parking spots using . means empty spot, C means the car has occupied the space

# getting the inputs
num_spaces = int(input("num of spaces: "))
parking_pattern_both_days = input("today's parking pattern: ") + input("yesterday's parking pattern: ")

# looping through each patterns to find occupied spaces on both days
total_parked_count=0
for char in parking_pattern_both_days:
    if char == 'C':
        total_parked_count +=1
        
print(total_parked_count)

# finding out other ways to count
total_parked_count=0
print(parking_pattern_both_days.count('C'))

# function for the logic without list count method
def total_parked_spaces(num_spaces, parking_pattern_both_days):
    total_parked_count=0
    for char in parking_pattern_both_days:
        total_parked_count+=1
    return total_parked_count
