import sys
N = int(sys.stdin.readline())
num = [float(sys.stdin.readline()) for _ in range(N)]

for i in range(1, N):
    num[i] = max(num[i], num[i] * num[i-1])

print("%.3f" % max(num))