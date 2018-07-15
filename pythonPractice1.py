iimport datetime

class Employee:
    raise_amt = 1.04
    no_of_emp = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first+'.'+last+'@gmail.com'
        Employee.no_of_emp+=1
        
    #property decortaor allowing call a method as an attribute
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    
    #this is getter of fullname
    #this proprty name is further used by setter and deleter
    @property    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    #setter for fullname
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    
    #deleter for fullname    
    @fullname.deleter
    def fullname(self):
        print('Deleting name')
        self.first = None
        self.last = None
        
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
emp2.fullname = 'avdhesh tiwari'
emp3 = Employee.from_string('nikki-sharma-200000')
print(Employee.no_of_emp)
print(emp1.fullname)
print(emp2.fullname)
del emp2.fullname
print(emp2.fullname)
print(emp3.email)
emp2.set_raise_amt(1.06)
print(emp2.raise_amt)
my_day = datetime.date(2018,7,14)
print(Employee.is_working_day(my_day))
