N = int(input())

answer = 1
tmp = 1

if not N % 2 or not N % 5:
    print(-1)
else:
    while tmp % N:
        answer += 1
        tmp = (tmp % N) * 10 + 1

    print(answer)