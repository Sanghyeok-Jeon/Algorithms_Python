import sys
N = int(input())
winA, winB = 0, 0
for _ in range(N):
    scoreA, scoreB = map(int, sys.stdin.readline().split())
    if scoreA > scoreB:
        winA += 1
    elif scoreA < scoreB:
        winB += 1
print(winA, winB)