M = int(input())

last_rotation = 1
last_belt = 0
for _ in range(M):
    a, b, belt = map(int, input().split())

    last_rotation = last_rotation // a * b

    if belt == 1:
        last_belt = 1 if last_belt == 0 else 0

print(last_belt, last_rotation)