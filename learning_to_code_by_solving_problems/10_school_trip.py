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
    student_proportions_yrs = input('student proportions in each of 4 years (separate each using a space): ').split()
    num_students=int(input('number of students: '))
    
    # converting list of strings to list of floats
    for prop_idx in range(len(student_proportions_yrs)):
        student_proportions_yrs[prop_idx] = float(student_proportions_yrs[prop_idx])
    
    print(trip_cost, student_proportions_yrs, num_students, sep='\n\n')
    
    # calculating the num of students in each year using proportion
    students_yrs = []
    
    for prop in student_proportions_yrs:
        students_yrs.append(int(prop*num_students))
        

