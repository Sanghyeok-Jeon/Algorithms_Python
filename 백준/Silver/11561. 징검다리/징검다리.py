def max_k(N):
    left, right = 1, N
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 <= N:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

T = int(input())
for _ in range(T):
    N = int(input())
    print(max_k(N))