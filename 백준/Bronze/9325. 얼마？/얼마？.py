T = int(input())
for tc in range(T):
    price = int(input())
    optionCnt = int(input())
    for _ in range(optionCnt):
        q, p = map(int, input().split())
        price += q * p
    print(price)