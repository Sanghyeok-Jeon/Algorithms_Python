R, C, N = map(int, input().split())
init = [list(input()) for _ in range(R)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

now, past = init, []
for n in range(N-1):
    if n % 2 == 0:
        past = now
        now = [list('O'*C) for _ in range(R)]
    else:
        for i in range(R):
            for j in range(C):
                if past[i][j] == 'O':
                    now[i][j] = '.'
                    for mode in range(4):
                        ni = i + di[mode]
                        nj = j + dj[mode]
                        if 0 <= ni < R and 0 <= nj < C:
                            now[ni][nj] = '.'

for i in range(R):
    print(''.join(now[i]))