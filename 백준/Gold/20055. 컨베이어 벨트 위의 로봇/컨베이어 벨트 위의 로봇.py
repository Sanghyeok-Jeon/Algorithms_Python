import sys
input = sys.stdin.readline

N, K = map(int, input().split())
durability = list(map(int, input().split()))

robots = [False] * N
step = 0

while True:
    step += 1

    # 1. 벨트 회전
    durability = [durability[-1]] + durability[:-1]
    robots = [False] + robots[:-1]
    robots[-1] = False  # 내리는 위치에 있는 로봇은 내린다

    # 2. 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and durability[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            durability[i + 1] -= 1
    robots[-1] = False  # 내리는 위치에 있는 로봇은 내린다

    # 3. 로봇 올리기
    if durability[0] > 0:
        robots[0] = True
        durability[0] -= 1

    # 4. 종료 조건 확인
    if durability.count(0) >= K:
        break

print(step)