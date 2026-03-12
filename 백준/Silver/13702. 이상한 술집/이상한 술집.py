import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    lo, hi = 1, max(arr)
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 0
        for v in arr:
            cnt += v // mid

        if cnt >= K:          
            ans = mid
            lo = mid + 1
        else:                 
            hi = mid - 1

    print(ans)

if __name__ == "__main__":
    main()