import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
required_mileages = []

for _ in range(n):
    p, l = map(int, input().strip().split())
    mileages = list(map(int, input().strip().split()))

    mileages.sort(reverse=True)

    if p < l:
        required_mileages.append(1)
    else:
        required_mileages.append(mileages[l - 1])

required_mileages.sort()

count = 0
total_mileage = 0

for mileage in required_mileages:
    if total_mileage + mileage <= m:
        total_mileage += mileage
        count += 1
    else:
        break

print(count)