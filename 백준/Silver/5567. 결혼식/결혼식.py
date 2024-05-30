import sys
import collections

def BFS():
    cnt = 0
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            person = q.popleft()
            for p in friends[person]:
                if not invite[p]:
                    invite[p] = 1
                    q.append(p)
                    cnt += 1

        if level == 2:
            break

    return cnt

n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
invite = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

q = collections.deque()
q.append(1)
invite[1] = 1

print(BFS())