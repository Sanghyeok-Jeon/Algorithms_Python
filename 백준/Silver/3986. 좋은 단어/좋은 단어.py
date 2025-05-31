N = int(input())

answer = 0
for _ in range(N):
    report = input()
    stack = []

    for i in range(len(report)):
        if len(stack) == 0:
            stack.append(report[i])
        else:
            if stack[-1] == report[i]:
                stack.pop()
            else:
                stack.append(report[i])

    if not len(stack):
        answer += 1

print(answer)