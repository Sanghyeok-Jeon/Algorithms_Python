import sys
N = int(sys.stdin.readline())
cnt = 1
stick = []

for _ in range(N):
    stick.append(int(sys.stdin.readline()))

maxH = stick[-1]

for i in range(N-1, -1, -1):
    if stick[i] > maxH:
        cnt += 1
        maxH = stick[i]

print(cnt)