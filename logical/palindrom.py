'''
palindrom : 101, 12021 ( reverse == num)
'''


def list_num(num):
    reverse =  ''
    while num != 0:
        reminder = num %10
        reverse += str(reminder)
        num = num //10
    return reverse


def isPalindrom(num):
    try:
        reverse_num = list_num(num)
        if int(reverse_num) == num:
            return True
        return False
    except TypeError:
        return "Enter a numerical value"

print(isPalindrom(2012102))


