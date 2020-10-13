#Dynamic programming
def febonacci(num):
    if type(num) != int or num < 1:
            return "invalid input"
    f1 = 0
    f2 = 1

    while num != 1:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        num -= 1
    return f1

# Recursion
# def febonacci(num):
#     if type(num) != int or num < 1:
#         return "invalid input"
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     else:
#         return febonacci(num-1) + febonacci(num-2)
    


print(febonacci(5))
print(febonacci(9))
print(febonacci(1))
print(febonacci(2))