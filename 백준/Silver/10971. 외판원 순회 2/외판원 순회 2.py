import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
answer = float('inf')


def dfs(now, depth, total):
    global answer

    if total >= answer:
        return

    if depth == N:
        if W[now][0] != 0:
            answer = min(answer, total + W[now][0])
        return

    for nxt in range(1, N):  
        if not visited[nxt] and W[now][nxt] != 0:
            visited[nxt] = True
            dfs(nxt, depth + 1, total + W[now][nxt])
            visited[nxt] = False


visited[0] = True
dfs(0, 1, 0)

print(answer)