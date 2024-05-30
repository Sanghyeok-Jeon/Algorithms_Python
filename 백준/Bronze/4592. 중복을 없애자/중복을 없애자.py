while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    
    afterData = []
    for i in range(1, data[0]+1):
        if i == 1:
            afterData.append(data[i])
        else:
            if data[i] != afterData[-1]:
                afterData.append(data[i])
        
    print(*afterData, '$')