def DFS(i):
    visited[i] = 1
    count = 1
    stack = [i]

    while stack:
        n = stack.pop()
        for j in trust[n]:
            if not visited[j]:
                visited[j] = 1
                stack.append(j)
                count += 1

    return count

N, M = map(int, input().split())
trust = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    trust[B].append(A)

max_num = -1
result = []
for i in range(1, N+1):
    if trust[i]:
        visited = [0] * (N+1)
        temp_computers = DFS(i)

        if temp_computers > max_num:
            max_num = temp_computers
            result = [i]
        elif temp_computers == max_num:
            result.append(i)

print(*result)