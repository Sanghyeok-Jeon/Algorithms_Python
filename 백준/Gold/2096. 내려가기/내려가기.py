import sys

N = int(sys.stdin.readline())
maxDP = [[0] * 3 for _ in range(2)]
minDP = [[0] * 3 for _ in range(2)]

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))

    maxDP[1][0] = max(maxDP[0][0], maxDP[0][1]) + data[0]
    minDP[1][0] = min(minDP[0][0], minDP[0][1]) + data[0]

    maxDP[1][1] = max(maxDP[0][0], maxDP[0][1], maxDP[0][2]) + data[1]
    minDP[1][1] = min(minDP[0][0], minDP[0][1], minDP[0][2]) + data[1]

    maxDP[1][2] = max(maxDP[0][1], maxDP[0][2]) + data[2]
    minDP[1][2] = min(minDP[0][1], minDP[0][2]) + data[2]

    maxDP[0][0], maxDP[0][1], maxDP[0][2] = maxDP[1][0], maxDP[1][1], maxDP[1][2]
    minDP[0][0], minDP[0][1], minDP[0][2] = minDP[1][0], minDP[1][1], minDP[1][2]

print(max(maxDP[1]), min(minDP[1]))