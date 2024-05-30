from collections import deque

def BFS():
    while q:
        num, cnt = q.popleft()
        if num == 100:
            return cnt

        for dice in range(1, 7):
            next_num = num + dice
            if next_num <= 100 and not visited[next_num]:
                if next_num in snake_ladder.keys():
                    next_num = snake_ladder[next_num]
                visited[next_num] = True
                q.append((next_num, cnt+1))

N, M = map(int, input().split())
visited = [False] * 101

snake_ladder = dict()
for _ in range(N):
    x, y = map(int, input().split())
    snake_ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snake_ladder[u] = v

q = deque()
q.append((1, 0))

answer = BFS()

print(answer)