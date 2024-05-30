def DFS(idx, cnt):
    if cnt == M:
        print(*result)
        return

    for i in range(idx, len(numList)):
        result.append(numList[i])
        DFS(i, cnt+1)
        result.pop()

N, M = map(int, input().split())
numList = sorted(set(list(map(int, input().split()))))
result = []

DFS(0, 0)