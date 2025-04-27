
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

