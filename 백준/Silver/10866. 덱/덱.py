import sys
import collections

N = int(sys.stdin.readline())
q = collections.deque()
for _ in range(N):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push_front':
        q.appendleft(order[1])
    elif order[0] == 'push_back':
        q.append(order[1])
    elif order[0] == 'pop_front':
        if not len(q):
            print(-1)
        else:
            print(q.popleft())
    elif order[0] == 'pop_back':
        if not len(q):
            print(-1)
        else:
            print(q.pop())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if not len(q):
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not len(q):
            print(-1)
        else:
            print(q[0])
    else:
        if not len(q):
            print(-1)
        else:
            print(q[-1])
