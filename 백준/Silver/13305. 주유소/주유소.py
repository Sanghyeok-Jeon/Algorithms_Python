N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

total_price = 0
min_price = price[0]
for i in range(N - 1):
    if price[i] > min_price:
        price[i] = min_price
    else:
        min_price = price[i]

    total_price += min_price * distance[i]

print(total_price)