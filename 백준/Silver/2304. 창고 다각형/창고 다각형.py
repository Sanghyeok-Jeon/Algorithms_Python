import sys
input = sys.stdin.readline

N = int(input())
pillars = [tuple(map(int, input().split())) for _ in range(N)]
pillars.sort()

xs = [p[0] for p in pillars]
hs = [p[1] for p in pillars]

Hmax = max(hs)
max_indices = [i for i, h in enumerate(hs) if h == Hmax]
left_max = max_indices[0]
right_max = max_indices[-1]

area = 0

# (A) left sweep
cur = 0
for i in range(0, left_max):
    cur = max(cur, hs[i])
    dx = xs[i+1] - xs[i]
    area += cur * dx

# (B) right sweep
cur = 0
for i in range(N-1, right_max, -1):
    cur = max(cur, hs[i])
    dx = xs[i] - xs[i-1]
    area += cur * dx

# (C) max block
area += Hmax * (xs[right_max] - xs[left_max] + 1)

print(area)