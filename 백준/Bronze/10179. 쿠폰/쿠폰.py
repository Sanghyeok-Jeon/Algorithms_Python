T = int(input())
for _ in range(T):
    priceOrigin = float(input())
    print('$', end='')
    print(format(priceOrigin*0.8, '.2f'))