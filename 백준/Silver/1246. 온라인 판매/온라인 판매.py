def max_profit(n, m, prices):
    prices.sort(reverse=True)
    max_profit = 0
    best_price = 0

    for i in range(m):
        eggs_sold = min(n, i + 1)
        profit = prices[i] * eggs_sold

        if profit > max_profit:
            max_profit = profit
            best_price = prices[i]

    return best_price, max_profit

n, m = map(int, input().split())
prices = [int(input()) for _ in range(m)]

best_price, max_profit = max_profit(n, m, prices)
print(best_price, max_profit)
