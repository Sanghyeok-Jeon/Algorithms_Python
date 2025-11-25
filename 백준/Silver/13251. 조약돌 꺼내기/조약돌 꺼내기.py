from math import comb
import sys
input = sys.stdin.readline

m = int(input().strip())
stones = list(map(int, input().strip().split()))
k = int(input().strip())

total_stones = sum(stones)
probability = 0.0

for stone_count in stones:
    if stone_count >= k:
        probability += comb(stone_count, k) / comb(total_stones, k)

print(probability)