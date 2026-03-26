import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def count_factorial_prime(n, p):
    count = 0
    while n > 0:
        n //= p
        count += n
    return count

count_two = count_factorial_prime(n, 2) - count_factorial_prime(m, 2) - count_factorial_prime(n - m, 2)
count_five = count_factorial_prime(n, 5) - count_factorial_prime(m, 5) - count_factorial_prime(n - m, 5)

print(min(count_two, count_five))