# 4 digit ph num
# 1st digit = 8 or 9
# 2nd and 3rd digits are the same between 0 and 9
# 4th digit = 8 or 9

num_1 = int(input('digit 1:'))
num_2 = int(input('digit 2:'))
num_3 = int(input('digit 3:'))
num_4 = int(input('digit 4:'))

# conditional logic formation
if num_1 in [8,9] and num_4 in [8,9] and num_3 in list(range(10)) and num_3 in list(range(10)):
    print('ignore the call')
else:
    print('answer the call')

# improving the code logic
if (num_1 ==8 or num_1==9) and (num_4 ==8 or num_4==9) and num_3==num_2:
    print('ignore the call')
else:
    print('answer the call')

# catching multiple number and negative integers edge cases
inputs = [num_1, num_2, num_3, num_4]
if any(not isinstance(n,int) or n<0 or n>9 for n in inputs):
    print('Invalid input: nums must be in single digit and non-negative ints')
else:
    if num_1 in [8,9] and num_4 in [8,9] and num_3 in list(range(10)) and num_3==num_2:
        print('ignore the call')
    else:
        print('answer the call')

# function to decide whether to answer the call or not
def answer_or_ignore_call(num_1, num_2, num_3, num_4):
    inputs = [num_1, num_2, num_3, num_4]
    if any(not isinstance(n,int) or n<0 or n>9 for n in inputs):
        print('Invalid input: nums must be in single digit and non-negative ints')
    else:
        if num_1 in [8,9] and num_4 in [8,9] and num_3 in list(range(10)) and num_3==num_2:
            print('ignore the call')
        else:
            print('answer the call')

# calling the fn
answer_or_ignore_call(num_1, num_2, num_3, num_4)


# testing mutiple test conditions
print()
print('testing:')
answer_or_ignore_call(0,1,2,3)
answer_or_ignore_call(0,1,2,0)
answer_or_ignore_call(8,1,2,8)
print()
answer_or_ignore_call(-8,1,1,-9)
answer_or_ignore_call(8,1,10,9)
answer_or_ignore_call(9,'a','a',8)
answer_or_ignore_call(9,0.6,0,8)
print()
answer_or_ignore_call(8,5,5,9)
answer_or_ignore_call(9,0,0,9)
answer_or_ignore_call(9,0,0,8)

