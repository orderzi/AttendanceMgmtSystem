from Utils import *
from Employee_Pack.Employee_Class import Employee
import pandas as pd

def create_dataframe():
    df = pd.DataFrame(columns=columns)
    return df

def welcome_page(df):
    action = int(input('Welcome to Attendance Management System ! :\n'
          '1. Add Employee Manually\n'
          '2. Add Employee from a file\n'))
    if action == 1:
        add_user_man(df)
    elif action == 2:
        pass

def add_user_man(df):
    user = {}
    user['Employee_id'] = input('Please enter your Employee ID:')
    user['Name'] = input('Please enter your Name:')
    user['Phone'] = input('Please enter your Phone:')
    user['Age'] = int(input('Please enter your Age:'))
    df = df.append(user, ignore_index=True)
    print(df)
    return df


df = create_dataframe()
welcome = welcome_page(df)












#create_emp_file()



