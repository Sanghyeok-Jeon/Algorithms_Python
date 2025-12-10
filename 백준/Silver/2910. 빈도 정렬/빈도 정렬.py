from collections import Counter
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
nums = list(map(int, input().split()))

order = {}
for i, num in enumerate(nums):
    if num not in order:
        order[num] = [i, 1]
    else:
        order[num][1] += 1

sorted_items = sorted(order.items(), key=lambda x: (-x[1][1], x[1][0]))

result = []
for num, (idx, cnt) in sorted_items:
    result.extend([str(num)] * cnt)

print(*result)