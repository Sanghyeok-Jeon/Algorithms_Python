p = list(map(int, input().split()))
x, y, r = map(int, input().split())

num_die = 0
for i in range(1, 5):
    if x == p[i - 1]:
        num_die = i

print(num_die)