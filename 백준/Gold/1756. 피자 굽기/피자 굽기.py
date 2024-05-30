import sys
input = sys.stdin.readline

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

# 위쪽 지름이 아래쪽 지름보다 작으면 아래쪽 지름을 위쪽 지름과 같이 변경.
for i in range(1, D):
    if oven[i] > oven[i - 1]:
        oven[i] = oven[i - 1]

idx = D - 1    # 오븐 가장 아래에서 부터 피자 넣을 수 있는지 확인.
for i in range(N):
    while idx >= 0 and oven[idx] < pizza[i]:    # 피자 넣을 수 있을 때까지 위로 올라감.
        idx -= 1

    if idx < 0:    # 피자가 모두 오븐에 들어가지 않는 경우
        print(0)
        sys.exit(0)

    idx -= 1

print(idx + 2)