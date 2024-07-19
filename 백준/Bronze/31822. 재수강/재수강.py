target = input()[:5]

answer = 0
N = int(input())
for _ in range(N):
    subject = input()
    if target == subject[:5]:
        answer += 1

print(answer)