import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))

result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return

    prev = 0
    for i in range(start, n):
        if prev != nums[i]:
            result.append(nums[i])
            prev = nums[i]
            dfs(i + 1)
            result.pop()

dfs(0)