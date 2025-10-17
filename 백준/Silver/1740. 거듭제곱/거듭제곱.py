def solve(n):
    result = 0
    power = 1

    while n > 0:
        if n % 2 == 1:
            result += power
        n //= 2
        power *= 3

    return result

n = int(input())
print(solve(n))