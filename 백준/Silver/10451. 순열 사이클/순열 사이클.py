def find_cycles(permutation):
    visited = [False] * len(permutation)
    cycle_count = 0

    for i in range(len(permutation)):
        if not visited[i]:
            cycle_count += 1
            current = i
            while not visited[current]:
                visited[current] = True
                current = permutation[current] - 1

    return cycle_count

t = int(input())
for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    result = find_cycles(permutation)
    print(result)