import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())    # 박스 정보의 개수. [보내는 마을, 받는 마을, 박스 개수]
array = [list(map(int, input().split())) for _ in range(M)]
array.sort(key=lambda x: (x[1], x[0]))    # 배달 종료점이 작은 순으로 정렬. 같을 경우 배달 시작점이 작은 순으로 정렬.

answer = 0
capacity = [C] * (N + 1)    # 각 마을에서의 트럭 현재 용량. 초기 용량은 트럭 최대 용량 C로 초기화.
for i in range(M):
    tmp = min(array[i][2], min(capacity[array[i][0]:array[i][1]]))    # 현재 마을에서 배달할 수 있는 박스의 최대 수. 현재 박스의 수와 트럭의 현재 용량 중 작은 값.
    for j in range(array[i][0], array[i][1]):    # 트럭 용량 갱신. 배달한 박스의 수만큼 용량 감소.
        capacity[j] -= tmp

    answer += tmp    # 배달한 박스의 총 수 갱신.

print(answer)