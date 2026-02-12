import sys
from math import gcd, isqrt

input = sys.stdin.readline
R, G = map(int, input().split())

d = gcd(R, G)
divisors = []

# d의 약수 찾기 (1 ~ sqrt(d))
for i in range(1, isqrt(d) + 1):
    if d % i == 0:
        divisors.append(i)
        if i * i != d:
            divisors.append(d // i)

divisors.sort()

out = []
for n in divisors:
    out.append(f"{n} {R//n} {G//n}")
print("\n".join(out))