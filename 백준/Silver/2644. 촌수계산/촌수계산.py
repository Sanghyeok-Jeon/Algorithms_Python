def DFS(p, cnt):
    global min_cnt
    if p == p2:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    for i in range(1, n+1):
        if visited[i] == 0 and connect[p][i] == 1:
            visited[i] = 1
            DFS(i, cnt+1)

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
connect = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    connect[s][e] = 1
    connect[e][s] = 1
visited = [0] * (n+1)
min_cnt = 101

DFS(p1, 0)

print(min_cnt if min_cnt != 101 and min_cnt != 0 else -1)