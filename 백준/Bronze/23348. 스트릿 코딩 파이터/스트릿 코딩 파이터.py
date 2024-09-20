A, B, C = map(int, input().split())
N = int(input())

max_score = 0
for _ in range(N):
    tmp_score = 0
    for i in range(3):
        a, b, c = map(int, input().split())
        tmp_score += A * a + B * b + C * c

    max_score = max(max_score, tmp_score)

print(max_score)