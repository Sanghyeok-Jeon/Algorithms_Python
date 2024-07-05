import sys
input = sys.stdin.readline

N = int(input())
distances = [int(input()) for _ in range(N)]
total = sum(distances)
distances = distances * 2  # 원형 배열을 처리하기 위해 두 배로 늘림
prefix_sum = [0] * (2 * N + 1)

# 부분합 배열 생성
for i in range(1, 2 * N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + distances[i - 1]

max_distance = 0
right = 1
# 투 포인터를 이용해 최대 거리 계산
for left in range(2 * N):
    while right < 2 * N + 1 and prefix_sum[right] - prefix_sum[left] <= total - prefix_sum[right] + prefix_sum[left]:
        max_distance = max(max_distance, prefix_sum[right] - prefix_sum[left])
        right += 1

print(max_distance)