N = int(input())
tower = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:    # 레이저 수신 가능
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if not stack:
        answer.append(0)

    stack.append([i, tower[i]])    # idx, tower

print(*answer)