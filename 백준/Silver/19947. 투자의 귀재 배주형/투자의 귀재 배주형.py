H, Y = map(int, input().split())
profit = [0] * 11

for i in range(11):
    if i == 0:
        profit[i] = H
    elif i <= 2:
        profit[i] = int(profit[i - 1] * 1.05)
    elif i <= 4:
        profit[i] = max(int(profit[i - 1] * 1.05), int(profit[i - 3] * 1.2))
    else:
        profit[i] = max(int(profit[i - 1] * 1.05), int(profit[i - 3] * 1.2), int(profit[i - 5] * 1.35))

print(profit[Y])