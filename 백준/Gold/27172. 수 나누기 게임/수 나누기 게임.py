score = [None for _ in range(1000001)]
N = int(input())
cards = list(map(int, input().split()))

# 플레이어별 점수 초기화
for card in cards:
    score[card] = 0

# 에라토스테네스의 체 활용
for card in cards:
    for j in range(card, 1000001, card):
        if score[j] is not None:    # 플레이어가 가진 카드의 배수에 해당하는 카드를 상대방이 가진 경우
            score[j] -= 1     # 상대방 패배
            score[card] += 1    # 플레이어 승리

print(*[score[card] for card in cards])