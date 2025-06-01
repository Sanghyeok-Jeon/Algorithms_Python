N, M = map(int, input().split())

min_price_package = 1001
min_price_each = 1001
for _ in range(M):
    price_package, price_each = map(int, input().split())

    min_price_package = min(min_price_package, price_package)
    min_price_each = min(min_price_each, price_each)


print(min(N // 6 * min_price_package + N % 6 * min_price_each, N * min_price_each, (N // 6 + 1) * min_price_package))