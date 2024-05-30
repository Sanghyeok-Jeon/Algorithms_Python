def DFS(x, count):
    if count == 6:
        for i in range(k):
            if selected[i]:
                print(S[i], end=' ')
        print()
        return

    for j in range(x, k):
        selected[j] = 1
        DFS(j+1, count+1)
        selected[j] = 0

while True:
    data = list(map(int, input().split()))
    k = data[0]

    if k == 0:
        break

    S = data[1:]
    selected = [0] * k

    DFS(0, 0)

    print()