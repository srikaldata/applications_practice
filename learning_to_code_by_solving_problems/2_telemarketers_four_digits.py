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
    print('Invalid input: nums must be in single digit, non-negative ints')
else:
    if num_1 in [8,9] and num_4 in [8,9] and num_3 in list(range(10)) and num_3==num_2:
        print('ignore the call')
    else:
        print('answer the call')
