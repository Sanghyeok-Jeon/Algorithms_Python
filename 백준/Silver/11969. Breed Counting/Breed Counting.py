def breed_counting(N, Q, breeds, queries):
    prefix_holsteins = [0] * (N + 1)
    prefix_guernseys = [0] * (N + 1)
    prefix_jerseys = [0] * (N + 1)

    for i in range(1, N + 1):
        prefix_holsteins[i] = prefix_holsteins[i - 1] + (1 if breeds[i - 1] == 1 else 0)
        prefix_guernseys[i] = prefix_guernseys[i - 1] + (1 if breeds[i - 1] == 2 else 0)
        prefix_jerseys[i] = prefix_jerseys[i - 1] + (1 if breeds[i - 1] == 3 else 0)

    results = []
    for a, b in queries:
        count_holsteins = prefix_holsteins[b] - prefix_holsteins[a - 1]
        count_guernseys = prefix_guernseys[b] - prefix_guernseys[a - 1]
        count_jerseys = prefix_jerseys[b] - prefix_jerseys[a - 1]
        results.append((count_holsteins, count_guernseys, count_jerseys))

    return results

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
breeds = [int(input()) for _ in range(N)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

results = breed_counting(N, Q, breeds, queries)

for result in results:
    print(*result)
