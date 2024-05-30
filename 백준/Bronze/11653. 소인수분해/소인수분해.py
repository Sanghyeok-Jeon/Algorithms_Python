N = int(input())

if N != 1:
    primeNumber = [1] * 10000001
    primeNumber[0] = primeNumber[1] = 0
    for p in range(2, N+1):
        if primeNumber[p]:
            while not N % p:
                print(p)
                N //= p
    
            for i in range(p, N+1, p):
                primeNumber[i] = 0