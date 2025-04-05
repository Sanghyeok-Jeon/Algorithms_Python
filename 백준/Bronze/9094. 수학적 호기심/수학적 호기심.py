memory = [[0] * 101 for _ in range(101)]

for b in range(2, 101) :
    for a in range(1, b) :
        memory[b][a] = a ** 2 + b ** 2

for _ in range(int(input())) :
    n, m = map(int, input().split())
    cnt = 0
    for b in range(2, n) :
        for a in range(1, b) :
            if (memory[b][a] + m) % (a * b) == 0:
                cnt += 1

    print(cnt)