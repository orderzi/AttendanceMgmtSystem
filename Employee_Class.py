class Employee:
    def __init__(self, employee_id, name, phone, age):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.age = age

    def add_emp_man(self,df):
        new_emp = {'Employee_id': self.employee_id, 'Name': self.name, 'Phone': self.phone, 'Age': self.age}
        df = df.append(new_emp, ignore_index=True)
        return df







