group_no = 1
while True:
    n = int(input())

    if n == 0:
        break

    list_name = []
    list_review = []
    for _ in range(n):
        data = list(input().split())
        name = data[0]
        list_name.append(name)
        list_review.append(data[:0:-1])

    list_nasty_review = []
    for i in range(n):
        listener = list_name[i]
        for j in range(n - 1):
            if list_review[i][j] == 'N':
                writer = list_name[(i + j + 1) % n]
                list_nasty_review.append((writer + ' was nasty about ' + listener, j, i))

    list_nasty_review.sort(key=lambda x:(x[2], -x[1]))

    if group_no != 1:
        print()

    print('Group {}'.format(group_no))
    group_no += 1

    if len(list_nasty_review) == 0:
        print('Nobody was nasty')
    else:
        for i in range(len(list_nasty_review)):
            print(list_nasty_review[i][0])