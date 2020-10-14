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

# print(isPrime(97))
# print(isPrime(71))
# print(isPrime(10971))
# print(isPrime("97"))

def primeInRange(lower_range, upper_range):
    all_prime = []
    try:
        for number in range(lower_range, upper_range+1):
            prime = isPrime(number)
            if prime:
                all_prime.append(number)
        return all_prime
    except TypeError:
        return "Enter numerical value"


all_prime = primeInRange(100, 200)
print(all_prime)