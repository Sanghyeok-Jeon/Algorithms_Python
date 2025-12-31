import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
m = int(input())

if sum(req) <= m:
    print(max(req))
else:
    low, high = 0, max(req)
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        total = 0

        for x in req:
            total += x if x < mid else mid

        if total <= m:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    print(answer)