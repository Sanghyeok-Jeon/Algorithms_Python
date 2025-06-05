import math

N = int(input())
R = list(map(int, input().split()))

ring_first = R[0]
for i in range(1, N):
    g = math.gcd(ring_first, R[i])

    print('{}/{}'.format(ring_first//g, R[i]//g))