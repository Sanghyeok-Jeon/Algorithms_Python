T = int(input())
for _ in range(T):
    data = sorted(list(map(int, input().split())))
    minEven = 0
    sumEven = 0
    for d in data:
        if not d%2:
            if not minEven:
                minEven += d
            sumEven += d
    print(sumEven, minEven)