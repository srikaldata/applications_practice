# importing packages for gui
import tkinter as tk
from tkinter import messagebox


# individual operation functions
def addition(num1, num2):
    return num1+num2

def subtraction(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError('Cannot divide by zero!')
    else:
        return num1/num2

def modulus(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2


# the main function to calculate and perform the operation
def perform_calculation():
    
    num1 = float(usr_input_num1.get())
    num2 = float(usr_input_num2.get())
    op = operation_selected.get()
        
    # addition
    if int(op) == 'Addition':
        result = addition(num1, num2)
    
    # subtraction
    elif int(op) == 'Subtraction':
        result = subtraction(num1, num2)
    
    # multiplication
    elif int(op) == 'Multiplication':
        result = multiplication(num1, num2)
    
    # division
    elif int(op) == 'Division':
        result = division(num1, num2)
    
    # modulus
    elif int(op) == 'Modulus':
        result = modulus(num1, num2)
    
    # power
    elif int(op) == 'Power':
        result = power(num1, num2)
    
    # if none of the above 
    else:
        result = 'Please select a valid operation!'

    # method to display the result post calc
    label_result.config(text=f'Result: {result}')
    
        

# creating the GUI

# instantiating the tk class
root_gui = tk.Tk()
root_gui.title('Basic calculator with 6 operations and 2 operands')

# the input section for operands
# type of gui element for 1st operand
usr_input_num1 = tk.Entry(root_gui)
# position of the 1st operand input element in the gui 
usr_input_num1.grid(row=0, column=1, pady=8)

# type of gui element for 2nd operand
usr_input_num2 = tk.Entry(root_gui)
# position of the 1st operand input element in the gui 
usr_input_num2.grid(row=1, column=1, pady=8)

# user choosing the operation to be performed
tk.Label(root, text='Select operation: ').grid(row=2, column=0, pady=8)
operation_selected = tk.StringVar(root_gui)
# setting the default operation to be performed
operation_selected.set('Addition') 
# listing the set of operations to select from
operations_list = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Modulus', 'Power']
# creating a dropdown menu for letting the user choose the operation
operation_selected_ddmenu = tk.OptionMenu(root_gui, operation_selected, *operations_list)
operation_selected_ddmenu.grid(row=2, column=1, pady=8)

# calculate button
calculate_btn = tk.Button(text='CALCULATE', command=perform_calculation)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=12)

# displaying the result
label_result = tk.Label(root_gui, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, pady=8)
