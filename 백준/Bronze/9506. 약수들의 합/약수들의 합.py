while True:
    n = int(input())

    if n == -1:
        break

    divisor = []
    for i in range(1, n):
        if not n % i:
            divisor.append(i)

    if sum(divisor) == n:
        print(n, end=' = ')
        print(*divisor, sep=' + ')
    else:
        print('{} is NOT perfect.'.format(n))