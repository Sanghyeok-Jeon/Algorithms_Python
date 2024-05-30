def DFS(cnt):
    global answer, sum_hobbit
    if cnt == 7:
        if sum_hobbit == 100:
            for i in range(9):
                if visited[i]:
                    print(hobbit[i])
            exit()
        return
    if sum_hobbit > 100:
        return

    for i in range(9):
        if not visited[i]:
            visited[i] = 1
            sum_hobbit += hobbit[i]
            DFS(cnt+1)
            visited[i] = 0
            sum_hobbit -= hobbit[i]

data = [int(input()) for _ in range(9)]
hobbit = sorted(data)
answer = []
visited = [0] * 9
sum_hobbit = 0

DFS(0)

print(answer)