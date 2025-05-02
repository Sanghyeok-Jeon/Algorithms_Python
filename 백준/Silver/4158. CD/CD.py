import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    sg = set()
    for _ in range(N):
        data = int(input())
        sg.add(data)

    sy = set()
    for _ in range(M):
        data = int(input())
        sy.add(data)

    print(len(sg&sy))