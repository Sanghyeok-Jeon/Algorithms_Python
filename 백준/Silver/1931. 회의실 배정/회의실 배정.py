import sys

N = int(sys.stdin.readline())
meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])

ans = 0
start = 0
for m in meeting:
    if m[0] >= start:
        start = m[1]
        ans += 1

print(ans)