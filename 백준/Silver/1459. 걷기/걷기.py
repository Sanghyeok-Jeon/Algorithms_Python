X, Y, W, S = map(int, input().split())

if S < 2 * W:
    if S > W:
        print(min(X, Y) * S + abs(X - Y) * W)
    else:
        if (X + Y) % 2 == 1:
            print((max(X, Y) - 1) * S + W)
        else:
            print(max(X, Y) * S)
else:
    print((X + Y) * W)