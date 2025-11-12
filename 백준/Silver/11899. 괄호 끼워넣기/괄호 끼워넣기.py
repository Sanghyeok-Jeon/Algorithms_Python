data = input()
stack = []

cnt = 0
for d in data:
    if d == ')':
        if len(stack) and stack[-1] == '(':
            stack.pop()
        else:
            cnt += 1

    else:
        stack.append(d)

print(cnt + len(stack))