import datetime

class Employee:
    raise_amt = 1.04
    no_of_emp = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'
        Employee.no_of_emp+=1
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
        
    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
print(Employee.no_of_emp)
emp1 = Employee('khushboo','tiwari',20000)
emp2 = Employee('ajay','sharma',200000)
emp3 = Employee.from_string('nikki-sharma-200000')
print(Employee.no_of_emp)
print(emp1.email)
print(emp3.email)
emp2.set_raise_amt(1.06)
print(emp2.raise_amt)
my_day = datetime.date(2018,7,14)
print(Employee.is_working_day(my_day))
