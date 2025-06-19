def count_good_intervals(L, n):
    L.sort()

    if n in L:
        return 0

    left, right = 0, 0
    for num in L:
        if num < n:
            left = num
        elif num > n:
            right = num
            break

    count = (n - left - 1) * (right - n) + (right - n - 1)

    return count

S = int(input())
L = list(map(int, input().split()))
n = int(input())

print(count_good_intervals(L, n))