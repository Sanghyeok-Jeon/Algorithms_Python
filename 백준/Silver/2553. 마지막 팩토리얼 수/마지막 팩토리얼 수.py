import sys

def last_nonzero_digit(n: int) -> int:
    base = [1, 1, 2, 6, 4]  # D(0), D(1), D(2), D(3), D(4)

    if n < 5:
        return base[n]

    # D(n) = D(n//5) * D(n%5) * 2^(n//5) (mod 10)
    return (last_nonzero_digit(n // 5) * base[n % 5] * pow(2, n // 5, 10)) % 10

n = int(sys.stdin.readline().strip())
print(last_nonzero_digit(n))