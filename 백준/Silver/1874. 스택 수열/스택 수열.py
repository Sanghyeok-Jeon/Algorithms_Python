import sys

n = int(sys.stdin.readline())
stack = []
pushPop = []
cnt = 1
possible = True

for _ in range(n):
    target = int(sys.stdin.readline())

    while cnt <= target:
        stack.append(cnt)
        pushPop.append('+')
        cnt += 1

    if stack[-1] == target:
        stack.pop()
        pushPop.append('-')
    else:
        possible = False
        break

if not possible:
    print('NO')
else:
    print('\n'.join(pushPop))