import collections

def BFS():
    for i in range(1, k+1):
        if bus[i][0] <= sx <= bus[i][2] and bus[i][1] <= sy <= bus[i][3]:
            q.append(i)
            visited[i] = 1

    while q:
        idx = q.popleft()
        if bus[idx][0] <= dx <= bus[idx][2] and bus[idx][1] <= dy <= bus[idx][3]:
            return visited[idx]
        for j in range(1, k+1):
            if not visited[j]:
                if bus[idx][0] <= bus[j][2] and bus[idx][2] >= bus[j][0] and bus[idx][1] <= bus[j][3] and bus[idx][3] >= bus[j][1]:
                    visited[j] = visited[idx] + 1
                    q.append(j)

m, n = map(int, input().split())
k = int(input())
bus = [0] * (k+1)
for i in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    bus[b] = [x1, y1, x2, y2]
sx, sy, dx, dy = map(int, input().split())
visited = [0] * (k+1)
q = collections.deque()

print(BFS())