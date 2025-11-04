import sys
input = sys.stdin.readline

def calculate_trimmed_and_adjusted_means(scores, k):
    scores.sort()
    n = len(scores)

    trimmed_scores = scores[k:n-k]
    trimmed_mean = sum(trimmed_scores) / len(trimmed_scores)

    adjusted_scores = [scores[k]]* k + scores[k:n-k]+ [scores[n-k-1]]* k
    adjusted_mean = sum(adjusted_scores) / n

    return trimmed_mean, adjusted_mean

n, k = map(int, input().split())
scores = [float(input().strip()) for _ in range(n)]

trimmed_mean, adjusted_mean = calculate_trimmed_and_adjusted_means(scores, k)

print(f"{trimmed_mean + 1e-8:.2f}")
print(f"{adjusted_mean + 1e-8:.2f}")