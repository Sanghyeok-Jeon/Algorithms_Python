def find_three_primes(K):
    for i in primes:
        for j in primes:
            for k in primes:
                if i + j + k == K:
                    return i, j, k

    return '0'

def get_primes(n):
    prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return [i for i in range(2, n + 1) if prime[i]]

primes = get_primes(1000)

T = int(input())
for _ in range(T):
    K = int(input())
    print(*find_three_primes(K))