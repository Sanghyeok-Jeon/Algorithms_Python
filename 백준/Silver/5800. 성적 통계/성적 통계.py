K = int(input())
for classNum in range(1, K + 1):
    data = list(map(int, input().split()))

    scores = sorted(data[1:])[::-1]
    largesGap = 0
    for i in range(data[0] - 1):
        largesGap = max(largesGap, scores[i] - scores[i + 1])

    print('Class {}'.format(classNum))
    print('Max {}, Min {}, Largest gap {}'.format(max(scores), min(scores), largesGap))
