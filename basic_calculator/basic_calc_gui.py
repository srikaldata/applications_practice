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
root_gui.title('Basic calculator with 6 operations')
 