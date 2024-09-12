T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())
    work_parallel = d + n * p
    work_serial = n * s

    if work_parallel < work_serial:
        print('parallelize')
    elif work_parallel > work_serial:
        print('do not parallelize')
    else:
        print('does not matter')