import sys
import collections

def BFS(p):
    global cnt, sharkSize, startPoint, total
    q = collections.deque()
    visited = [[0]*N for _ in range(N)]
    q.append(p)
    visited[p[0]][p[1]] = 1
    feed = []
    state = False
    Lv = 0

    while q:
        Lv += 1
        for _ in range(len(q)):
            v = q.popleft()
            for mode in range(4):
                ni = v[0] + di[mode]
                nj = v[1] + dj[mode]
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    if not ocean[ni][nj] or ocean[ni][nj] == sharkSize:
                        q.append([ni, nj])
                    elif 0 < ocean[ni][nj] < sharkSize:
                        feed.append([ni, nj])
                        state = True
        if state:
            break
    if state:
        feed.sort(key=lambda x: ((abs(startPoint[0]-x[0])+abs(startPoint[1]-x[1])), x[0], x[1]))
        ocean[feed[0][0]][feed[0][1]] = 9
        ocean[startPoint[0]][startPoint[1]] = 0
        startPoint = feed[0]
        cnt += 1
        total += Lv
        if cnt == sharkSize:
            sharkSize += 1
            cnt = 0
    return state

N = int(sys.stdin.readline())
ocean = []
startPoint = []
sharkSize = 2
cnt = 0
total = 0

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(N):
    oc = list(map(int, sys.stdin.readline().rstrip().split()))
    ocean.append(oc)
    for j, num in enumerate(oc):
        if num == 9:
            startPoint = [i, j]

while True:
    check = BFS(startPoint)
    if not check:
        break

print(total)