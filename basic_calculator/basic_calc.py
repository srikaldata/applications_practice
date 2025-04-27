
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


