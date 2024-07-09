A, B = map(int, input().split())

x1 = int(-2 * A + ((2 * A) ** 2 - 4 * B) ** 0.5) // 2
x2 = int(-2 * A - ((2 * A) ** 2 - 4 * B) ** 0.5) // 2

if x1 == x2:
    print(x1)
elif x1 > x2:
    print(x2, x1)
else:
    print(x1, x2)