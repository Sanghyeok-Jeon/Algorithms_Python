N = int(input())
M = int(input())
X = list(map(int, input().split()))

answer = 0

len_start = 0
len_end = 0
max_len_xs = 0
for i in range(M):
    if i == 0:
        len_start = X[i]
        if M == 1:
            len_end = N - X[i]
    elif i == (M - 1):
        len_end = N - X[i]
        max_len_xs = max(X[i] - X[i - 1], max_len_xs)
    else:
        max_len_xs = max(X[i] - X[i - 1], max_len_xs)

half_max_len_xs = max_len_xs // 2 + 1 if max_len_xs % 2 else max_len_xs // 2

answer = max(len_start, len_end, half_max_len_xs)

print(answer)