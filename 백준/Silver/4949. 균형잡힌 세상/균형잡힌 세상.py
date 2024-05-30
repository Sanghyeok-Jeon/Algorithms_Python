while True:
    data = input()

    if data == '.':
        break

    yesPossible = 1
    stack = []
    for d in data:
        if d == '(' or d == '[':
            stack.append(d)
        elif d == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                yesPossible = 0
                break
        elif d == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                yesPossible = 0
                break
        else:
            continue

    if yesPossible and not len(stack):
        print('yes')
    else:
        print('no')