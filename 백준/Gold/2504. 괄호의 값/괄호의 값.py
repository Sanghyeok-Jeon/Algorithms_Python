data = input()

stack = []
for d in data:
    stack.append(d)

    while True:
        # 1. '()'
        if len(stack) >= 2 and stack[-2:] == ['(', ')']:
            stack = stack[:-2] + ['2']
            continue

        # 2. '[]'
        if len(stack) >= 2 and stack[-2:] == ['[', ']']:
            stack = stack[:-2] + ['3']
            continue

        # 3. '(x)'
        if len(stack) >= 3 and stack[-3] == '(' and stack[-2].isdigit() and stack[-1] == ')':
            stack = stack[:-3] + [str(int(stack[-2]) * 2)]
            continue

        # 4. '[x]'
        if len(stack) >= 3 and stack[-3] == '[' and stack[-2].isdigit() and stack[-1] == ']':
            stack = stack[:-3] + [str(int(stack[-2]) * 3)]
            continue

        # 5. xy = x + y
        if len(stack) >= 2 and stack[-2].isdigit() and stack[-1].isdigit():
            stack = stack[:-2] + [str(int(stack[-2]) + int(stack[-1]))]
            continue

        break

result = int(stack[0]) if (len(stack) == 1 and stack[0].isdigit()) else 0

print(result)