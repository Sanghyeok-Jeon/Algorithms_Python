N = int(input())

total_result = []
for n in range(1, N + 1):
    player_number = n
    card = list(map(int, input().split()))

    max_result = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                max_result = max(max_result, (card[i] + card[j] + card[k]) % 10)

    total_result.append([player_number, max_result])

print(sorted(total_result, key=lambda x:(-x[1], -x[0]))[0][0])