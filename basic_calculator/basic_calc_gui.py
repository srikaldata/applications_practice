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
