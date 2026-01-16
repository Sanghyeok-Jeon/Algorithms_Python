def solve(index, choose):
    global count
    if index == 10:
        point = 0
        for i in range(10):
            if answers[i] == choose[i]:
                point += 1

        if point >= 5:
            count += 1
        return

    for i in range(1, 6):
        if index >= 2 and choose[index-1] == i and choose[index-2] == i:
            continue
        choose[index] = i
        solve(index + 1, choose)
        choose[index] = 0

count = 0
answers = list(map(int, input().split()))
choose = [0] * 10
solve(0, choose)
print(count)