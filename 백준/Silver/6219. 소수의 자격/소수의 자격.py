a, b, d = map(int, input().split())

is_prime = [True] * (b + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(b**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, b + 1, i):
            is_prime[j] = False

count = 0
for i in range(a, b + 1):
    if is_prime[i] and str(d) in str(i):
        count += 1

print(count)