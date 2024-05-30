T = int(input())
for tc in range(T):
    tg, data = input().split()
    target = int(tg) - 1

    answer = ''
    for i in range(len(data)):
        if i != target:
            answer += data[i]

    print(answer)