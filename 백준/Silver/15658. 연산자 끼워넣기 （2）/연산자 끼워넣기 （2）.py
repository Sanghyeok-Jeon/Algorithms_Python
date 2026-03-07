import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))  # [+, -, *, /] counts

max_val = -10**18
min_val = 10**18

def dfs(idx: int, cur: int):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, cur)
        min_val = min(min_val, cur)
        return

    next_num = nums[idx]

    # +
    if ops[0] > 0:
        ops[0] -= 1
        dfs(idx + 1, cur + next_num)
        ops[0] += 1

    # -
    if ops[1] > 0:
        ops[1] -= 1
        dfs(idx + 1, cur - next_num)
        ops[1] += 1

    # *
    if ops[2] > 0:
        ops[2] -= 1
        dfs(idx + 1, cur * next_num)
        ops[2] += 1

    # /
    if ops[3] > 0:
        ops[3] -= 1
        dfs(idx + 1, int(cur / next_num))  # 0을 향해 버림
        ops[3] += 1

dfs(1, nums[0])
print(max_val)
print(min_val)