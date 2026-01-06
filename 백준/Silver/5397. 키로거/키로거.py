T = int(input())
for i in range(T):
    data = input()

    stack1 = []
    stack2 = []

    for s in data:
        if s == '<':
            if len(stack1):
                stack2.append(stack1.pop())
        elif s == '>':
            if len(stack2):
                stack1.append(stack2.pop())
        elif s == '-':
            if len(stack1):
                stack1.pop()
        else:
            stack1.append(s)

    print(''.join(stack1) + ''.join(stack2[::-1]))