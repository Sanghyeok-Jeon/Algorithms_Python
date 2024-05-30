import sys

N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if not len(queue):
            print(-1)
        else:
            print(queue.pop(0))
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if not len(queue):
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not len(queue):
            print(-1)
        else:
            print(queue[0])
    else:
        if not len(queue):
            print(-1)
        else:
            print(queue[-1])