data = input()
stack = []

for d in data:
    if d.isdigit():
        stack.append(int(d))
    else:
        right = stack.pop()
        left = stack.pop()

        if d == '+':
            stack.append(left + right)
        elif d == '-':
            stack.append(left - right)
        elif d == '*':
            stack.append(left * right)
        elif d == '/':
            stack.append(left // right)

print(stack.pop())