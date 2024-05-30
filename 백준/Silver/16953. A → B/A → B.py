def DFS(num, cnt):
    global minCnt
    if num == B:
        if cnt < minCnt:
            minCnt = cnt
        return
    if num > B:
        return

    DFS(num * 2, cnt + 1)
    DFS(num * 10 + 1, cnt + 1)

A, B = map(int, input().split())
minCnt = 2e9

DFS(A, 1)

if minCnt != 2e9:
    print(minCnt)
else:
    print(-1)