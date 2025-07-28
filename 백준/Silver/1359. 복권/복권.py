import math

def calculate_probability(n, m, k):
    total_cases = math.comb(n, m)

    winning_cases = 0
    for i in range(k, m + 1):
        if i <= n:
            winning_cases += math.comb(m, i) * math.comb(n - m, m - i)

    probability = winning_cases / total_cases

    return probability

N, M, K = map(int, input().split())

probability = calculate_probability(N, M, K)
print(probability)