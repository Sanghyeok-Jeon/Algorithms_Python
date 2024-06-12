N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    if (x + y) % 2 or (x - y) > 2 or x < y:
        print('No Number')
    else:
        if x % 2:
            print(x + y - 1)
        else:
            print(x + y)