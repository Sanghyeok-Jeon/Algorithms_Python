numbers = list(map(int, input().split()))

answer = min(numbers)
while True:
    cnt = 0
    for num in numbers:
        if answer % num == 0:
            cnt += 1

    if cnt >= 3:
        print(answer)
        break

    answer += 1