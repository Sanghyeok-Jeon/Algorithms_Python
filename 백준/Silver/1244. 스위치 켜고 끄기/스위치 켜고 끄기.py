def change(n):
    if switch[n]:
        switch[n] = 0
    else:
        switch[n] = 1
    return

N = int(input())
switch = [0] + list(map(int, input().split()))
student = int(input())
data = [list(map(int, input().split())) for _ in range(student)]

for i in range(student):
    if data[i][0] == 1:
        for j in range(data[i][1], N+1, data[i][1]):
            change(j)
    else:
        change(data[i][1])
        k = 1
        while data[i][1]-k > 0 and data[i][1]+k < N+1 and switch[data[i][1]-k] == switch[data[i][1]+k]:
                change(data[i][1]-k)
                change(data[i][1]+k)
                k += 1

for i in range(1, N+1):
    if i != 1 and i%20 == 1:
        print()
    print(switch[i], end=' ')