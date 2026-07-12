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
    print('remaining_data from previous month:', remaining_data, 'MB')
    used_data = int(input('data used this month in MB: '))
    
    # making sure if the used data doesnt exceed remaining data 
    if used_data < (monthly_data_mb+remaining_data): 
        remaining_data = monthly_data_mb + remaining_data - used_data
        print('remaining data:', remaining_data, 'MB')
    else:
        print('ERROR: used data cannot exceed remaining data')
        break

print('Final remaining_data:', remaining_data)

# enclosing everything within a function 
def data_plan(monthly_data_mb, num_months):
    for _ in range(num_months):
        print('remaining_data from previous month:', remaining_data, 'MB')
        used_data = int(input('data used this month in MB: '))
        
        # making sure if the used data doesnt exceed remaining data 
        if used_data < (monthly_data_mb+remaining_data): 
            remaining_data = monthly_data_mb + remaining_data - used_data
            print('remaining data:', remaining_data, 'MB')
        else:
            print('ERROR: used data cannot exceed remaining data')
            break

    print('Final remaining_data:', remaining_data)

# testing the function with different inputs
data_plan(20, 5)
data_plan(200, 3)
data_plan(100, 9)

# another logic to calculate data plan
# calculate total available data first
total_available_data = (num_months+1) * monthly_data_mb
