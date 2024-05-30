T = int(input())
for _ in range(T):
    num, unit = input().split()

    if unit == 'kg':
        print(format(float(num) * 2.2046, ".4f"), 'lb')
    elif unit == 'lb':
        print(format(float(num) * 0.4536, ".4f"), 'kg')
    elif unit == 'l':
        print(format(float(num) * 0.2642, ".4f"), 'g')
    elif unit == 'g':
        print(format(float(num) * 3.7854, ".4f"), 'l')