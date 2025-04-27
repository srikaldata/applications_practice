
# defining a function to get operator
def get_operator():
    print("""Welcome to the operator
          Select the operation: 
          [1] addition
          [2] subtraction
          [3] multiplication
          [4] division
          [5] modulus
          [6] power""")
    
    operator = input('choose the respective number of the operation to perform (press "q" to quit): ')
    
    return operator


# fetching the operands from user input
def get_operands():
    num1 = float(input('Enter the val of the first number: '))
    num2 = float(input('Enter the val of the second number: '))
    return num1, num2


# individual operation functions
def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    return num1/num2

def modulus(num1, num2):
    return num1%num2

def power(num1, num2):
    return num1**num2


# performing the calculation
def perform_calculation(op, num1, num2):
    
    # q to quit
    if op == 'q':
        return None
    
    # addition
    elif int(op) == 1:
        return addition(num1, num2)
    
    # subtraction
    elif int(op) == 2:
        return subtraction(num1, num2)
    
    # multiplication
    elif int(op) == 3:
        return multiplication(num1, num2)
    
    # division
    elif int(op) == 4:
        return division(num1, num2)
    
    # modulus
    elif int(op) == 5:
        return modulus(num1, num2)
    
    # power
    elif int(op) == 6:
        return power(num1, num2)
    
    

# main function for the basic calc
def basic_calculator():
    while True:
            
        try:
            # fetching the type of operation to perform from user i/p
            op = get_operator()

            # if the use chose to quit
            if op == 'q':
                print('exiting calculator...')
                break
            
            elif op != 'q' and op not in [1,2,3,4,5,6]:
                print('please enter a valid option to perform a listed operation or to quit')
                continue
            
            # fetching operands
            num1, num2 = get_operands()
            
            # performing the calculation
            result = perform_calculation(op, num1, num2)
            
            # display the result in stdout 
            print('The result of the calculation is: ', result)
