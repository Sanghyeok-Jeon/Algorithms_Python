import sys

input = sys.stdin.readline

N, S = map(int, input().split())
sequence = list(map(int, input().split()))

# 투 포인터 알고리즘 사용
left = right = 0    # left, right 포인터 초기화
min_length = len(sequence) + 1    # 최소 길이 무한대로 초기화
sum_value = 0    # 현재 부분합 값

while True:
    if sum_value >= S:    # 부분합이 S 이상인 경우
        min_length = min(min_length, right - left)    # 최소 길이 갱신
        sum_value -= sequence[left]    # left 포인터 이동
        left += 1
    elif right == N:    # 모든 수열을 탐색한 경우
        break
    else:    # 부분합이 S 미만인 경우
        sum_value += sequence[right]    # right 포인터 이동
        right += 1    

# 최소 길이 출력
if min_length == len(sequence) + 1:    # 최소 길이가 갱신되지 않은 경우
    print(0)
else:
    print(min_length)