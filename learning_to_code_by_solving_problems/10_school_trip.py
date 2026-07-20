# school trip brunch based funding

# inputs:
# cost in dollars of school trip
# proportion of students at brunch 1st year, 2nd year, 3rd year, 4th year
# num of students attending the brunch

# output:
# if students need to raise money --> YES. if not --> NO

# setting the constant
cost_per_student_diff_yrs = [12, 10, 7, 5]


# getting the inputs
for _ in range(10):
    trip_cost = int(input('cost of the trip in $: '))
    student_proportions_yrs = [float(x) for x in input('student proportions in each of 4 years (separate each using a space) (MUST TOTAL TO 1.0): ').split()]
    num_students=int(input('number of students: '))
    # if cost per student needs to be varied for each iteration 
    cost_per_student_diff_yrs = [int(x) for x in input('brunch cost per student in each of 4 years (separate each using a space): ').split()]
   
   # converting list of strings to list of floats
    for prop_idx in range(len(student_proportions_yrs)):
        student_proportions_yrs[prop_idx] = float(student_proportions_yrs[prop_idx])
    
    print(trip_cost, student_proportions_yrs, num_students, sep='\n\n')
    
    # calculating the num of students in each year using proportion
    students_each_yr = []
    
    for prop in student_proportions_yrs:
        students_each_yr.append(int(prop*num_students))
        
    # calculating the total amount raised from brunch 
    total_amt_raised = 0
    for idx in range(len(students_each_yr)):
        total_amt_raised= total_amt_raised + (students_each_yr[idx] * cost_per_student_diff_yrs[idx])
        
    print('total amount raised: ', total_amt_raised)
    
    # finding if it would cover the trip cost
    if total_amt_raised/2 < trip_cost:
        print('YES')
    else:
        print('NO') 
    

# wrapping the logic into functions
def get_inputs():
    trip_cost = int(input('cost of the trip in $: '))
    student_proportions_yrs = [float(x) for x in input('student proportions in each of 4 years (separate each using a space) (MUST TOTAL TO 1.0): ').split()]
    num_students=int(input('number of students: '))
    # if cost per student needs to be varied for each iteration 
    cost_per_student_diff_yrs = [int(x) for x in input('brunch cost per student in each of 4 years (separate each using a space): ').split()]
    
    return trip_cost , student_proportions_yrs, num_students, cost_per_student_diff_yrs

def will_amt_cover_trip(trip_cost , student_proportions_yrs, num_students, cost_per_student_diff_yrs):
    # converting list of strings to list of floats
    for prop_idx in range(len(student_proportions_yrs)):
        student_proportions_yrs[prop_idx] = float(student_proportions_yrs[prop_idx])
    
    print(trip_cost, student_proportions_yrs, num_students, sep='\n\n')
    
    # calculating the num of students in each year using proportion
    students_each_yr = []
    
    for prop in student_proportions_yrs:
        students_each_yr.append(int(prop*num_students))
        
    # calculating the total amount raised from brunch 
    total_amt_raised = 0
    for idx in range(len(students_each_yr)):
        total_amt_raised= total_amt_raised + (students_each_yr[idx] * cost_per_student_diff_yrs[idx])
        
    print('total amount raised: ', total_amt_raised)
    
    # finding if it would cover the trip cost
    if total_amt_raised/2 < trip_cost:
        print('YES')
    else:
        print('NO')

print(get_inputs())
print(will_amt_cover_trip(*get_inputs()))


# second way to solve the problem
# getting the inputs
for _ in range(10):
    trip_cost = int(input('cost of the trip in $: '))
    student_proportions_yrs = [float(x) for x in input('student proportions in each of 4 years (separate each using a space) (MUST TOTAL TO 1.0): ').split()]
    num_students=int(input('number of students: '))
    # if cost per student needs to be varied for each iteration 
    cost_per_student_diff_yrs = [int(x) for x in input('brunch cost per student in each of 4 years (separate each using a space): ').split()]
    
    # calculating the num of students in each year using proportion
    students_each_yr = []
    
    for prop in student_proportions_yrs:
        students_each_yr.append(int(prop*num_students))
    
    counted_students = sum(students_each_yr)
    uncounted_students = num_students - counted_students
    max_students_yr_idx = students_each_yr.index(max(students_each_yr))
    