N = int(input())
lemon = [0] + list(map(int, input().split()))

max_lemon = 0
for i in range(1, N + 1):
    now_lemon = lemon[i] - (N + 1 - i)
    if now_lemon > max_lemon:
        max_lemon = now_lemon

print(max_lemon)