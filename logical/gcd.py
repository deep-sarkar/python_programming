'''
gcd : gcd of 12 and 16 is 4
'''

def calculateGCD(num1, num2):
    gcd = 1
    try:
        # Check for smaller number
        if num1 > num2:
            smaller = num2
        else:
            smaller = num1
        if smaller > 0:
            # loop upto smaller number
            for num in range(2, smaller + 1):
                # If reminder is 0 for both number, then consider that number as gcd
                if (num1 % num == 0) and (num2 % num == 0):
                    gcd = num
            return gcd
        return "Enter positive integer value"
    except TypeError:
        return "Enter integer values"


gcd = calculateGCD("14",28)
print(gcd)