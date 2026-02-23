import sys
input = sys.stdin.readline

N, M = map(int, input().split())
t = list(map(int, input().split()))

def can_make(x: int) -> bool:
    total = 0
    for i in range(N):
        total += x // t[i]

        if total >= M:
            return True

    return False

lo, hi = 0, min(t) * M

while lo < hi:
    mid = (lo + hi) // 2
    if can_make(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)