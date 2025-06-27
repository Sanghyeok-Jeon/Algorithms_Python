N = int(input())
data = [input() for _ in range(N)]

number = []
for i in range(N):
    target = data[i]

    num = ''
    for t in target:
        if t.isnumeric():
            num += t
        else:
            if len(num):
                number.append(int(num))
            num = ''

    if len(num):
        number.append(int(num))

number.sort()
for i in range(len(number)):
    print(number[i])