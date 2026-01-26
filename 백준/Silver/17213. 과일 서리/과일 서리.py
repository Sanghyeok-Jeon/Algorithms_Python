import math

def combination(n, k):
    return math.comb(n, k)

N = int(input())
M = int(input())

if M < N:
    print(0)
else:
    print(combination(M - 1, N - 1))