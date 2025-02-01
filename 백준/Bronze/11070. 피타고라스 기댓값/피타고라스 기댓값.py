T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    team_score = [[0, 0] for _ in range(n + 1)]
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        team_score[a][0] += p
        team_score[a][1] += q
        team_score[b][0] += q
        team_score[b][1] += p

    max_expected_value = 0
    min_expected_value = 1001
    for i in range(1, n + 1):
        S = team_score[i][0]
        A = team_score[i][1]

        if S == 0 and A == 0:
            expected_value = 0
        else:
            expected_value = int(S ** 2 / (S ** 2 + A ** 2) * 1000)

        max_expected_value = max(max_expected_value, expected_value)
        min_expected_value = min(min_expected_value, expected_value)

    print(max_expected_value)
    print(min_expected_value)