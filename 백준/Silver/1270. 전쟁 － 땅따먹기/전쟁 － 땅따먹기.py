n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    Ti = data[0]
    Nij = data[1:]

    count = {}
    for tmp_army in Nij:
        if tmp_army in count:
            count[tmp_army] += 1
        else:
            count[tmp_army] = 1

    majority = Ti // 2
    answer = 'SYJKGW'
    for army, cnt in count.items():
        if cnt > majority:
            answer = army
            break

    print(answer)