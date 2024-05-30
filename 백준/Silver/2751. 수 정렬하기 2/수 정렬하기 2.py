import sys

N = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(N)]
for n in sorted(data):
    print(n)