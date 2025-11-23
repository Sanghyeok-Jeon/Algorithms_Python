import sys

def dfs(day, weight):
    global result
    if weight < 500:
        return

    if day == n:
        result += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(day + 1, weight + kit[i] - k)
            visited[i] = False

n, k = map(int, sys.stdin.readline().split())
kit = list(map(int, sys.stdin.readline().split()))

visited = [False] * n
result = 0
dfs(0, 500)

print(result)