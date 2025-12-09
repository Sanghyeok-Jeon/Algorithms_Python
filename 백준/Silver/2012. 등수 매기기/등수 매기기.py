import sys
input = sys.stdin.readline

n = int(input())
expected_ranks = [int(input()) for _ in range(n)]

expected_ranks.sort()

dissatisfaction = 0
for actual_rank in range(1, n + 1):
    dissatisfaction += abs(expected_ranks[actual_rank - 1] - actual_rank)

print(dissatisfaction)