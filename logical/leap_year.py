'''
input : year
returns : true if leap year else false
'''

def isLeapYear(year):
    try:
        if year < 0:
            return "Enter a valid year"
        elif year % 400 == 0 or year % 4 == 0 and year%100 != 0:
            return True
        return False
    except TypeError:
        return "Enter a numerical value"

year = isLeapYear(2300)
print(year)
year = isLeapYear(2312)
print(year)
year = isLeapYear(2020)
print(year)
year = isLeapYear(2010)
print(year)