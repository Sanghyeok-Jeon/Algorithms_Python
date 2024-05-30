T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    price = 0

    if a == 1:
        price += 5000000
    elif 1 < a <= 3:
        price += 3000000
    elif 3 < a <= 6:
        price += 2000000
    elif 6 < a <= 10:
        price += 500000
    elif 10 < a <= 15:
        price += 300000
    elif 15 < a <= 21:
        price += 100000

    if b == 1:
        price += 5120000
    elif 1 < b <= 3:
        price += 2560000
    elif 3 < b <= 7:
        price += 1280000
    elif 7 < b <= 15:
        price += 640000
    elif 15 < b <= 31:
        price += 320000

    print(price)