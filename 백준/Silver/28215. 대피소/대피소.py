from itertools import combinations

N, K = map(int, input().split())
homes = [list(map(int, input().split())) for _ in range(N)]

min_range = float('inf')
for shelter_idx in combinations(range(N), K):
    max_dist = 0
    for i in range(N):
        min_dist = float('inf')
        for idx in shelter_idx:
            dist = abs(homes[i][0] - homes[idx][0]) + abs(homes[i][1] - homes[idx][1])
            min_dist = min(min_dist, dist)

        max_dist = max(max_dist, min_dist)

    min_range = min(min_range, max_dist)

print(min_range)