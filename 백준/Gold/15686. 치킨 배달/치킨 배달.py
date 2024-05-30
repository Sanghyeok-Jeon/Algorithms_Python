import sys

def measure(idx, cnt):
    global distanceChicken
    if idx > len(chicken):  
        return

    if cnt == M:
        distanceTemp = 0
        for xHouse, yHouse in house:
            d = 2e9
            for v in V:
                xChicken, yChicken = chicken[v]
                d = min(d, abs(xHouse-xChicken)+abs(yHouse-yChicken))
            distanceTemp += d
        distanceChicken = min(distanceChicken, distanceTemp)
        return

    V.append(idx)  # 지점 선택
    measure(idx+1, cnt+1)
    V.pop()
    measure(idx+1, cnt)

N, M = map(int, sys.stdin.readline().rstrip().split())
position = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
house, chicken, V = [], [], []
distanceChicken = 2e9

for i in range(N):
    for j in range(N):
        if position[i][j] == 1:
            house.append((i+1, j+1))
        elif position[i][j] == 2:
            chicken.append((i+1, j+1))

measure(0, 0)

print(distanceChicken)