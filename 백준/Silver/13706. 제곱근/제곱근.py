N = int(input())

start, end = 1, N
while start <= end:
    mid = (start + end) // 2

    sq = mid * mid
    if sq == N:
        print(mid)
        break
    elif sq < N:
        start = mid + 1
    else:
        end = mid - 1