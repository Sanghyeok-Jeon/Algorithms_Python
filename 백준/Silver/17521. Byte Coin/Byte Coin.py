n, w = map(int, input().split())
prices = [int(input()) for _ in range(n)]
coin = 0

for i in range(n-1):
    if prices[i] < prices[i+1]:
        buy = w // prices[i]
        w -= buy * prices[i]
        coin += buy
    elif prices[i] > prices[i+1] and coin > 0:
        w += coin * prices[i]
        coin = 0

if coin > 0:
    w += coin * prices[-1]
    
print(w)