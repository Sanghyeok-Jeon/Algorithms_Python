import sys
input = sys.stdin.readline

N = int(input())
stack = []
score = 0

for _ in range(N):
    info = list(map(int, input().split()))

    if info[0] == 1:
        A, T = info[1], info[2]
        if T == 1:
            score += A
        else:
            stack.append([A, T - 1])
    else:
        if stack:
            A, T = stack.pop()
            T -= 1
            if T == 0:
                score += A
            else:
                stack.append([A, T])

print(score)