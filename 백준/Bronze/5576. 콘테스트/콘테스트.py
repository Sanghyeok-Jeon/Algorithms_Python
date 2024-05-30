W_score = []
for _ in range(10):
    W_score.append(int(input()))

K_score = []
for _ in range(10):
    K_score.append(int(input()))

print(sum(sorted(W_score, reverse=True)[:3]), sum(sorted(K_score, reverse=True)[:3]))