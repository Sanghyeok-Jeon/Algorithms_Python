S = input()

length = len(S)
result = S
for i in range(1, length - 1):
    for j in range(i + 1, length):
        part_first = S[:i][::-1]
        part_second = S[i:j][::-1]
        part_third = S[j:][::-1]

        candidate = part_first + part_second + part_third

        if candidate < result:
            result = candidate

print(result)