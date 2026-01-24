import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(R):
    for c in range(C):
        if grid[r][c] != '.':
            continue

        cnt = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.':
                cnt += 1

        if cnt == 1:
            print(1)
            sys.exit(0)

print(0)