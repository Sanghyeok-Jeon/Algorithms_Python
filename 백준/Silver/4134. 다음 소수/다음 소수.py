def isPrime(x):
    if x < 2:
        return False

    for i in range(2, int(x**0.5)+1):
        if not x % i:
            return False

    return True

T = int(input())
for _ in range(T):
    n = int(input())

    while True:
        if isPrime(n):
            print(n)
            break
        else:
            n += 1