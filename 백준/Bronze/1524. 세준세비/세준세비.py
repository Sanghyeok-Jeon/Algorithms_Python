T = int(input())
for _ in range(T):
    tmp = input()
    N, M = map(int, input().split())
    sj = sorted(list(map(int, input().split())))
    sb = sorted(list(map(int, input().split())))

    while True:
        if len(sj) == 0 or len(sb) == 0:
            break

        if sj[0] < sb[0]:
            sj.remove(sj[0])
        elif sj[0] >= sb[0]:
            sb.remove(sb[0])

    if len(sj) == 0:
        print('B')
    elif len(sb) == 0:
        print('S')
    else:
        print('C')
