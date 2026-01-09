def count_numbers(n, current_sum=0, depth=0):
    if depth == n:
        return 1 if current_sum % 3 == 0 else 0

    count = 0
    for digit in range(3):
        if depth == 0 and digit == 0:
            continue

        count += count_numbers(n, current_sum + digit, depth + 1)

    return count

n = int(input().strip())
result = count_numbers(n)
print(result)