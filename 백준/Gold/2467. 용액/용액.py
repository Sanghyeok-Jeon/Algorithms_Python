import sys
input = sys.stdin.readline

def find_nearest_solution(arr):
    min_diff = float('inf')    # 합의 최소값을 저장
    result = []    # 합이 최소가 되는 두 용액

    # 투 포인터 알고리즘
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]     # 현재 합이 0에 더 가까운 경우, 최소값 갱신

        if abs(current_sum) < min_diff:
            min_diff = abs(current_sum)
            result = [arr[left], arr[right]]

        if current_sum < 0:    # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
            left += 1
        else:    # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
            right -= 1

    return result


N = int(input())
solutions = list(map(int, input().split()))

# 합이 0에 가장 가까운 용액 찾기
result = find_nearest_solution(solutions)

print(*result)