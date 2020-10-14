def isPrime(num):
    first_prime = 2
    try:
        if num > 0:
            while first_prime <= num // 2:
                if num % first_prime == 0:
                    return False
                first_prime += 1
                if first_prime % 2 == 0:
                    first_prime += 1
            return True
    except TypeError:
        return "Enter numerical value"

print(isPrime(97))
print(isPrime(71))
print(isPrime(10971))
print(isPrime("97"))
