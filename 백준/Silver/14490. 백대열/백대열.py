import math

input_data = input().strip()
n, m = map(int, input_data.split(':'))

gcd = math.gcd(n, m)

n //= gcd
m //= gcd

print(f"{n}:{m}")