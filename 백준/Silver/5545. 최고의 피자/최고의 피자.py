N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [int(input()) for _ in range(N)]

max_ratio = C / A
D.sort(reverse=True)
current_calories = C
current_price = A

for topping in D:
    current_calories += topping
    current_price += B

    ratio = current_calories / current_price
    if ratio > max_ratio:
        max_ratio = ratio

print(int(max_ratio))