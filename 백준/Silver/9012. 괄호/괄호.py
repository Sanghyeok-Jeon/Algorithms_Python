
T = int(input())
for _ in range(T):
    ps = input()
    stack = []

    impossible = 0
    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                impossible = 1
                break

    if impossible == 0 and len(stack) == 0:
        print('YES')
    else:
        print('NO')