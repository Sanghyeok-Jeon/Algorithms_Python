T = int(input())
for tc in range(T):
    N = int(input())
    subTotal = 0
    for i in range(1, N+1):
        if i % 2:
            subTotal += i
    print(subTotal)