while True:
    data = list(map(int, input().split()))

    if data == [0, 0, 0]:
        break

    for i in range(2):
        for j in range(i+1, 3):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    if data[0]**2 + data[1]**2 == data[2]**2:
        print('right')
    else:
        print('wrong')