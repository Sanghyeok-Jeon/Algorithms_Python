import sys
input = sys.stdin.readline

N = int(input())

max_score = 0
for _ in range(N):
    score = list(map(int, input().split()))
    final_score = max(score[:2]) + sum(sorted(score[2:], reverse=True)[:2])

    if final_score > max_score:
        max_score = final_score

print(max_score)