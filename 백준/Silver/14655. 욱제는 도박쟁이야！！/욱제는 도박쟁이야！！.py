N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

sum_score_first = 0
for score in first:
    sum_score_first += abs(score)

sum_score_second = 0
for score in second:
    sum_score_second += abs(score)

print(sum_score_first + sum_score_second)