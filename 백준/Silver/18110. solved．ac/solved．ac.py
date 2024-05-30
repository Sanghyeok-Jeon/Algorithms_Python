import sys

def new_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

n = int(sys.stdin.readline())
if n:
    data = [int(sys.stdin.readline()) for _ in range(n)]
    data.sort()
    boundary = new_round(n * 0.15)
    print(new_round(sum(data[boundary:-boundary] if boundary else data) / (n - 2 * boundary)))
else:
    print(0)