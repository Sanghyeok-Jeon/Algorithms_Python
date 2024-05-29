T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    a %= 10

    if a in (0, 1, 5, 6):
        if not a:
            print(10)
        else:
            print(a)
    else:
        b = 4 + b % 4
        print((a ** b) % 10)