data = sorted(list(map(int, input().split())))
if data[1]-data[0] == data[2]-data[1]:
    print(data[2]+data[1]-data[0])
elif data[1]-data[0] < data[2]-data[1]:
    print(data[1]*2-data[0])
else:
    print(data[2]-data[1]+data[0])