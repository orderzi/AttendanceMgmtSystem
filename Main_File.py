from Utils import *
from Employee_Pack.Employee_Class import Employee
import pandas as pd

def create_dataframe():
    df = pd.DataFrame(columns=columns)
    return df

def welcome_page():
    action = int(input('Welcome to Attendance Management System ! :\n'
          '1. Add Employee Manually\n'
          '2. Add Employee from a file\n'))
    return action


def choose_action(action):
    if action == 1:
        pass
    elif action == 2:
        pass

def add_emp_man(df):
    emp = Employee(employee_id=int(input('Please enter your Employee_ID'))
                   ,name=str(input('Please enter your name')),
                   phone=input('Please enter your Phone number:'),
                   age=int(input('Please enter your age:')))
    emp = emp.add_emp_man(df)
    print(emp)
    return emp


df = create_dataframe()

welcome = welcome_page()
a = add_emp_man(df)











#create_emp_file()



