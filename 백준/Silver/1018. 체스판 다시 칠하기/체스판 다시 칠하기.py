import sys

N, M = map(int, sys.stdin.readline().split())
board = [input() for _ in range(N)]
min_paint = 50 * 50
chess1 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]
chess2 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

for i in range(N-8+1):
    for j in range(M-8+1):
        tmp_paint1 = 0
        tmp_paint2 = 0
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y] != chess1[x][y]:
                    tmp_paint1 += 1
                if board[i+x][j+y] != chess2[x][y]:
                    tmp_paint2 += 1

        min_paint = min(min_paint, tmp_paint1, tmp_paint2)

print(min_paint)