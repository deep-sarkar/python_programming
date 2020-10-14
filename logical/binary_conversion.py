'''
4 = 100
5 = 101
'''

def getReminder(num):
    return num % 2

def toBinary(num):
    try:
        bin = ''
        while num != 0:
            reminder = getReminder(num)
            bin = str(reminder) + bin
            num = num // 2
        return int(bin)
    except TypeError as e:
        return "enter a numerical value"

print(toBinary('wad'))
print(toBinary(567))