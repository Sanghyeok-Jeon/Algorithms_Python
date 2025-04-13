P = int(input())
for _ in range(P):
    data = list(map(int, input().split()))

    total = 0
    for i in range(1, 20):
        for j in range(i + 1, 21):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                total += 1

    print(data[0], total)
