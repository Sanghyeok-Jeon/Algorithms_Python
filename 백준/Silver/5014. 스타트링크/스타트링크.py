import collections

def BFS():

    while q:
        now, cntButton = q.popleft()
        if now == G:
            return cntButton

        for mode in range(2):
            next = now + ud[mode]
            if 1 <= next <= F and visited[next] == 0:
                visited[next] = 1
                q.append((next, cntButton+1))

    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)
q = collections.deque()
q.append((S, 0))
visited[S] = 1
ud = [U, -D]

print(BFS())