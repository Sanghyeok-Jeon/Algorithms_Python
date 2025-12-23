def evaluate_postfix(expression, values):
    stack = []

    for char in expression:
        if char.isalpha():  # 피연산자일 경우
            stack.append(values[ord(char) - ord('A')])
        else:  # 연산자일 경우
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)

    return stack[0]

n = int(input())
expression = input().strip()
values = [int(input()) for _ in range(n)]

result = evaluate_postfix(expression, values)
print(f"{result:.2f}")