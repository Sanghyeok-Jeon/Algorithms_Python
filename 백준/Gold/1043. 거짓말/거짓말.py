N, M = map(int, input().split())
know_truth = set(list(map(int, input().split()))[1:])
party = []
cnt = []

for _ in range(M):
    party.append(set((list(map(int, input().split()))[1:])))
    cnt.append(1)  # 전부 거짓말 가능으로 초기화

for _ in range(M):
    for i, p in enumerate(party):
        if know_truth & p:     # 진실을 아는 사람이 있는지 확인(교집합)
            cnt[i] = 0         # 거짓말 불가능 추가
            know_truth |= p    # 진실만을 말해야 되는 파티를 추가(합집합)

print(sum(cnt))