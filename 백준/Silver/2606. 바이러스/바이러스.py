import sys
import collections

def BFS():
    cnt = 0
    while q:
        tmp_data = q.popleft()
        for i in range(len(tmp_data)):
            if not visited[tmp_data[i]]:
                visited[tmp_data[i]] = 1
                cnt += 1
                q.append(data[tmp_data[i]])
    return cnt

N = int(input())
connect = int(input())
data = [[] for _ in range(N+1)]
for _ in range(connect):
    s, e = map(int, input().split())
    data[s].append(e)
    data[e].append(s)
q = collections.deque()
q.append(data[1])
visited = [0]*(N+1)
visited[1] = 1

print(BFS())