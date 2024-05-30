N = int(input())
nowOrder = list(map(int, input().split()))

stack = []
passNum = 0
while nowOrder:
    if nowOrder[0] == passNum+1:
        nowOrder.pop(0)
        passNum += 1
    else:
        stack.append(nowOrder.pop(0))

    while stack:
        if stack[-1] == passNum+1:
            stack.pop()
            passNum += 1
        else:
            break

print('Nice' if not stack else 'Sad')