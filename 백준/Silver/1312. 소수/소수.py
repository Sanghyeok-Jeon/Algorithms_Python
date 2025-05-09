A, B, N = map(int, input().split())

num = A % B
i = 0
answer = 0
while True:
    num *= 10
    if num >= B:
        answer = num // B
    else:
        answer = 0

    num %= B

    i += 1

    if i == N:
        break

print(answer)