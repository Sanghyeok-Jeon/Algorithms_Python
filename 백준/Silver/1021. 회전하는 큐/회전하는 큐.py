from collections import deque

def minimum_operation(N, target_indices):
    q = deque(range(1, N + 1))
    operations = 0

    for target in target_indices:
        target_index = q.index(target)

        if target_index < len(q) - target_index:
            q.rotate(-target_index)
            operations += target_index
        else:
            q.rotate(len(q) - target_index)
            operations += len(q) - target_index

        q.popleft()

    return operations

N, M = map(int, input().split())
target_indices = list(map(int, input().split()))

print(minimum_operation(N, target_indices))