C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))
    avgData = sum(data[1:]) / data[0]

    winner = 0
    for i in range(1, len(data)):
        if data[i] > avgData:
            winner += 1

    print('{:.3f}%'.format(winner/data[0]*100))