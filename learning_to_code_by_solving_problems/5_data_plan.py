# data plan with monthly carryover. find total data available currently

# inputs: 
# x --> data in MB per month
# n --> number of months 
# set of lines with data usage per month in MB for each of the n months

# output:
# data in MB remaining and available for next month

# fetching the inputs
monthly_data_mb = int(input('monthly data in MB: '))
num_months = int(input('number of months: '))

# initializing the final data remaining
remaining_data = 0

# looping through the num of months to get the data used in each month
for _ in range(num_months):
    used_data = int(input('data used this month in MB: '))
