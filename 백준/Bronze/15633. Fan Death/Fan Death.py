n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i

print(total * 5 - 24)