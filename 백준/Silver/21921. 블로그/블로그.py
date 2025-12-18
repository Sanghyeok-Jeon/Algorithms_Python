def max_visitors(n, x, visitors):
    current_sum = sum(visitors[:x])
    max_sum = current_sum
    max_count = 1

    for i in range(x, n):
        current_sum += visitors[i] - visitors[i - x]

        if current_sum > max_sum:
            max_sum = current_sum
            max_count = 1
        elif current_sum == max_sum:
            max_count += 1

    return max_sum, max_count

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

max_sum, max_count = max_visitors(N, X, visitors)
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(max_count)