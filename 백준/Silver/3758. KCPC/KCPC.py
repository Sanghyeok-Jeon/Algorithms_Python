import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())

    scores = [[0] * (k + 1) for _ in range(n + 1)]
    submit_cnt = [0] * (n + 1)
    last_submit = [0] * (n + 1)

    for time in range(1, m + 1):
        i, j, s = map(int, input().split())

        if scores[i][j] < s:
            scores[i][j] = s

        submit_cnt[i] += 1
        last_submit[i] = time

    ranking = []
    for team in range(1, n + 1):
        total_score = sum(scores[team])
        ranking.append((team, total_score, submit_cnt[team], last_submit[team]))

    ranking.sort(key=lambda x: (-x[1], x[2], x[3], x[0]))

    for rank, info in enumerate(ranking, start=1):
        if info[0] == t:
            print(rank)
            break