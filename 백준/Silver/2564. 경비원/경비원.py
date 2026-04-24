w, h = map(int, input().split())
n = int(input())

stores = [tuple(map(int, input().split())) for _ in range(n)]
dong_dir, dong_pos = map(int, input().split())


def to_line(direction, pos):
    # 사각형 둘레를 한 줄로 펼쳤을 때의 위치
    if direction == 1:      # 북쪽: 왼쪽에서 오른쪽
        return pos
    elif direction == 2:    # 남쪽: 오른쪽에서 왼쪽 방향으로 둘레 진행
        return w + h + (w - pos)
    elif direction == 3:    # 서쪽: 아래에서 위쪽 방향으로 둘레 진행
        return 2 * w + h + (h - pos)
    else:                   # 동쪽: 위에서 아래
        return w + pos


perimeter = 2 * (w + h)
dong = to_line(dong_dir, dong_pos)

answer = 0

for d, p in stores:
    store = to_line(d, p)
    dist = abs(dong - store)
    answer += min(dist, perimeter - dist)

print(answer)