import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    
    if x == 2:
        return True
    
    if x % 2 == 0:
        return False
    
    limit = int(x ** 0.5)
    for i in range(3, limit + 1, 2):
        if x % i == 0:
            return False
        
    return True

N = int(input())
numbers = list(map(int, input().split()))

primes = set()
for num in numbers:
    if is_prime(num):
        primes.add(num)
        
if not primes:
    print(-1)
else:
    result = 1
    for p in primes:
        result *= p
    
    print(result)