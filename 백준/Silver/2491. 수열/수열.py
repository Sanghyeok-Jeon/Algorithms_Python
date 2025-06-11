def longest_subsequence_length(data, n):
    if not data:
        return 0

    if n == 1:
        return 1

    max_length = 1
    inc_length = 1
    dec_length = 1

    for i in range(1, n):
        if data[i] > data[i - 1]:
            inc_length += 1
            dec_length = 1
        elif data[i] < data[i - 1]:
            dec_length += 1
            inc_length = 1
        else:
            inc_length += 1
            dec_length += 1

        max_length = max(max_length, inc_length, dec_length)

    return max_length

N = int(input())
data = list(map(int, input().split()))

print(longest_subsequence_length(data, N))