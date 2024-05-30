N, X = map(int, input().split())
A = list(map(int, input().split()))

min_price = 1000 * 1000000 * 2 + 1
for i in range(N-1):
    tmp_price = A[i] * X + A[i+1] * X
    min_price = min(min_price, tmp_price)

print(min_price)