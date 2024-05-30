while True:
    data = list(map(int, input().split()))
    a = data[0]
    if a == 0:
        break

    result = 1
    for i in range(1, 2*a, 2):
        splittingFactor = data[i]
        branching = data[i+1]

        result *= splittingFactor
        result -= branching

    print(result)