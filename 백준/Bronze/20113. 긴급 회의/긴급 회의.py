N = int(input())
data = list(map(int, input().split()))

vote = [0] * (N + 1)
for d in data:
    if d == 0:
        vote[d] -= 1
    else:
        vote[d] += 1

max_vote = max(vote)
if vote.count(max_vote) >= 2:
    print('skipped')
else:
    print(vote.index(max_vote))