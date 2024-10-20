N = int(input())
S = input()

bonus = 0
score = 0
for i in range(N):
    if S[i] == 'X':
        bonus = 0
    else:
        score += i + 1 + bonus
        bonus += 1

print(score)