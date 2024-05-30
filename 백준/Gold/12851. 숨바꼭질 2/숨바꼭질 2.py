from collections import deque

def bfs(start, target):
    min_time, count = float('inf'), 0

    q = deque()
    q.append((start, 0))

    while q:
        now, time = q.popleft()
        visited[now] = True

        if now == target:
            if time < min_time:
                min_time = time
                count = 1
            elif time == min_time:
                count += 1

        for next in [now - 1, now + 1, now * 2]:
            if 0 <= next <= 100000 and not visited[next]:
                q.append((next, time + 1))

    return min_time, count

N, K = map(int, input().split())

visited = [False] * 100001

min_time, count = bfs(N, K)

print(min_time)
print(count)