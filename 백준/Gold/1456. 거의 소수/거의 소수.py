def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(max_num + 1) if is_prime[p]]

def count_almost_primes(A, B):
    max_base = int(B ** 0.5) + 1
    primes = sieve_of_eratosthenes(max_base)

    count = 0
    for prime in primes:
        power = prime * prime
        while power <= B:
            if power >= A:
                count += 1
            if power > B // prime:
                break
            power *= prime
    return count

A, B = map(int, input().split())

result = count_almost_primes(A, B)
print(result)