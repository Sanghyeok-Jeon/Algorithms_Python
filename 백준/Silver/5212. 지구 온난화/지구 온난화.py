import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

next_grid = [['.' for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if grid[r][c] == 'X':
            sea = 0
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    sea += 1
                elif grid[nr][nc] == '.':
                    sea += 1
            if sea < 3:
                next_grid[r][c] = 'X'

xs = [(r, c) for r in range(R) for c in range(C) if next_grid[r][c] == 'X']

if not xs:
    print(".")
    sys.exit(0)

min_r = min(r for r, _ in xs)
max_r = max(r for r, _ in xs)
min_c = min(c for _, c in xs)
max_c = max(c for _, c in xs)

for r in range(min_r, max_r + 1):
    print(''.join(next_grid[r][min_c:max_c + 1]))