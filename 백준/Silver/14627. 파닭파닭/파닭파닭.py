import sys

def solve():
    input = sys.stdin.readline
    S, C = map(int, input().split())
    arr = [int(input().strip()) for _ in range(S)]

    lo, hi = 1, max(arr)
    best = 0

    def pieces(L: int) -> int:
        return sum(x // L for x in arr)

    while lo <= hi:
        mid = (lo + hi) // 2
        if pieces(mid) >= C:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1

    total = sum(arr)
    waste = total - best * C
    print(waste)

if __name__ == "__main__":
    solve()