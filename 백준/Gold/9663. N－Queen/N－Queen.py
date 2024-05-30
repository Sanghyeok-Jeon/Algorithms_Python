def DFS(i, cnt):
    global nQueen
    if i == N:
        if cnt == N:
            nQueen += 1
        return

    for j in range(N):
        if selected[j]:
            continue

        possible = True
        for mode in range(3):
            check_i = i + di[mode]
            check_j = j + dj[mode]
            while True:
                if check_i < 0 or check_i > N-1 or check_j < 0 or check_j > N-1:
                    break
                if board[check_i][check_j]:
                    possible = False
                    break
                else:
                    check_i += di[mode]
                    check_j += dj[mode]

            if not possible:
                break

        if possible:
            selected[j] = 1
            board[i][j] = 1
            DFS(i+1, cnt+1)
            board[i][j] = 0
            selected[j] = 0

N = int(input())
nQueen = 0
board = [[0] * N for _ in range(N)]
selected = [0] * N

di = [-1, -1, -1]
dj = [-1, 0, 1]

DFS(0, 0)

print(nQueen)