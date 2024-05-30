n = int(input())
for _ in range(n):
    p = int(input())

    maxPrice = 0
    answer = ''
    for _ in range(p):
        price, name = input().split()
        if int(price) > maxPrice:
            maxPrice = int(price)
            answer = name

    print(answer)