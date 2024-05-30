import collections

def BFS():
    global M
    while q:
        now, cnt = q.popleft()
        visited[now] = 1
        if now == M:
            return cnt
        for m in range(8):
            if m < 6:
                next = now + move[m]
                if 0 <= next <= 100000 and visited[next] == 0:
                    visited[next] = 1
                    q.append((next, cnt+1))
            else:
                next = now * move[m]
                if 0 <= next <= 100000 and visited[next] == 0:
                    visited[next] = 1
                    q.append((next, cnt+1))
                    
A, B, N, M = map(int, input().split())
q = collections.deque()
q.append((N, 0))
visited = [0] * 100001
move = [1, -1, A, -A, B, -B, A, B]

print(BFS())