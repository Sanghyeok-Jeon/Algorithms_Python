while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    cnt = 0
    prev = 0
    while a > 0 or b > 0:
        if a%10 + b%10 + prev >= 10:
            cnt += 1
            a //= 10
            b //= 10
            prev = 1
        else:
            a //= 10
            b //= 10
            prev = 0

    print(cnt)