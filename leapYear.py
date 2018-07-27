#leap year 
def checkLeapYear(year):
    if (((year %4 == 0) and (year % 100!=0)) or year %400 ==0):
        print("leap year")
    else:
        print("not leap year")
        
y=1900
y=2012
checkLeapYear(y)
