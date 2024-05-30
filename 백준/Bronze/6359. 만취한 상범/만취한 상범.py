T = int(input())

for tc in range(T):
    n = int(input())
    door = [0] * (n+1)

    for i in range(1, n+1):
        for j in range(i, n+1, i):
            if door[j] == 0:
                door[j] = 1
            else:
                door[j] = 0

    print(sum(door))