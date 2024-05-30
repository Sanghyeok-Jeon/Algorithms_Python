import collections

N = int(input())
q = collections.deque()
for i in range(1, N+1):
    q.append(i)

cnt = 0
while len(q) > 1:
    if cnt % 2:
        q.append(q.popleft())
    else:
        q.popleft()
    cnt += 1

print(q[0])