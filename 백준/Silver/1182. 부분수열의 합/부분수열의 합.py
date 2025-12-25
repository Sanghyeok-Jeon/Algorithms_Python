import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

def dfs(idx, cur_sum):
    global cnt

    if idx == n:
        if cur_sum == s:
            cnt += 1
        return

    dfs(idx + 1, cur_sum)
    dfs(idx + 1, cur_sum + nums[idx])

dfs(0, 0)

if s == 0:
    cnt -= 1

print(cnt)
