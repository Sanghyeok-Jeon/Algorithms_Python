def find_rank(n, new_score, p, scores):
    if n == 0:
        return 1

    scores.append(new_score)
    scores.sort(reverse=True)

    rank = scores.index(new_score) + 1

    if rank > p:
        return -1

    if scores.count(new_score) > 1 and scores.index(new_score) + scores.count(new_score) > p:
        return -1

    return rank

N, newScore, P = map(int, input().split())
scores = list(map(int, input().split())) if N > 0 else []

print(find_rank(N, newScore, P, scores))