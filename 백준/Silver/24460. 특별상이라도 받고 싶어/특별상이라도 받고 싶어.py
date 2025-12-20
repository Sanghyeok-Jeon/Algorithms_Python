import sys
input = sys.stdin.readline

def solve(x, y, size):
    if size == 1:
        return board[x][y]

    half = size // 2
    vals = []
    vals.append(solve(x, y, half))
    vals.append(solve(x, y + half, half))
    vals.append(solve(x + half, y, half))
    vals.append(solve(x + half, y + half, half))

    vals.sort()
    return vals[1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(solve(0, 0, N))