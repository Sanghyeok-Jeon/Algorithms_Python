def DFS(cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(lstNo[i])
            DFS(cnt+1)
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())
lstNo = list(map(int, input().split()))
lstNo.sort()
visited = [0] * N
result = []

DFS(0)