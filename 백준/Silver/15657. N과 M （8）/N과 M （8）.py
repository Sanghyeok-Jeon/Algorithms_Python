def DFS(idx, cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(idx, N):
        result.append(data[i])
        DFS(i, cnt+1)
        result.pop()

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = []
DFS(0, 0)