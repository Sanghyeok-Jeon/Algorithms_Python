import sys
input = sys.stdin.readline

N = int(input())
weight_limit = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

if box[0] > weight_limit[0]:
    print(-1)
else:
    time = 0
    while box:
        time += 1
        for wl in weight_limit:
            if box and box[-1] > wl:
                continue

            for i in range(len(box)):
                if wl >= box[i]:
                    del box[i]
                    break

    print(time)
