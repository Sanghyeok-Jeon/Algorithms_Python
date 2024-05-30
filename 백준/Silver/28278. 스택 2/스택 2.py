import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    mode = input().rstrip()

    if len(mode) > 2:
        stack.append(int(mode[2:]))
    elif mode == '2':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif mode == '3':
        print(len(stack))
    elif mode == '4':
        if len(stack):
            print(0)
        else:
            print(1)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)