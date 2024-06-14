from collections import deque

def bfs(N, M, K):
    # 초기 상태 (a, b, c, d) = (N, M, 0, 0)
    initial_state = (N, M, 0, 0)
    queue = deque([(initial_state, 0)])
    visited = set()
    visited.add(initial_state)

    while queue:
        (a, b, c, d), steps = queue.popleft()

        # 모든 학생이 융합인재관으로 이동한 경우
        if a == 0 and c == N:
            return steps

        # 창의인재관에서 융합인재관으로 이동
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                if x <= K * y:
                    new_state = (a - x, b - y, c + x, d + y)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))

        # 융합인재관에서 창의인재관으로 이동
        for z in range(1, c + 1):
            for w in range(1, d + 1):
                if z <= K * w:
                    new_state = (a + z, b + w, c - z, d - w)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))

    return -1

# 입력 받기
T = int(input())
results = []

for _ in range(T):
    N, M, K = map(int, input().split())
    result = bfs(N, M, K)
    print(result)