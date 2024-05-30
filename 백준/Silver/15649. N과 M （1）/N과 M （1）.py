def DFS(cnt):
    if cnt == M:
        print(*ans)
        return

    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            DFS(cnt+1)
            ans.pop()

N, M = map(int, input().split())

ans = []
DFS(0)