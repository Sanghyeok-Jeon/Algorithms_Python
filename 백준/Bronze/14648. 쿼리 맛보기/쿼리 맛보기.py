n, q = map(int, input().split())
target = list(map(int, input().split()))
for _ in range(q):
    data = list(map(int, input().split()))
    if data[0] == 1:
        print(sum(target[data[1]-1:data[2]]))
        target[data[1]-1], target[data[2]-1] = target[data[2]-1], target[data[1]-1]
    else:
        cal = sum(target[data[1]-1:data[2]]) - sum(target[data[3]-1:data[4]])
        print(cal)