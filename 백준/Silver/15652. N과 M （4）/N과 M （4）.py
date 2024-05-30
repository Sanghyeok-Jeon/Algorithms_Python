def DFS(idx, cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(idx, N):
        result.append(i+1)
        DFS(i, cnt+1)
        result.pop()

N, M = map(int, input().split())
result = []

DFS(0, 0)