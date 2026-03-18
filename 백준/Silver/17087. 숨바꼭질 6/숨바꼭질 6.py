import sys
import math

input = sys.stdin.readline

N, S = map(int, input().split())
positions = list(map(int, input().split()))

g = 0
for p in positions:
    g = math.gcd(g, abs(p - S))

print(g)