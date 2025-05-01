def solve():
    n = int(input())

    if n == 0:
        print("NO")
        return

    fact = [1]
    i = 1
    while fact[-1] <= n:
        fact.append(fact[-1] * i)
        i += 1

    fact.reverse()

    for f in fact:
        if n >= f:
            n -= f

    if n == 0:
        print("YES")
    else:
        print("NO")


solve()