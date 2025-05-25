N = input()

if '0' not in N:
    print(-1)
else:
    sum_digit = sum(map(int, N))
    if sum_digit % 3:
        print(-1)
    else:
        print(''.join(sorted(N, reverse=True)))