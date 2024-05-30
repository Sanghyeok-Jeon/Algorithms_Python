from collections import deque

def BFS(N, K):
    q = deque()
    q.append(N)
    visited = [-1] * 100001
    visited[N] = 0
    
    while q:
        x = q.popleft()
        
        if x == K:  # 동생의 위치에 도달한 경우
            return visited[x]
        
        # 순간이동으로 이동한 경우를 우선순위를 위해 큐 앞으로 추가
        if 0 <= x * 2 <= 100000 and visited[x * 2] == -1:
            q.appendleft(x * 2)
            visited[x * 2] = visited[x]

        # 걸어서 이동한 경우를 큐에 추가
        for nx in (x-1, x+1):
            if 0 <= nx <= 100000 and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1
        
    return -1   # 동생의 위치에 도달하지 못한 경우 -1 반환
    
N, K = map(int, input().split())
result = BFS(N, K)
print(result)