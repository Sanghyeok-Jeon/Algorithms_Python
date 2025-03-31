N = int(input())
data = list(map(int, input().split()))

max_profit = 0
high_price = data[-1]
low_price = max(data)
for i in range(N - 2, -1, -1):
    if data[i] > high_price:
        high_price = data[i]
        low_price = high_price
    else:
        low_price = min(low_price, data[i])
        max_profit = max(max_profit, high_price - low_price)

print(max_profit)