def min_difference(n, k):
    min_required = k * (k + 1) // 2

    if n < min_required:
        return -1

    remaining = n - min_required

    return k - 1 + (1 if remaining % k else 0)

n, k = map(int, input().split())

print(min_difference(n, k))