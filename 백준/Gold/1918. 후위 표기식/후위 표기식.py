def postfix(exp):
    stack = [] # 연산자를 저장할 스택
    result = ''

    # 연산자 우선순위
    priority = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }

    for c in exp:
        if c.isalpha(): # 피연산자
            result += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # 여는 괄호 제거
        else: # 연산자
            while stack and priority[c] <= priority.get(stack[-1], 0):
                result += stack.pop()
            stack.append(c)

    while stack: # 스택에 남은 연산자들을 결과에 추가
        result += stack.pop()

    return result

expression = input()
result = postfix(expression)
print(result)