def max_earnings(n, m, earnings):
    current_sum = sum(earnings[:m])
    max_sum = current_sum

    for i in range(m, n):
        current_sum += earnings[i]- earnings[i - m]
        max_sum = max(max_sum, current_sum)

    return max_sum

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
earnings = list(map(int, input().strip().split()))

result = max_earnings(n, m, earnings)
print(result)

