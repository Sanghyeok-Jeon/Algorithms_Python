import sys

input = sys.stdin.readline

k = int(input())
arr = list(map(int, input().split()))

levels = [[] for _ in range(k)]

def build(start, end, depth):
    if start > end:
        return

    mid = (start + end) // 2
    levels[depth].append(arr[mid])

    build(start, mid - 1, depth + 1)
    build(mid + 1, end, depth + 1)

build(0, len(arr) - 1, 0)

for level in levels:
    print(*level)