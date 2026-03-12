import sys

def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    snacks = list(map(int, input().split()))

    if max(snacks) == 0:
        print(0)
        return

    lo, hi = 1, max(snacks)
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2 
        cnt = 0
        for x in snacks:
            cnt += x // mid

        if cnt >= M:          
            ans = mid
            lo = mid + 1
        else:                
            hi = mid - 1

    print(ans)

if __name__ == "__main__":
    main()