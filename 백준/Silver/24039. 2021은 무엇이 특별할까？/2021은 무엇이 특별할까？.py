import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_next_special_number(n):
    primes = []
    limit = 11000
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)

    for i in range(len(primes) - 1):
        product = primes[i] * primes[i + 1]
        if product > n:
            return product

n = int(input())
print(find_next_special_number(n))
