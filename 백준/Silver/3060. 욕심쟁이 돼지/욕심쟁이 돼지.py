T = int(input())
for _ in range(T):
    N = int(input())
    food = list(map(int, input().split()))

    total_food = sum(food)
    day = 1
    while N >= total_food:
        day += 1
        total_food *= 4

    print(day)