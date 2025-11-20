from collections import deque

N, M = map(int, input().split())

city_map = [list(map(int, input().split())) for _ in range(M)]

q = deque()
q.append((0, 0))

di = [0, 1]
dj = [1, 0]

possible = False
while q:
    i, j = q.popleft()

    if i == M - 1 and j == N - 1:
        possible = True
        break

    for mode in range(2):
        ni = i + di[mode]
        nj = j + dj[mode]

        if 0 <= ni < M and 0 <= nj < N and city_map[ni][nj] == 1:
            q.append((ni, nj))
            city_map[ni][nj] = 0

if possible:
    print('Yes')
else:
    print('No')