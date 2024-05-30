import sys
input = sys.stdin.readline

def DFS(r, c, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for mode in range(4):
        nr = r + dr[mode]
        nc = c + dc[mode]
        if 0 <= nr < R and 0 <= nc < C and alphabet[nr][nc] not in visited_alpha:
            visited_alpha.add(alphabet[nr][nc])
            DFS(nr, nc, cnt + 1)
            visited_alpha.remove(alphabet[nr][nc])

    return max_cnt

R, C = map(int, input().split())
alphabet = [list(input()) for _ in range(R)]
visited_alpha = set()
visited_alpha.add(alphabet[0][0])
max_cnt = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

DFS(0, 0, 1)

print(max_cnt)