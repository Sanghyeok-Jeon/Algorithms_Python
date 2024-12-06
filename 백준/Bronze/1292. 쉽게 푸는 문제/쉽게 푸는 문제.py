A, B = map(int, input().split())

n = 1
idx = 1
answer = 0

while idx <= B:
    for i in range(n):
        if A <= idx <= B:
            answer += n
        idx += 1

    n += 1

print(answer)