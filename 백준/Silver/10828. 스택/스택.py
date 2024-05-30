import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if not len(stack):
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if not len(stack):
            print(1)
        else:
            print(0)
    else:
        if not len(stack):
            print(-1)
        else:
            print(stack[-1])