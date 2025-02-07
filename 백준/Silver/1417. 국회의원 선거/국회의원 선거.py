N = int(input())
pre_vote = [int(input()) for _ in range(N)]

dasom = pre_vote[0]
candidates = pre_vote[1:]

cnt = 0
while candidates and dasom <= max(candidates):
    max_votes = max(candidates)
    candidates[candidates.index(max_votes)] -= 1
    dasom += 1
    cnt += 1

print(cnt)