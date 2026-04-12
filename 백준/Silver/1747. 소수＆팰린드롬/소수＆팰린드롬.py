import sys
import math

input = sys.stdin.readline

n = int(input())


def is_palindrome(x):
    s = str(x)
    return s == s[::-1]


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


num = n
while True:
    if is_palindrome(num) and is_prime(num):
        print(num)
        break
    num += 1