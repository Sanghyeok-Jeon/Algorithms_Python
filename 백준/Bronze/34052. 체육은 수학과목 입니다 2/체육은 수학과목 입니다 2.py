total = 0
for _ in range(4):
    total += int(input())

if total + 300 <= 1800:
    print('Yes')
else:
    print('No')