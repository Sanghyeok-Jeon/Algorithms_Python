from collections import deque

def bfs(hp):
    # 초기 상태
    initial_state = tuple(hp)
    queue = deque([(initial_state, 0)])
    visited = set()
    visited.add(initial_state)

    # 공격 조합
    attacks = [
        (9, 3, 1),
        (9, 1, 3),
        (3, 9, 1),
        (3, 1, 9),
        (1, 9, 3),
        (1, 3, 9)
    ]

    while queue:
        (a, b, c), steps = queue.popleft()

        # 모든 적의 체력이 0 이하인 경우
        if a <= 0 and b <= 0 and c <= 0:
            return steps

        # 다음 상태로 이동
        for attack in attacks:
            na = max(0, a - attack[0])
            nb = max(0, b - attack[1])
            nc = max(0, c - attack[2])
            new_state = (na, nb, nc)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))

    return -1

# 입력 받기
N = int(input())
hp = list(map(int, input().split()))

# 체력이 3개가 되도록 0을 추가
while len(hp) < 3:
    hp.append(0)

# 결과 출력
print(bfs(hp))