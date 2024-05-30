N = int(input())
maxPrice = 0
for _ in range(N):
    a, b, c = sorted(map(int, input().split()))
    price = 0

    if a == b == c:
        price += 10000 + a*1000
    elif (a==b and a!=c) or (a!=b and b==c):
        price += 1000 + b*100
    else:
        price += c*100

    maxPrice = max(price, maxPrice)

print(maxPrice)