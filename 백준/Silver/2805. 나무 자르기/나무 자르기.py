import sys

N, M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))
woods.sort()

short, long = 1, woods[-1]
while short <= long:
    mid = (short + long) // 2

    temp = 0
    for wood in woods:
        if wood > mid:
            temp += wood - mid
    if temp >= M:
        short = mid + 1
    else:
        long = mid - 1

print(long)