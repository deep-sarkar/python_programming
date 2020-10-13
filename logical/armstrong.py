


def count(num):
    counter = 0
    while num != 0:
        num //= 10
        counter += 1
    return counter


def power(digit, power):
    power_value = 1
    while power != 0:
        power_value *= digit
        power -= 1
    return power_value


def isArmstrong(num):
    if type(num) != int or num < 0:
        return "invalid input"
    initial_value = num
    sum = 0
    total_digit = count(num)
    while num != 0:
        digit = num %10
        num = num //10
        if digit != 0:
            power_value = power(digit, total_digit)
            sum += power_value

    if sum == initial_value:
        return True
    return False

if __name__ == '__main__':
    print(isArmstrong(533))
    print(isArmstrong(1634))
    print(isArmstrong(153))
    
