import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

bus_fare = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus_fare[a][b] = min(bus_fare[a][b], c)    # '시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.'

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):    # 경유지
    for i in range(1, n + 1):    # 출발지
        for j in range(1, n + 1):    # 도착지
            bus_fare[i][j] = min(bus_fare[i][j], bus_fare[i][k] + bus_fare[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or bus_fare[i][j] == INF:
            print(0, end=' ')
        else:
            print(bus_fare[i][j], end=' ')
    print()