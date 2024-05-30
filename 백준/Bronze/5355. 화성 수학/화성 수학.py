T = int(input())
for tc in range(T):
    data = list(input().split())
    num = float(data[0])

    for i in range(1, len(data)):
        if data[i] == '@':
            num *= 3
        elif data[i] == '%':
            num += 5
        else:
            num -= 7

    print('{0:.2f}'.format(num))