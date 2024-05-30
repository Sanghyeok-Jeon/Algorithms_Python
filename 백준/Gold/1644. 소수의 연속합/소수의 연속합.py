# 에라토스테네스의 체를 사용하여 소수를 구하는 함수
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

def find_prime_sum(n):
    primes = sieve_of_eratosthenes(n)
    count = 0    # 소수의 연속합의 개수
    total = 0    # 소수의 연속합의 합
    left = right = 0

    while right <= len(primes):
        if total < n:    # 소수의 연속합이 n보다 작은 경우
            if right == len(primes):
                break

            total += primes[right]
            right += 1
        else:    # 소수의 연속합이 n보다 크거나 같은 경우
            total -= primes[left]
            left += 1

        # 소수의 연속합이 n과 같은 경우
        if total == n:
            count += 1

    return count

N = int(input())

# 소수의 연속합 구하기
result = find_prime_sum(N)

print(result)