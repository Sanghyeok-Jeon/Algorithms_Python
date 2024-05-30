import sys

R, C = map(int, sys.stdin.readline().split())
room = [[0]*C for _ in range(R)]
k = int(sys.stdin.readline())
for i in range(k):
    br, bc = map(int, sys.stdin.readline().split())
    room[br][bc] = -1
sr, sc = map(int, sys.stdin.readline().split())
room[sr][sc] = -2
order = list(map(int, sys.stdin.readline().split()))

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

i, j = sr, sc
mode = 0
cnt = 0
while True:
    if cnt == 4:
        break
    ni = i + di[order[mode]]
    nj = j + dj[order[mode]]
    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] == 0:
        room[ni][nj] = 1
        i, j = ni, nj
        cnt = 0
    else:
        cnt += 1
        mode = (mode + 1) % 4

print(i, j)